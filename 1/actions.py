# -*- coding: utf-8 -*-
import hashlib
import web
import time
import os
import urllib2,json
import lxml
from lxml import etree
import json

import youdao
from busline import buslineRes


def eventAction(xml): #事件消息处理
    if(xml.find("Event").text == 'subscribe'): #用户首次关注
        text = "你好，欢迎关注yaphone生活小助手，目前正处于开发阶段，功能还很buggy，不断完善ing"
        return text
    
def textAction(xml): #文本信息处理
    content=xml.find("Content").text#获得用户所输入的内容
    if(u'查公交' in content):
#        return content
        return buslineRes(content)
    youdaoRes = youdao.youdao(content)
    return youdaoRes