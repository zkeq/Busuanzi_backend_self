# coding:utf-8
import requests
from replit import db
import time


def get_before_data(host):
    url = "https://busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback_777487655111"
    payload = {}
    headers = {
        'Referer': "https://" + host,
        'Cookie': 'busuanziId=89D15D1F66D2494F91FB315545BF9C2A'
    }
    response = None
    while not response:
        response = requests.request("GET", url, headers=headers, data=payload)
        print("遇到错误，正在重试")
        time.sleep(1)
    str_2_dict = eval(response.text[34:][:-13])
    site_uv = str_2_dict["site_uv"]
    site_pu = str_2_dict["site_pv"]
    db[host] = {"pv": 0, "data": {"/": 0}}
    db[host]["pv"] = site_pu
    db[host]["uv"] = site_uv
    print("写入新网址数据成功")
