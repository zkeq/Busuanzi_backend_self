# coding:utf-8
import subprocess
from urllib.parse import urlparse

import redis
import uvicorn
from fastapi import FastAPI, Request, Header, Response

from get_before_data import get_before_data
from pv import pv
from uv import ip_in_and_conter_out

chmod_redis = "chmod 755 ./redis-server"

start_redis = "./redis-server redis.conf"

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

app = FastAPI(docs_url=None, redoc_url=None)


@app.post("/")
def root(request: Request,
        response: Response,
        x_bsz_referer: str = Header(None),
):
    if not x_bsz_referer:
        return Response(content="Powered by: FastAPI + Redis", media_type="text/plain")
    client_host = request.client.host
    url_res = urlparse(x_bsz_referer)
    host = url_res.netloc
    path = url_res.path
    if "index" in path:
        path = path.split("index")[0]
    site_uv_before = r.get("live_site:%s" % host)
    if not site_uv_before:
        site_uv_before = get_before_data(host)
    else:
        site_uv_before = int(site_uv_before.decode())
    uv = ip_in_and_conter_out(host, client_host) + site_uv_before
    page_pv, site_pv = pv(host, path)
    dict_data = {
        "site_uv": uv,
        "page_pv": page_pv,
        "site_pv": site_pv,
        "version": 2.1
    }
    response.headers["Content-Type"] = "application/json"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return dict_data


@app.get("/")
def root_get():
    return Response(content="Powered by: FastAPI + Redis", media_type="text/plain")


# 加一个option请求
@app.options("/")
def root_option():
    return Response(status_code=204,headers={
        "Access-Control-Allow-Methods": "GET,POST,HEAD,OPTIONS",
        "Access-Control-Allow-Headers": "x-bsz-referer",
        "Access-Control-Max-Age": "86400",
        "Access-Control-Allow-Origin": "*"})


if __name__ == "__main__":
    print("chmod redis")
    subprocess.run(chmod_redis, shell=True)
    print("start redis")
    subprocess.Popen(start_redis, shell=True)
    print("start uvicorn")
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", proxy_headers=True, forwarded_allow_ips="*")
