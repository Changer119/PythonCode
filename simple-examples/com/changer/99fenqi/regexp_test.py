#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def getFileContent(filePath):
    with open(filePath, "rt", encoding="utf-8") as f:
        lines = f.read()
        # for x in lines:
        #     print(x)
        return lines

if __name__ == "__main__":
    content = getFileContent("plain_html.txt")
    # pattern = re.compile(r'href="touziren\.jsp\?method(.*?)>(.*?)</a>', re.S)
    # # ll = re.findall(r"[\u4e00-\u9fa5]", content, re.S)
    # print("==================================")
    # result = pattern.findall(content)
    # names = []
    # for x in result:
    #     names.append(x[1])
    # print(names)

    trs = re.findall(r"<tr(.*?)</tr>", content, re.S)

    # 遍历再去匹配
    order_infos = []
    for item in trs:
        m = re.search(r"href", item, re.S)
        if m:
            # print("hanlde")
            # print(item)
            aa = re.findall(r"href=\"(.*?)\">(.*?)</a>(.*?)<td>(\d{18})</td>(.*?)<td align=\"right\">(.*?)</td>", item, re.S)
            # print(aa)
            if len(aa):
                r = aa[0]
                order_info = []
                order_info.append(r[0])
                order_info.append(r[1])
                order_info.append(r[3])
                order_info.append(r[5])
                order_infos.append(order_info)
        else:
            print("not handle")
    print(order_infos)