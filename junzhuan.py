import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
import time
import re
import json
import pymongo
from lxml import etree
import csv
from multiprocessing import Pool
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

he = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
      }


def getpage(info):
    # html = requests.get(url, headers=he)
    # print(html.text)
    getMain = re.findall(r'<tbody id="separatorline"(.*?)</body>', info, re.S)[0]
    #print(getMain)
    types = re.findall('<em>\[<a href=".*?">(.*?)</a>\]</em>', getMain, re.S)
    print(types)
    titles = re.findall('</em> <a href=".*?" onclick="atarget\(this\)" class="s xst">(.*?)</a>', getMain, re.S)
    print(titles)
    # authors = re.findall(r'<a href=".*?" c="1".*？>(.*?)</a></cite>[\s\S]*?<em><span>', getMain, re.S)
    # authors = re.findall(r'<a href="https://junzhuan\.com/space-uid.*?" c="1.*?>(.*?)</a></cite>[\s\S]*?<em><span>',
    # getMain, re.S)
    authors = re.findall(r'<a href="https://junzhuan.com/space-uid-.*?html" c=.*?>(.*?)</a></cite>', getMain, re.S)
    print(authors)
    times = re.findall(r'<em><span>(.*?)</span></em>', getMain, re.S)
    print(times)
    replys = re.findall(r'<td class="num"><a href=".*?" class="xi2">(.*?)</a><em>', getMain, re.S)
    print(replys)
    sees = re.findall(r'<td class="num"><a href=".*?" class="xi2">.*?</a><em>(.*?)</em>', getMain, re.S)
    print(sees)
    for type, title, author, time, reply, see in zip(types, titles, authors, times, replys, sees):
        print(type, title, author, time, reply, see)
        writer.writerow((type, title, author, time, reply, see))
        pass


if __name__ == '__main__':
    fp = open('d:\\junzhuan_自主.csv', 'wt', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('类别', '标题', '作者', '时间', '回复', '查看数'))

    browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
    '''
    try:
        browser.get('http://www.baidu.com')
        keyword = browser.find_element_by_id('kw')
        keyword.send_keys('Python')
        keyword.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
        print(browser.current_url)
        print(browser.get_cookies())
        print(browser.page_source)
    finally:
        browser.close()
    '''
    urls = []
    for i in range(1, 1001):
        url = 'https://junzhuan.com/forum-5-{}.html'.format(i)
        urls.append(url)
        browser.get(url)
        browser.implicitly_wait(10)
        getpage(browser.page_source)
        time.sleep(1)
        # time.sleep(k)
    print(urls)

    # print(driver.page_source)
    # pool = Pool(processes=4)
    # pool.map(getpage,urls)
    fp.close()
    # pool.map(getinfo, urls)
