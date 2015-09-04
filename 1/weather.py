#coding:UTF-8

import urllib 
import json

def weather(content):
    juhe_url = 'http://v.juhe.cn/weather/index?'
    key = '&key=' + '98344ecd560b15c559ceba1ca9841a4e'
    content_list = content.split(' ')
    cityname = '&cityname=' + content_list[1]
    url = juhe_url + cityname + key
    response = urllib.urlopen(url.encode('utf-8')).read()
    
    res_dict = json.JSONDecoder().decode(response)
    if res_dict['resultcode'] == '200':
        now_weather = ''
        now_weather_dict = res_dict['result']['sk'] #当前温度字典
        now_temp = u'当前温度： ' + now_weather_dict['temp'] + '\n' #当前温度
        now_wind_direction = u'当前风向： ' + now_weather_dict['wind_direction'] + '\n' #当前风向
        now_wind_strength = u'当前风力： ' + now_weather_dict['wind_strength'] + '\n' #当前风力
        now_humidity = u'当前湿度： ' + now_weather_dict['humidity'] +'\n' #当前湿度
        now_time = u'更新时间： ' + now_weather_dict['time'] + '\n' #更新时间
        
        now_weather = now_temp + now_wind_direction + now_wind_strength + now_humidity + now_time
        return now_weather