# coding:utf-8
import uvicorn
from typing import Optional
from fastapi import FastAPI, Request, Header
from fastapi.responses import HTMLResponse
from urllib.parse import urlparse
from uv import ip_in_and_conter_out
from get_before_data import get_before_data
from replit import db

keys = db.keys()
from pv import pv
import json

app = FastAPI(docs_url=None, redoc_url=None)


def read_white_site(site):
    print("来路:", site)
    with open("white_list.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    if site in data:
        return True
    else:
        return False


@app.get("/", response_class=HTMLResponse)
def root(request: Request,
         referer: str = Header(None),
         user_agent: str = Header(None),
         jsonpCallback: str = ""
         ):
    client_host = request.client.host
    url_res = urlparse(referer)
    host = url_res.netloc
    path = url_res.path
    data_chose = read_white_site(host)
    if not data_chose or not host:
        return '<meta http-equiv="refresh" content="0;url=https://busuanzi.icodeq.com">'
    try:
        db[host]["uv"]
    except:
        get_before_data(host)
    uv = ip_in_and_conter_out(host, client_host)
    page_pv, site_pv = pv(host, path)
    dict_data = {
        "site_uv": uv,
        "page_pv": page_pv,
        "site_pv": site_pv,
        "version": 2.4
    }
    data_str = "try{" + jsonpCallback + "(" + json.dumps(dict_data) + ");}catch(e){}"
    print(data_str)
    return data_str


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="info", proxy_headers=True, forwarded_allow_ips="*")
