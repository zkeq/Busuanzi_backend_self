from replit import db


def pv(host, path):
    if not db.get(host):
        db[host] = {"pv": 0, "data": {"/": 0}}
    db[host]["pv"] += 1
    print(db[host])
    if not db[host]["data"].get(path):
        db[host]["data"][path] = 0
    db[host]["data"][path] += 1
    page_pv = db[host]["data"][path]
    site_pv = db[host]["pv"]
    return page_pv, site_pv
