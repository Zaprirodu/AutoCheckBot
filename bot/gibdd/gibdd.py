import json
import asyncio
import aiohttp
import datetime
import html


from ..gibdd import data_type
from ..utils import recaptcha
from ..config import API_TOKEN


id = {'gibdd': ['vehicle', 'ownershipPeriods'],
      'dtp': 'Accidents',
      'wanted': 'records',
      'restrict': 'records',
      'eaisto': 'diagnosticCards'}




car = {}

async def get_check_auto(session, key, VIN):

    params = {
        'vin': VIN,
        'type': key,
        'token': API_TOKEN
    }
    url = f"https://api-cloud.ru/api/gibdd.php"




    async with session.get(url=url, params=params) as requests:
        counter = 0
        try:
            req = await requests.json(content_type=None)
        except json.decoder.JSONDecodeError as error:
            print(error)
            print(requests)
            print(requests.status)

            while requests.status == 429 or requests.status == 404:
                await asyncio.sleep(1)
                async with session.post(url=url, params=params) as requests:
                   req = await requests.json(content_type=None)

    print(req)
# запрос по регистрации !Перевел на апи
    if key == 'gibdd':
        d_register = req['vehicle']
        p_register = req['ownershipPeriod']

        car['registr'] = {
            'model': d_register['model'],
            'year': d_register['year'],
            'color': d_register['color'],
            'VIN': VIN,
            'numberEngine': d_register['engineNumber'],
            'workingVol': d_register['engineVolume'],
            'power': d_register['powerHp'],
            'type_car': d_register['typeinfo']
        }
        car['period'] = []
        for num in p_register:
            car['period'].append({
                'date_from': num['from'],
                'date_to': num['to'],
                'period': num['period'],
                'typePerson': num['simplePersonTypeInfo'],
                'last_oper': num['lastOperationInfo']
            })



# запрос по дтп !Перевел на апи
    elif key == 'dtp':
        car['dtp'] = []
        if (req['count']) == 0:
            car['dtp'].append('По указанному VIN номеру не найдено данных')
        else:
            d_dtp = req["records"]
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


# запрос по розыску !Перевел на апи
    elif key == 'wanted':
        car['wanted'] = []
        if (req['count']) == 0:
            car['wanted'].append('По указанному VIN номеру не найдено данных')
        else:
            d_wanted = req["records"]
            for num in d_wanted:
                car['wanted'].append({
                    'model_w': num['w_model'],
                    'year_w': num['w_god_vyp'],
                    'data_w': num['w_data_pu'],
                    'region_w': num['w_reg_inic']
                })
            if len(car['wanted']) == 0:
                car['wanted'].append('По указанному VIN номеру не найдено данных')


# запрос по ограничениям !Перевел на апи
    elif key == 'restrict':
        car['limit'] = []
        if (req['count']) == 0:
            car['limit'].append('По указанному VIN номеру не найдено данных')
        else:
            d_limit = req["records"]
            for num in d_limit:
                car['limit'].append({
                    'date_l': num['dateogr'],
                    'region_l': num['regname'],
                    'organ_l': num['divtypeinfo'],
                    'type_l': num['ogrkodinfo'],
                    'osnov_l': num['osnOgr'],
                    'phone_l': num['phone'],
                    'KeyGID_l': num['gid']
                })
            if len(car['limit']) == 0:
                car['limit'].append('По указанному VIN номеру не найдено данных')


# запрос по диагностике !Перевел на апи
    elif key == 'eaisto':
        car['diagnostic'] = []

        if req['count'] == 0:
            car['diagnostic'].append('По указанному VIN номеру не найдено данных')
        else:
            d_diagnostic = req["records"]
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
    print(car)
    return car

async def getVin(gosnum):
    query = f"vin={gosnum}" if len(gosnum) == 17 else f"regNumber={gosnum}"
    payload = f"https://api-cloud.ru/api/rsa.php?type=osago&{query}&token={API_TOKEN}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url=payload) as response:
            resp = await response.read()
            r = json.loads(resp)
    print(r)

    try:
        VIN = r['rez'][0]['vin']
        GOS = r['rez'][0]['regnum']
        OSAGO = r['rez']
    except:
        raise ValueError('VIN не найден')
    return [VIN, GOS, OSAGO]

