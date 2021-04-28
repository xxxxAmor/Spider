import json
import ast
import re
out=set()
with  open('E:\文本内容计算\mySpider\split\splitprocorpus3.txt',encoding='utf-8') as f:
    for a in f:
        if a.startswith(u'\ufeff'):
            a= a.encode('utf8')[3:].decode('utf8')
    #a=json.loads(a)   #将字符串转换为字典
        a=ast.literal_eval(a)
        b=a['value']
        words = [str(i) for i in b['words']]
        words = ''.join(words)
        tuple = (words,b['documentId'])
        out.add(tuple)
        
list_out=list(out)
#print(list_out[0],type(list_out[0]))   #列表元素是元组
f = open('E:\文本内容计算\mySpider\quchong\corpus.txt', 'a+',encoding='utf-8')
for line in list_out:
     f.write(str(line)+"\n")
print("OK!!!!!!!!!")
