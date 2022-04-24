# coding:utf-8
import requests
import redis
import time

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


def get_before_data(host):
    url = "https://busuanzi.ibruce.info/busuanzi?jsonpCallback=BusuanziCallback_777487655111"
    payload = {}
    headers = {
        'Referer': "https://" + host + "/",
        'Cookie': 'busuanziId=89D15D1F66D2494F91FB315545BF9C2A'
    }
    response = None
    while not response:
        response = requests.request("GET", url, headers=headers, data=payload)
        print("首次连接，正在从不蒜子官网拉取数据")
        time.sleep(1)
    str_2_dict = eval(response.text[34:][:-13])
    site_uv = str_2_dict["site_uv"]
    page_pv = str_2_dict["page_pv"]
    site_pv = str_2_dict["site_pv"]
    r.set("live_site:%s" % host, site_uv, ex=60 * 60 * 24 * 30)
    # r.set("page_pv:%s:/" % host, page_pv, ex=60 * 60 * 24 * 30)
    # page pv 不过期了
    r.set("page_pv:%s:/" % host, page_pv)
    r.set("site_pv:%s" % host, site_pv, ex=60 * 60 * 24 * 30)
    print("写入新网址数据成功")
    print("网址:%s" % host)
    print("全站访问人数:%s" % site_uv)
    print("首页访问量:%s" % page_pv)
    print("全站访问量:%s" % site_pv)
    return site_uv
