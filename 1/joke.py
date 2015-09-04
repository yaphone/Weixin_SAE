#coding:UTF-8

import urllib
import json
import random

def joke():
    url = "http://api.laifudao.com/open/xiaohua.json"
    response = urllib.urlopen(url)
    html = response.read()
    res = json.JSONDecoder().decode(html)
    num = random.randint(0, 9)
    title = res[num]['title']
    content = res[num]['content']
    response = title + '\n\n' + content
    response = response.replace('<br/>', ' ')
    return response
