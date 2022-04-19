# bilibili 评论数据抓取
# -*- coding: utf-8 -*-
# Author : richard
# Date : 2022/3/7


import requests

import json
import time
import pandas as pd
import datetime
oid='680449533'

comment_api = 'https://api.bilibili.com/x/v2/reply?pn=1&type=1&oid='+oid+'&sort=2'  # sort=2按热度

response = requests.get(url=comment_api)
data_json = response.text
data = json.loads(data_json)

#alldata_num = data['data']['page']['acount']#总评论数
alldata_num = data['data']['page']['count']  # 根评论数
print(alldata_num)
# 创建一个df存放爬取到的数据
cols = ['rpid', 'rcount', 'mid', 'current_level', 'sex', 'vipStatus', 'text', 'like', 'ctime', 'message']
df = pd.DataFrame(index=range(alldata_num), columns=cols)

flag = 0  # (计数用)
num1 = 1514  # （分段用）
j = 0 # 控制总循环
k = 0 # 控制页数
while j < (num1):
    flag = flag + 1
    count = 0
    for i in range(len(data['data']['replies'])):

        # cols = ['rpid','rcount','mid','current_level','sex','vipStatus','text','like','ctime','message']
        # 评论的id
        df.loc[j, 'rpid'] = data['data']['replies'][i]['rpid']
        # 评论的回复数量
        df.loc[j, 'rcount'] = data['data']['replies'][i]['rcount']
        # 第一条作者id、等级、性别、是否vip、vip描述
        df.loc[j, 'mid'] = data['data']['replies'][i]['member']['mid']
        df.loc[j, 'current_level'] = data['data']['replies'][i]['member']['level_info']['current_level']
        df.loc[j, 'sex'] = data['data']['replies'][i]['member']['sex']
        df.loc[j, 'vipStatus'] = data['data']['replies'][i]['member']['vip']['vipStatus']
        df.loc[j, 'text'] = data['data']['replies'][i]['member']['vip']['label']['text']
        # 第一条评论内容 点赞数
        df.loc[j, 'like'] = data['data']['replies'][i]['like']
        # 第一条评论内容 #ctime 发送时间
        df.loc[j, 'ctime'] = data['data']['replies'][i]['ctime']
        # 第一条评论内容
        df.loc[j, 'message'] = data['data']['replies'][i]['content']['message']
        # print(data_list[i]['progress'])
        # df.loc[j,'progress'] = data_list[i]['progress']
        j = j + 1
        count = count + 1
        #print(df)
    print('已经完成第' + str(k) + '页')
    k = k + 1
    url = 'https://api.bilibili.com/x/v2/reply?pn=' + str(k) + '&type=1&oid='+oid+'&sort=2'  # 记得改oid
    # print('url:',url)
    response = requests.get(url=url)
    data_json = response.text
    data = json.loads(data_json)

    if flag % 5 == 0:
        print('\033[1;35m进度{}% \033[0m'.format(round(j / num1 * 100, 1)))
        time.sleep(1)
    time.sleep(0.5)
print('\033[1;31m进度100% \033[0m')
print('j:', j)
print('k:', k)
print('url', url)
df.to_excel('暖 暖 的，很 烫 嘴.xlsx',encoding='utf8')