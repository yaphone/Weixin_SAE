#coding=utf-8

import urllib
import json
import sys


def youdao(content):
    url = "http://fanyi.youdao.com/openapi.do?keyfrom=YaphoneTek&key=819376396&type=data&doctype=json&version=1.1&q=" + content.encode("utf-8")
    response = urllib.urlopen(url)
    html = response.read()
    data = json.loads(html)
    res = ""    
    for ans in data["translation"]:
        res += ans + '\n'
    return res


