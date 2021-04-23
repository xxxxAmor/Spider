# -*- coding:utf-8 -*-
from datetime import datetime

source_dir = 'E:\文本内容计算\mySpider\splitprocorpus3.txt'
target_dir = 'E:\文本内容计算\mySpider\split'

# 计数器
flag = 0

# 文件名
name = 1

# 存放数据
dataList = []

print("开始")
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

with open(source_dir, 'r', encoding="utf-8") as f_source:
    for line in f_source:
        flag += 1
        dataList.append(line)
        if flag == 1000000:
            with open(target_dir+"procorpus"+str(name)+".txt", 'w+', encoding="utf-8") as f_target:
                for data in dataList:
                    f_target.write(data)
            name += 1
            flag = 0
            dataList = []

    # 处理最后一批行数少于200万行的
with open(target_dir+"procorpus"+str(name)+".txt", 'w+', encoding="utf-8") as f_target:
    for data in dataList:
        f_target.write(data)

print("完成")
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


