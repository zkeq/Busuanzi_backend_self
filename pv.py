from replit import db


def pv(host, path):
    try: 
        pv_data = db[host]
        print("数据库拿到pv")
    except:
        pv_data  = {"pv": 0, "data": {"/": 0}}
        db[host] = pv_data
    pv_data["pv"] += 1
    print("全站pv成功加1")
    try:
      pv_data["data"][path] += 1
      print("单页pv成功加1")
    except:
      pv_data["data"][path] = 0
    page_pv = pv_data["data"][path]
    print("单页pv", page_pv)
    site_pv = pv_data["pv"]
    print("全站pv", site_pv)
    db[host] = pv_data
    print("放回数据库")
    return page_pv, site_pv
