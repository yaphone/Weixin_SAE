#coding:utf-8
import os



def POST(self):
    str_xml = web.data() #获得post来的数据
    xml = etree.fromstring(str_xml)#进行XML解析
    msgType=xml.find("MsgType").text        
    msgTypeDict = {'subscribe': subscribeAction, 'text': textAction}
    msgTypeDict[msgType](xml)