# coding: UTF-8

import urllib
import json


def buslineRes(content):  
    
    url = 'http://op.juhe.cn/189/bus/busline?'
    key = 'key=ebe44ee7130cc7fcc443079f15a0f165' + '&'
    content_list = content.split(' ')
    if(len(content_list)<3):
        return u'请输入：“查公交+城市+线路”进行查询，注意将“+”号换为空格，如“查公交 重庆 347”'
    city = 'city=' + content_list[1] + '&'
    bus = 'bus=' + content_list[2]
    req = url + key + city + bus
    res = urllib.urlopen(req.encode('utf-8')).read()
    response = jsonHandler(res)
    return response
    
    
def jsonHandler(res):
    response = ''
    json_dict = json.JSONDecoder().decode(res)
    if(json_dict['reason']=='success'):
        result_list = json_dict['result']
        
        #去程        
        come_terminal_name = result_list[0]['terminal_name'] #去程终端站名称
        come_stations_list = result_list[0]['stationdes'] # 去程站台列表
        come_station_num = 1  # 去站台序号
        response += u'往' + come_terminal_name + u'方向' + '\n'
        for station in come_stations_list:
            response += str(come_station_num) + ' ' + station['name'] + '\n'
            come_station_num += 1
        response += '\n'
        
            
        #返程
        back_terminal_name = result_list[1]['terminal_name'] #去程终端站名称
        back_stations_list = result_list[1]['stationdes'] # 去程站台列表
        back_station_num = 1  # 去站台序号
        response += u'往' + back_terminal_name + u'方向' +'\n'
        for station in back_stations_list:
            response += str(back_station_num) + ' ' + station['name'] +'\n'
            back_station_num += 1
        return response
    return u'查询失败，请检查输入，正确输入为：查公交+城市+线路，+号换为空格'
    