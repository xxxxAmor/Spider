import time

import requests
import json
import threading
from ua_list import ua_list
from ip_list import ip_list
import random

def call_post(n):
    url = 'http://202.112.194.62:8084/query'
    ua = random.choice(ua_list)
    proxies = random.choice(ip_list)
    headers = {"User-Agent": ua}
    f = open("words.txt", "r", encoding='utf-8')
    count = len(f.readlines())
    f = open("words.txt", encoding='utf-8')
    a = {}
    for line, i in zip(f, range(count)):
        a[i] = line
    for i in a:
        content = a[i]
        data = {
            "content": content,
            "type": 1

        }
    #data = {"content": "测试"}
        r = requests.post(url, data=json.dumps(data), headers=headers)
        print('线程' + str(n) + ':' + str(r.status_code))  # n为并发数
        #print(r.headers)
        data = r.headers
        cur = 'http://202.112.194.62:8084/'
        cur = cur + data['Stream-Location']
        # print(cur)
        f = open("url_list.txt", "a+")  # 打开文件以便写入
        print(cur, file=f)
        f.close  # 关闭文件


def thread(n):
    threads = []

    for i in range(0, n):  # n 为并发数
        t = threading.Thread(target=call_post, args=(i,))
    # 针对函数创建线程，target为调用的并发函数，args为调用函数的参数，该参数必须为数组，所以这里加了逗号，如果不加就不是数组，运行会报错
        threads.append(t)   # 添加线程到线程组
        print(threads)

        for t in threads:
            t.start()   # 开启线程
        for t in threads:
            t.join()   # 等待所有线程终止
thread(3)
# if __name__ == '__main__':
#     call_post()
#

