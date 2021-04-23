# a1={"kind": "match", "value": {"words": ["这", "次", "黄浦区", "有关", "部门", "执法", "之后", ",", "没有", "做", "“", "甩手", "政府", "”", ",", "而", "是", "主动", "牵线搭桥", ",", "帮助", "阿大", "与", "某", "网络", "订餐", "平台", "达成", "合作", "协议", ",", "由", "该", "平台", "出资", "为", "“", "阿大", "葱油饼", "”", "在", "原址", "附近", "寻得", "新址", ",", "并", "承担", "新", "店", "开设", "的", "租金", "。"], "captures": {}, "highlights": [{"start": 21, "end": 21}], "sentenceId": "0b955e053f338a9a5790388eed8c81090a2105d19e9a3bc69d806385f4d0f30d", "sentence_index": 8, "sentence_uri": "/sentences?id=0b955e053f338a9a5790388eed8c81090a2105d19e9a3bc69d806385f4d0f30d", "documentId": "docs/人民日报/docs/2017/01/12/人民日报20170112.0040.json.gz", "metadata": {"id": "人民日报20170112.0040", "doc_type": "story", "headline": "“阿大葱油饼”为何能重张", "newspaper": "人民日报", "date": "20170112", "DATELINE": "2017年01月12日"}}}
# a2={"kind": "match", "value": {"words": ["这", "次", "黄浦区", "有关", "部门", "执法", "之后", ",", "没有", "做", "“", "甩手", "政府", "”", ",", "而", "是", "主动", "牵线搭桥", ",", "帮助", "阿大", "与", "某", "网络", "订餐", "平台", "达成", "合作", "协议", ",", "由", "该", "平台", "出资", "为", "“", "阿大", "葱油饼", "”", "在", "原址", "附近", "寻得", "新址", ",", "并", "承担", "新", "店", "开设", "的", "租金", "。"], "captures": {}, "highlights": [{"start": 37, "end": 37}], "sentenceId": "0b955e053f338a9a5790388eed8c81090a2105d19e9a3bc69d806385f4d0f30d", "sentence_index": 8, "sentence_uri": "/sentences?id=0b955e053f338a9a5790388eed8c81090a2105d19e9a3bc69d806385f4d0f30d", "documentId": "docs/人民日报/docs/2017/01/12/人民日报20170112.0040.json.gz", "metadata": {"id": "人民日报20170112.0040", "doc_type": "story", "headline": "“阿大葱油饼”为何能重张", "newspaper": "人民日报", "date": "20170112", "DATELINE": "2017年01月12日"}}}
# #print(type(a))   #dict
# #print(a['value'])
# b1=a1['value']
# b2=a2['value']
# #print(type(b))   #dict
# words1 = [str(i) for i in b1['words']]
# words1 = ''.join(words1)
# words2 = [str(i) for i in b2['words']]
# words2 = ''.join(words2)
# tuple1 = (words1,b1['sentenceId'],b1['documentId'])
# print(tuple1)
# tuple2 = (words1,b2['sentenceId'],b2['documentId'])
# print(tuple2)

# set=set()
# set.add(tuple1)
# set.add(tuple2)
# print(set)


#------------------------------------------------------------------------------------------------------------------------------

#去除空行
# with open('corpus1.txt','r',encoding = 'utf-8') as fr,open('procorpus1.txt','w',encoding = 'utf-8') as fd:
#         for text in fr:
#                 if text.split():
#                         fd.write(text)
#
#
#         print('输出成功....')    #3224句

# import linecache
# c = linecache.getlines("test1.txt")
# for i in range(1,10):
#     a=c[i]
#     b=a['value']
#     words = [str(i) for i in b['words']]
#     words = ''.join(words)
#     tuple = (words,b['sentenceId'],b['documentId'])
#     set=set()
#     set.add(tuple)
# print(set)

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
