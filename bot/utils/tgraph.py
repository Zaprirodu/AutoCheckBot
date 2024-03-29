import json
import itertools
import aiohttp
import uuid
import time
import hashlib
import asyncio

from ..gibdd import templates
from ..gibdd import gibdd
from ..config import API_TOKEN
# Основная функция - createReport(vin)
# функция возвращает URL отчета, в самом внизу закомментирован пример

# vin - получаем из тг бота
# Пример вызова функции из тг бота - tgraph.createReport(vin)

#Пример объекта, который возвращает gibdd.get_data(vin)
json1 = {
    "registr": {
        "model": "РЕНО САНДЕРО ",
        "year": "2011",
        "color": "СИНИЙ",
        "VIN": "X7LBSRBYHBH427587",
        "numberEngine": "D150460",
        "workingVol": "1598.0",
        "power": "102.0",
        "type_car": "Легковые автомобили комби (хэтчбек)"
    },
    "period": [
        {
            "date_from": "2011-09-08",
            "date_to": "2018-09-14",
            "typePerson": "Физическое лицо",
            "last_oper": "первичная регистрация"
        },
        {
            "date_from": "2018-09-14",
            "date_to": "настоящее время",
            "typePerson": "Физическое лицо",
            "last_oper": "изменение собственника (владельца)"
        }
    ],
    "dtp": [
        {
            "number_dtp": "750055709",
            "time_dtp": "01.10.2016 19:30",
            "type_dtp": "Столкновение",
            "place_dtp": "Челябинская область, Чебаркульский район, Чебаркуль",
            "model_dtp": "нет данных"
        },
        {
            "number_dtp": "750038272",
            "time_dtp": "17.06.2015 19:00",
            "type_dtp": "Столкновение",
            "place_dtp": "Челябинская область, Чебаркульский район, Г Чебаркуль",
            "model_dtp": "нет данных"
        }
    ],
    "wanted": [
        "По указанному VIN номеру не найдено данных"
    ],
    "limit": [
        "По указанному VIN номеру не найдено данных"
    ],
    "diagnostic": [
        {
            "number_dc": "052930012005017",
            "date_dc": "2020-08-12",
            "date_end_dc": "2022-08-13",
            "addres_dc": "641877, КУРГАНСКАЯ ОБЛАСТЬ, ШАДРИНСК ГОРОД, , БАТУРИНСКАЯ УЛИЦА, 19, 0, 0",
            "brand_dc": "RENAULT",
            "model_dc": "SANDERO",
            "odometr_dc": "113000"
        }
    ]
}

#Токен Telegra.ph. Можно сгененерировать свой
token = 'c0c4bc25e50641cb84eda4bb0cf29deb6384ee959b0ca257142177c9e7e8'

async def getImageAuto(gosnum):
    params = {
        'regNum': gosnum,
        'type': 'regnum',
        'token': API_TOKEN
    }
    url = f"https://api-cloud.ru/api/autophoto.php"
    img = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url, params=params) as requests:
            req = await requests.json(content_type=None)
            if req['count'] != 0:
                for i in req['records']:
                    img.append(i['urlphoto'])


    return img


async def getLinksAuto(gosnum):
    tstamp = str(round(time.time()*1000))
    secret = hashlib.sha256(
        f"p15{gosnum}8163461e568122437b580aa8e6df6940history{tstamp}queivoo1ieNgae2e"
            .encode('utf-8')
    ).hexdigest()
    headers = {
        'User-Agent': 'Nomerogram/2.34.0 (Android; samsung; SM-G988N; 1.00)'
    }
    info = {
        'src':[],
        'link':[]
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://www.nomerogram.ru/api/v1.1/group/list?carplate={gosnum}&"
                               f"device_id=8163461e568122437b580aa8e6df6940&"
                               f"from=history&"
                               f"app_id=p15&"
                               f"timestamp={tstamp}&"
                               f"secret={secret}", headers=headers) as response:
            r = await response.json()
            print(r)
            for data_el in r['data']['groups']:
                info['link'].append(data_el['group_url'])
                for photo in data_el['photos']:
                    info['src'].append(photo['src']['default'])
        return info




async def createVIN(gosNum):
    vin = await gibdd.getVin(gosNum)
    url = await createReport(vin)
    return url

async def createReport(num):
    vin, gosnum, osago = await gibdd.getVin(num)
    print("OSAGO!!",osago)
    autoObj = await gibdd.get_data(vin)
    ngram = await getLinksAuto(gosnum)
    img = await getImageAuto(gosnum)
    content = list(itertools.chain(
        mainInfo(autoObj),
        usedPeriod(autoObj),
        dtp(autoObj),
        limits(autoObj),
        diagnostics(autoObj),
        social(ngram['link']),
        osag(osago),
        images(img)
    ))

    data = {
        "access_token": token,
        "title": "Автоотчет #"+str(uuid.uuid1()),
        "content": json.dumps(content),
    }
    # print(data)
    async with aiohttp.ClientSession() as session:
        async with session.post("https://api.telegra.ph/createPage", data=data) as response:
            r = await response.json()

    #r = requests.post("https://api.telegra.ph/createPage", data=data).json()
    print(r['result']['url'])
    return r['result']['url']



def mainInfo(autoObj):
    obj = [
        {'tag': 'h4', 'children': ['Базовая информация']}
    ]
    m = autoObj['registr']
    obj.append({
            'tag': 'p',
            'children': [templates.main_template.format(m['model'], m['VIN'], m['year'], m['color'], m['numberEngine'],
                                                        m['workingVol'], m['power'], m['type_car'])]
    })
    return obj


def usedPeriod(autoObj):
    obj = [
        {'tag': 'h4', 'children': ['Периоды владения ТС']}
    ]
    for period in autoObj['period']:
        desc_period = templates.used_template.format(period['date_from'],period['date_to'],
                                                     period['typePerson'],period['last_oper'])
        obj.append({
            'tag': 'p',
            'children': [desc_period]
        })
    return obj


def dtp(autoObj):
    obj = [
        {'tag': 'h4', 'children': ['Сведения о ДТП']}
    ]
    if type(autoObj['dtp'][0]) == str:
        obj.append({'tag': 'p', 'children': ['Не найдено']})
    else:
        for dtp in autoObj['dtp']:
            dtp_desc = templates.dtp_template.format(dtp['number_dtp'], dtp['time_dtp'], dtp['type_dtp'],
                                                     dtp['place_dtp'])
            obj.append({'tag': 'p', 'children': [dtp_desc]})
    return obj


def limits(autoObj):
    obj = [
        {'tag': 'h4', 'children': ['Данные об ограничениях']}
    ]
    if type(autoObj['limit'][0]) == str:
        obj.append({'tag': 'p', 'children': ['Не найдено']})
    else:
        for limit in autoObj['limit']:
            limit_desc = templates.limits_template.format(limit['type_l'], limit['osnov_l'], limit['organ_l'],
                                                          limit['date_l'], limit['region_l'], limit['phone_l'])
            obj.append({'tag': 'p', 'children': [limit_desc]})
    return obj


def diagnostics(autoObj):
    obj = [
        {'tag': 'h4', 'children': ['Данные о диагностической карте']}
    ]
    try:
        if type(autoObj['diagnostic'][0]) == str:
            obj.append({'tag': 'p', 'children': ['Не найдено']})
        else:
            for diag in autoObj['diagnostic']:
                diag_desc = templates.diagnostic_template.format(diag['number_dc'], diag['date_dc'], diag['date_end_dc'],
                                                                 diag['addres_dc'], diag['odometr_dc'])
                obj.append({'tag': 'p', 'children': [diag_desc]})
    except:
        obj.append({'tag': 'p', 'children': ['Не найдено']})
    return obj  


def images(img_lst):
    obj = []
    if len(img_lst) == 0:
        obj.append({'tag': 'h4', 'children': ['Дополнительных изображений не найдено']})
    else:
        for count, img in enumerate(img_lst):
            if (count > 5):
                break
            obj.append({
                'tag': 'a',
                'children': [{
                    'tag': 'img',
                    'attrs': {'src': img}
                }]
            })
    return obj



def social(soc_lst):
    obj = []
    if len(soc_lst) == 0:
        obj.append({'tag': 'h4', 'children': ['Упоминаний не найдено']})
    else:
        obj.append({'tag': 'h4', 'children': ['Найдены упоминания: ']})
        for soc in soc_lst:
            obj.append({
                'tag': 'p',
                'children':[{
                    'tag': 'a',
                    'children': [soc],
                    'attrs': {'href': soc}
                }]
            })
    return obj


def osag(osgh):
    obj = [
        {'tag': 'h4', 'children': ['Данные об ОСАГО']}
    ]
    try:
        for diag in osgh:
            diag_desc = templates.osago_template.format(diag['seria'] + " " + diag['nomer'], diag['orgosago'],
                                                        diag['status'],
                                                        diag['cel'], diag['owner'])
            obj.append({'tag': 'p', 'children': [diag_desc]})
    except:
        obj.append({'tag': 'p', 'children': ['Не найдено']})
    return obj

# Пример генерации отчета
#print(createReport('X7LBSRBYHBH427587'))
