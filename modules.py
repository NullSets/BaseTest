import math

print(math.sin(0))


import sys
sys.path.append('c:/pythonModule')   #告诉解释器在哪里寻找模块
import hello
import hello   #多次导入只导入一次


import hello2
hello2.hello()


import sys,pprint
pprint.pprint(sys.path)


import constants
print(constants.PI)


import constants.colors
from constants import shapes


# dir
import copy
print([n for n in dir(copy) if not n.startswith("_")])

print(copy.__all__)

help(copy)

#查看源代码位置
print(copy.__file__)




"""
 10.3 标准库
"""
import sys
#sys.argv
#sys.exit(0)
#sys.modules
#sys.path
#sys.stdin、sys.stdout、sys.stderr

import os
print(os.environ["PATH"])
#os.system(r'C:\"Program Files (x86)"\"Mozilla Firefox"\firefox.exe')    #运行外部程序
#os.startfile(r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe")    #接受一般路径，就算包含空格也没问题
#import subprocess
print(os.sep)         # \
print(os.pathsep)     # ;
print(os.linesep)     # \r\n

import webbrowser         #启动浏览器或者使用已经打开的浏览器
#webbrowser.open("http://www.baidu.com")

#遍历文本文件的所有行
import fileinput
# fileinput.input()
# fileinput.filename()
# fileinput.lineno()
# fileinput.filelineno()
# fileinput.isfirstline()
# fileinput.isstdin()
# fileinput.nextfile()
# fileinput.close()


"""
10.3.4 集合、堆和双端队列
"""
"""
集合
"""
print(set(range(10)))
a = set([1,2,3])
b = set([2,3,4])
print(a.union(b))
c = a & b
print(c.issubset(a))
print(c <= a)
print(c.issuperset(a))
print(c >= a)
print(a.intersection(b))
print(a & b)
print(a.difference(b))
print(a - b)
print(a.symmetric_difference(b))
print(a ^ b)
print(a.copy())
print(a.copy() is a)

a = set()
b = set()
a.add(frozenset(b))

"""
堆
"""
from heapq import *
from random import shuffle
data = range(10)
#shuffle(data)
heap = []
for n in data:
    heappush(heap,n)
print(heap)
heappush(heap,0.5)
print(heap)
print(heappop(heap))
print(heappop(heap))
print(heappop(heap))
print(heap)

heap = [5,8,0,3,6,7,9,1,4,2]
heapify(heap)
print(heap)
heapreplace(heap,0.5)
print(heap)
heapreplace(heap,10)
print(heap)
print(nlargest(1,heap))
print(nsmallest(1,heap))

"""
双端队列
"""
from collections import deque
q = deque(range(5))
q.append(5)
q.appendleft(6)
print(q)
print(q.pop())
print(q.popleft())
q.rotate(3)
print(q)
q.rotate(-1)
print(q)
