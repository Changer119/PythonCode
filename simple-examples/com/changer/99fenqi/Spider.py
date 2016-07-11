#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


class Spider(object):
    def __init__(self):
        print("开始爬取99分期数据")

    def login(self, username, password, yzm):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36",
            "Origin": "chrome-extension://hgmloofddffdnphfgcellkdfbfbjeloo",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6"
        }
        loginData = {"aname": username, "apass": password, "yzm": yzm}
        loginUrl = "http://tzr.fenqifu.com.cn:20000/index.jsp"
        cookies = {"JSESSIONID": "9BB83248A29BCC1924A310A3806A0117"}

        # s = requests.Session()
        # rr = s.post(loginUrl, data=loginData, headers=headers, cookies=cookies)
        # print(rr)

        resp = requests.post(loginUrl, data=loginData, headers=headers, cookies=cookies)
        print(resp.text)

        # s = requests.Session()
        # # post 数据实现登录
        # rr = s.post('http://tzr.fenqifu.com.cn:20000/index.jsp', loginData, headers=headers)
        # html = self.getHtml("http://tzr.fenqifu.com.cn:20000/touziren/touziren.jsp?method=listOrdersAnjia")
        # print(html

        text = self.getHtml("http://tzr.fenqifu.com.cn:20000/touziren/order_ajax.jsp")
        print(text)

    def getHtml(self, url):
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.text
        else:
            print("抓取网页出错 url=", url)

    def getOrderInfos(self, html):
        orderInfos = []
        

if __name__ == "__main__":
    spider = Spider()
    spider.login("51信用卡债转", "51xinyongka", "9060")