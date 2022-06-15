import requests
import json
import time
import aiohttp
import asyncio

async def get_task():
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "clientKey": "c915e62ed93b9d0e6e08620b7642e951",
        "task":
            {
                "type": "NoCaptchaTaskProxyless",
                "websiteURL": "https://dkbm-web.autoins.ru/dkbm-web-1.0/policyInfo.htm",
                "websiteKey": "6Lf2uycUAAAAALo3u8D10FqNuSpUvUXlfP7BzHOk"
            }
    })
    # print(data)

    #r = requests.post("https://api.capmonster.cloud/createTask", headers=headers,data=data).json()

    async with aiohttp.ClientSession() as session:
        async with session.post(url="https://api.capmonster.cloud/createTask", headers=headers,
                                data=data.encode("utf-8")) as response:
            r = await response.read()
            response = json.loads(r)

        
    return response["taskId"]

async def get_resp(id):
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "clientKey": "c915e62ed93b9d0e6e08620b7642e951",
        "taskId": id
    })
    # print(data)

    for tr in range(10):
        async with aiohttp.ClientSession() as session:
            async with session.post(url="https://api.capmonster.cloud/getTaskResult/", headers=headers,
                                data=data) as response:
                r = await response.read()
                response = json.loads(r)
        #r = requests.post("https://api.capmonster.cloud/getTaskResult/", headers=headers, data=data).json()
        print(response)
        if response['status'] == 'ready':
            break
        asyncio.sleep(2)
    return response['solution']['gRecaptchaResponse']

async def solution():
    while True:
        try:
            resp = await get_resp(await get_task())
            break
        except:
            print('Истекло время решения рекапчи. Пробую еще раз.')
            continue

    return resp

