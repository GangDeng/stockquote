#-*- coding:utf-8 -*-

from selenium import webdriver
import sys
import urllib2
import re

reload(sys)
sys.setdefaultencoding("utf8")

def getHtml(url):
    request = urllib2.Request(url)
    html = urllib2.urlopen(request).read()
    html = html.decode('gbk')
    return html
def getStackCode(html):
    s = r'<li><a target="_blank" href="http://quote.eastmoney.com/\S\S(.*?).html">'
    pat = re.compile(s)
    code = pat.findall(html)
    return code
def getzjlxhtml(driver,baseurl,code):
    driver.get(baseurl+code+".html")
    return driver.page_source

Url = 'http://quote.eastmoney.com/stocklist.html'
urlzjlx = "http://data.eastmoney.com/zjlx/"

code = getStackCode(getHtml(Url))
CodeList = []
for item in code:
    itemstr = item.encode('gbk')
    if (itemstr.startswith('6') or itemstr.startswith('300') or itemstr.startswith('000') or itemstr.startswith('002')):
      CodeList.append(itemstr)
driver = webdriver.PhantomJS(executable_path='/home/gangdeng/tools/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
for code in CodeList:
    page = getzjlxhtml(driver,urlzjlx,code)
    with open("zjlx_0525/"+code+".html","wb") as f:
        f.write(page)
driver.quit()

