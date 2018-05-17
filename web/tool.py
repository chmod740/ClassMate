import json
from time import time
import os
import httplib2


def get_location(ip):
    http = httplib2.Http()
    url = 'http://int.dpool.sina.com.cn/iplookup/iplookup.php'
    body = 'format=json&ip=' + str(ip)
    url = url + '?' + body
    response, content = http.request(uri=url)
    content = content.decode('utf8')
    try:
        content_dict = eval(content)
        country = content_dict.get('country')
        province = content_dict.get('province')
        city = content_dict.get('city')
        return country + ' ' + province + ' ' + city
    except:
        return ''