# -*- coding: UTF-8 -*-
# !/usr/bin/python3
# 版权所有 © 艾科瑞特科技
# 艾科瑞特（iCREDIT）-让企业业绩长青
# 预知更多业绩长青，请与我们联系
# 联系电话：0532-88984128
# 联系邮箱：market@itruth.xin

import urllib
import urllib.request
import time

#UUID采用当前程序运行时间，用于防止重放攻击，开发者可根据自己需求，自定义字符串
UUID = str(time.time())
#API产品路径
host = 'http://globlal.market.alicloudapi.com'
path = '/ai_market/ai_airplane/get_global_airplane_list'
#阿里云APPCODE
appcode = '你的阿里云APPCODE' 
#出发城市_中文，如：新加坡
START_CH = urllib.request.quote('新加坡')
#抵达城市_中文，如：伦敦(英)
END_CH = urllib.request.quote('伦敦(英)')
#出发城市_英文缩写，如：SIN
START_EN = 'SIN'
#抵达城市_英文缩写，如：LON
END_EN = 'LON'
#出发日期，如：20190323
START_DATE = '20190323'
#抵达日期，如：20190325
END_DATE = '20190325'
#开始航班信息数量，如：20，指从第20条信息开始，默认单次数据至多返回20条航班信息
START_AIRLINE = '0'
#结束航班信息数量，如：40，指至第40条信息技术，默认单次数据至多返回20条航班信息
END_AIRLINE = '20'
#航程类型，如：单程为1，往返为2
TYPE = '1'

querys = 'START_CH=%s&END_CH=%s&START_EN=%s&END_EN=%s&START_DATE=%s&END_DATE=%s&START_AIRLINE=%s&END_AIRLINE=%s&TYPE=%s' %(START_CH,END_CH,START_EN,END_EN,START_DATE,END_DATE,START_AIRLINE,END_AIRLINE,TYPE)
url = host + path + '?' + querys
request = urllib.request.Request(url)
request.add_header('Authorization', 'APPCODE ' + appcode)
request.add_header('X-Ca-Nonce', UUID)
request.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content.decode('utf-8'))
