#!/usr/bin/env python
# coding=utf-8
# By Ku Jui
import requests
from bs4 import BeautifulSoup
#浏览器中的header
hdrs = {'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)'}
url = "http://10.5.7.39/polarion/#/project/EAGLEII/workitems/softwareUnit"
r = requests.get(url, headers = hdrs)
soup = BeautifulSoup(r.content.decode('utf8', 'ignore'), 'lxml')
#定义变量
tbody = "empty"
tbody = soup.find('div')
#获取SVN版本号
#for tag in soup.find_all('td', id_='FIELD_SVNversion'):
#    subversion = tag.fing('div').get_text()
#    nums = subversion
print(tbody)