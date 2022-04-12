# coding:utf-8

import os
import json
from replit import db


def ip_in_and_conter_out(site_name, ip):
  file_name = "ips/" + site_name + ".json"
  if not os.path.exists(file_name):
    with open(file_name, "w") as f:
      f.write("[]")
  with open(file_name, 'r+', encoding='utf-8') as f:
      data = json.load(f)
  if ip not in data:
    data.append(ip)
  counter = len(data) + db[site_name]['uv']
  with open(file_name, 'w', encoding='utf-8') as f:
      f.write(json.dumps(data))
  return counter