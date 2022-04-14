from replit import db


def pv(host, path):
    try: 
        pv_data = db[host]
    except:
        pv_data  = {"pv": 0, "data": {"/": 0}}
    pv_data["pv"] += 1
    try:
      pv_data["data"][path] += 1
    except:
      pv_data["data"][path] = 0
    page_pv = pv_data["data"][path]
    site_pv = pv_data["pv"]
    db[host] = pv_data
    return page_pv, site_pv
