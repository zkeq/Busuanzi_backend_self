# coding:utf-8

import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


def ip_in_and_conter_out(site_name, ip):
    r.sadd("site_uv:%s" % site_name, ip)
    site_uv = r.scard("site_uv:%s" % site_name)
    r.expire("site_uv:%s" % site_name, 60 * 60 * 24 * 30)
    r.expire("live_site:%s" % site_name, 60 * 60 * 24 * 30)
    return site_uv
