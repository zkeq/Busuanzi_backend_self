import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

r.sadd("site_uv:icodeq.com", "127.0.0.1")
