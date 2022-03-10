import requests
import json
import time


def get_task():
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
    r = requests.post("https://api.capmonster.cloud/createTask", headers=headers,data=data).json()
    return r["taskId"]

def get_resp(id):
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "clientKey": "c915e62ed93b9d0e6e08620b7642e951",
        "taskId": id
    })
    # print(data)

    for tr in range(10):
        r = requests.post("https://api.capmonster.cloud/getTaskResult/", headers=headers, data=data).json()
        print(r)
        if r['status'] == 'ready':
            break
        time.sleep(5)
    return r['solution']['gRecaptchaResponse']

def solution():
    while True:
        try:
            resp = get_resp(get_task())
            break
        except:
            print('Истекло время решения рекапчи. Пробую еще раз.')
            continue

    return resp

