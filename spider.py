from bs4 import BeautifulSoup
from ua_list import ua_list
# 使用了线程库
import threading
# 队列
# from queue import queue
from multiprocessing import Queue
# 解析库
# from lxml import etree
# 请求处理
import requests
# json处理
import json
import time
import linecache
import random

class thread_crawl(threading.Thread):
    '''
    抓取线程类
    '''

    def __init__(self, threadID, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.q = q

    def run(self):
        print("Starting " + self.threadID)
        self.qiushi_spider()
        print("Exiting ", self.threadID)

    def qiushi_spider(self):
        # page = 1
        while True:
            if self.q.empty():
                break
            else:
                j= self.q.get()
                print(j)
                print('myspider=', self.threadID)
                str = linecache.getlines("url_list1.txt")
                url=str[j]
                ua = random.choice(ua_list)
                headers = {"User-Agent": ua}
               
                timeout = 4
                while timeout > 0:
                    timeout -= 1
                    try:
                        content = requests.get(url, headers=headers)
                        data_queue.put(content.text)
                        break

                    except Exception as e:
                        print('myspider', e)
                if timeout < 0:
                    print('timeout', url)


class Thread_Parser(threading.Thread):
    '''
    页面解析类；
    '''

    def __init__(self, threadID, queue, lock, f):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.queue = queue
        self.lock = lock
        
        

    def run(self):
        print ('starting ', self.threadID)
        global total, exitFlag_Parser
        while not exitFlag_Parser:
            try:
                '''
                调用队列对象的get()方法从队头删除并返回一个项目。可选参数为block，默认为True。
                如果队列为空且block为True，get()就使调用线程暂停，直至有项目可用。
                如果队列为空且block为False，队列将引发Empty异常。
                '''
                item=self.queue.get(False)
                if not item:
                    pass
                self.parse_data(item)
                self.queue.task_done()
                print('Thread_Parser=', self.threadID, ',total=', total)
            except:
                pass
        print('Exiting ', self.threadID)

    def parse_data(self, content):
        '''
        解析网页函数
        :param item: 网页内容
        :return:
        '''
        global total
        try:
            soup=BeautifulSoup(content, 'html.parser')
            text=soup.find_all(text = True)
            

            with self.lock:
                        
                f = open('corpus1.txt', 'a+',encoding='utf-8')
                f.write(text[0])
        except Exception as e:
            print('parse_data', e)
        with self.lock:
            total += 1

data_queue=Queue()
exitFlag_Parser=False
lock=threading.Lock()
total=0

def main():
    output=open('qiushibaike.json', 'a')

    pageQueue=Queue(68007)
    for j in range(1, 68007):
        pageQueue.put(j)
    
            

    # 初始化采集线程
    crawlthreads=[]
    crawlList=["crawl-1", "crawl-2", "crawl-3","crawl-4","crawl-5","crawl-6","crawl-7","crawl-8"]

    for threadID in crawlList:
        thread=thread_crawl(threadID, pageQueue)
        thread.start()
        crawlthreads.append(thread)

    # 初始化解析线程parserList
    parserthreads=[]
    parserList=["parser-1", "parser-2", "parser-3","parser-4","parser-5","parser-6","parser-7","parser-8"]
    # 分别启动parserList
    for threadID in parserList:
        thread=Thread_Parser(threadID, data_queue, lock, output)
        thread.start()
        parserthreads.append(thread)

    # 等待队列清空
    while not pageQueue.empty():
        pass

    # 等待所有线程完成
    for t in crawlthreads:
        t.join()

    while not data_queue.empty():
        pass
    # 通知线程退出
    global exitFlag_Parser
    exitFlag_Parser=True

    for t in parserthreads:
        t.join()
    print("Exiting Main Thread")
    with lock:
        output.close()


if __name__ == '__main__':
    main()
