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


'''

{u'errorCode': 0, u'query': u'\u90a3\u597d', u'translation': [u"That's good"],
 u'web': [{u'key': u'\u90a3\u597d', u'value': [u'Then good', u'that good', u'das ist gut']},
          {u'key': u'\u90a3\u5c31\u597d', u'value': [u'Good', u"That's good", u'Then good']}, 
          {u'key': u'\u90a3\u5c31\u597d\u4e86', u'value': [u"That's good", u'It is good']}]}
          
{u'errorCode': 0, u'query': u'\u597d', u'translation': [u'good'],
u'web': [{u'key': u'\u597d', u'value': [u'Good', u'fine', u'bueno']}, 
{u'key': u'\u5f88\u597d', u'value': [u'very good', u'Fine', u'very well']}, 
{u'key': u'\u51c6\u5907\u597d', u'value': [u'Be prepared', u'Ready', u'to be ready for']}],
u'basic': {u'phonetic': u'h\xe0o,h\u01ceo', u'explains': [u'all right', u'well', u'good', u'fine', u'ok']}}

'''