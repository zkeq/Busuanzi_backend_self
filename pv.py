import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


def pv(host, path):
    page_pv = r.incr("page_pv:%s:%s" % (host, path))
    # page_pv 不加了
    # r.expire("page_pv:%s:%s" % (host, path), 60 * 60 * 24 * 30)
    site_pv = r.incr("site_pv:%s" % host)
    r.expire("site_pv:%s" % host, 60 * 60 * 24 * 30)
    return page_pv, site_pv
