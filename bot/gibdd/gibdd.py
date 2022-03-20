import json
import asyncio
import aiohttp
import time

from ..damage_points import get_dtp
from ..gibdd import data_type


id = {'history': ['vehicle', 'ownershipPeriods'],
      'dtp': 'Accidents',
      'wanted': 'records',
      'restrict': 'records',
      'diagnostic': 'diagnosticCards'}


car = {}

async def get_check_auto(session, key, VIN):
    headers = {
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'ru,en;q=0.9,ko;q=0.8',
        'Connection': 'keep - alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.1.932 Yowser/2.5 Safari/537.36'
    }
    params = {
        'vin': VIN,
        'checkType': key
    }
    url = f"https://xn--b1afk4ade.xn--90adear.xn--p1ai/proxy/check/auto/{key}"




    async with session.post(url=url, headers=headers, params=params) as requests:
        counter = 0
        try:
            req = await requests.json(content_type=None)
            while req.get('RequestResult') == None:
                await asyncio.sleep(1)
                counter += 1
                if (counter < 5):
                    async with session.post(url=url, headers=headers, params=params) as requests:
                       req = await requests.json(content_type=None)
                else:
                    req = None
                    break

            while requests.status == 429 or requests.status == 404:
                await asyncio.sleep(1)
                async with session.post(url=url, headers=headers, params=params) as requests:
                   req = await requests.json(content_type=None)
        except json.decoder.JSONDecodeError as error:
            print(error)
            print(requests)
            print(requests.status)

            while requests.status == 429 or requests.status == 404:
                await asyncio.sleep(1)
                async with session.post(url=url, headers=headers, params=params) as requests:
                   req = await requests.json(content_type=None)


# запрос по регистрации
    if key == 'history':
        d_register = req["RequestResult"][id[key][0]]
        p_register = req["RequestResult"][id[key][1]]['ownershipPeriod']
        if d_register.get('engineNumber') == None:
            d_register['engineNumber'] = '-'
            d_register['engineVolume'] = '-'
        car['registr'] = {
            'model': d_register['model'],
            'year': d_register['year'],
            'color': d_register['color'],
            'VIN': VIN,
            'numberEngine': d_register['engineNumber'],
            'workingVol': d_register['engineVolume'],
            'power': d_register['powerHp'],
            'type_car': data_type.auto_types[d_register['type']]
        }
        car['period'] = []
        for num in p_register:
            if num.get('to') == None:
                num['to'] = 'настоящее время'
            car['period'].append({
                'date_from': num['from'],
                'date_to': num['to'],
                'typePerson': data_type.type_owner[num['simplePersonType']],
                'last_oper': data_type.typeOperation[num['lastOperation']]
                })


# запрос по дтп
    elif key == 'dtp':
        car['dtp'] = []
        d_dtp = req["RequestResult"][id[key]]
        for num in d_dtp:
            car['dtp'].append({
                'number_dtp': num['AccidentNumber'],
                'time_dtp': num['AccidentDateTime'],
                'type_dtp': num['AccidentType'],
                'place_dtp': num['AccidentPlace'],
                'model_dtp': num['VehicleMark'],
                'dmp_dtp': num['DamagePoints'],
                #'way_image': get_dtp.svgtopng(num['DamagePoints']),
            })
        if len(car['dtp']) == 0 :
            car['dtp'].append('По указанному VIN номеру не найдено данных')


# запрос по розыску
    elif key == 'wanted':
        car['wanted'] = []
        d_wanted = req["RequestResult"][id[key]]
        for num in d_wanted:
            car['wanted'].append({
                'model_w': num['w_model'],
                'year_w': num['w_god_vyp'],
                'data_w': num['w_data_pu'],
                'region_w': num['w_reg_inic']
            })
        if len(car['wanted']) == 0:
            car['wanted'].append('По указанному VIN номеру не найдено данных')


# запрос по ограничениям
    elif key == 'restrict':
        car['limit'] = []
        d_limit = req["RequestResult"][id[key]]
        for num in d_limit:
            car['limit'].append({
                'date_l': num['dateogr'],
                'region_l': num['regname'],
                'organ_l': data_type.organs[num['divtype']],
                'type_l': data_type.ogr[num['ogrkod']],
                'osnov_l': num['osnOgr'],
                'phone_l': num['phone'],
                'KeyGID_l': num['gid']
            })
        if len(car['limit']) == 0:
            car['limit'].append('По указанному VIN номеру не найдено данных')


# запрос по диагностике
    elif key == 'diagnostic':
        car['diagnostic'] = []

        if req == None:
            car['diagnostic'].append('По указанному VIN номеру не найдено данных')
        else:
            d_diagnostic = req["RequestResult"][id[key]]
            for num in d_diagnostic:
                car['diagnostic'].append({
                    'number_dc': num['dcNumber'],
                    'date_dc': num['dcDate'],
                    'date_end_dc': num['dcExpirationDate'],
                    'addres_dc': num['pointAddress'],
                    'brand_dc': num['brand'],
                    'model_dc': num['model'],
                    'odometr_dc': num['odometerValue']
                })
            if len(car['diagnostic']) == 0:
                car['diagnostic'].append('По указанному VIN номеру не найдено данных')


    print(f"[INFO] Обработал страницу {key}")



async def get_data(VIN):
    async with aiohttp.ClientSession() as session:

        tasks = []

        for key in id:

            task = asyncio.create_task(get_check_auto(session, key, VIN))
            tasks.append(task)

        await asyncio.gather(*tasks)

    return car

async def getVin(gosnum):
    now = datetime.datetime.now()
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = "bsoseries=ССС&bsonumber=&requestDate={}" \
              "&vin=&licensePlate={}" \
              "&bodyNumber=&chassisNumber=&isBsoRequest=false&captcha={}".format(now.strftime("%d.%m.%Y"), gosnum,
                                                                                 recaptcha.solution())

    # r = requests.post(url="https://dkbm-web.autoins.ru/dkbm-web-1.0/policyInfo.htm", headers=headers, data=payload.encode('utf-8'), verify=False).json()

    async with aiohttp.ClientSession() as session:
        async with session.post(url="https://dkbm-web.autoins.ru/dkbm-web-1.0/policyInfo.htm", headers=headers,
                                data=payload.encode('utf-8')) as response:
            r = await response.json()

    payload = "processId={}" \
              "&bsoseries=ССС&bsonumber=&vin=&licensePlate={}" \
              "&bodyNumber=&chassisNumber=&requestDate={}" \
              "&g-recaptcha-response=".format(r['processId'], gosnum, now.strftime("%d.%m.%Y"))
    while True:
        # r = requests.post(url="https://dkbm-web.autoins.ru/dkbm-web-1.0/policyInfoData.htm", headers=headers,
        #              data=payload.encode('utf-8'), verify=False)

        async with aiohttp.ClientSession() as session:
            async with session.post(url="https://dkbm-web.autoins.ru/dkbm-web-1.0/policyInfoData.htm", headers=headers,
                                    data=payload.encode('utf-8')) as response:
                r = html.fromstring(await response.read()).xpath('//tr[./td[text()="VIN"]]/td[2]/text()')

        try:
            VIN = r[0]
            break
        except:
            if ('Сведения о договоре ОСАГО с указанными данными не найдены.' in r.text):
                raise ValueError('VIN не найден')
            else:
                continue
    return VIN
