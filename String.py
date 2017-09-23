"""
所有标准的序列操作（索引、分片、乘法、判断成员资格、求长度、取最大最小值）对
字符串同样适用

但，字符串是不可变的

"""


"""
格式化字符串中有%，则可使用%%
"""
"""
%s 
%f   
%.3f：保留三位
%r

"""

#字符串模板
from string import Template
s = Template("$x,glorious $x!")
s.substitute(x = 'slurm')   #'slurm,glorious slurm!'
s = Template("It's ${x}tastic!")
s.substitute(x = 'slurm')  #替换一部分
#  $$ ：插入$
s = Template("A $thing must never $action")
d = {}
d['thing'] = 'gentleman'
d['action'] = 'show his socks'
s.substitute(d)   #使用字典



"""
3.3 字符串格式化
"""

from math import pi
print("%10f" % pi)                             #  3.141593
print("%10.2f" % pi)                           #      3.14
print("%.2f" % pi)                             #3.14
print("%.5s" % "Guido van Rossum")             #Guido
print("%.*s" % (5,"Guido van Rossum"))         #Guido
print("%010.2f" % pi)                          #0000003.14
print("%-10.2f" % pi)    #减号表示左对齐       #3.14      | 注意有空格
print(("% 5d" % 10) + '\n' + ("% 5d" % -10))   #" "空白意味着在正数前加上空格
#   10
#  -10
print(("%+5d" % 10) + '\n' + ("%+5d" % -10))   #加号表示不管是正数还是负数都表示出符号
#  +10
#  -10





"""
3.4 字符串方法

"""
import string
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.printable)
print(string.punctuation)


"""
3.4.1 find 
在较长的字符串中查找子字符串，返回子串所在位置的最左端索引，如果没有找到则返回-1
"""
title = "Monty Python's Flying Circus"
title.find('Python')
subject = "$$$ Get rich now!!! $$$"
subject.find("$$$",1)      #20
subject.find("!!!",0,16)   #-1

"""
rfind、index、rindex、count、startwith、endswith
"""



"""
3.4.2 join
split 的逆方法，用来在队列中添加元素
"""
seq = ['1','2','3','4','5']
sep = "+"
print(sep.join(seq))      #'1+2+3+4+5'

dirs = "","usr","bin","env"
print("/".join(dirs))     #'/usr/bin/env'

x = ['1','2','3','4','5']
print("".join(x))         #'12345'



"""
3.4.3 lower
"""
"""
translate
islower、capitalize、swapcase、title、istitle、upper、isupper、capwords
titile: 将所有单词的首字母大写，而其他字母小写
"""



"""
3.4.4  replace
"""
print("This is a test".replace("is","eez"))
print("This is a test".replace("is","eez",1))

"""translate、expandtabs"""



"""
3.4.5  split
join的逆方法，用于将字符串分割成序列
"""
print("1+2+3+4+5".split("+"))
print("11 2 44 578 58".split())    #不提供任何分割符，程序会把所有空格作为分隔符（空格、制表、换行等）

"""join、rsplit、splitlines"""



"""
3.4.6 strip
返回去除两侧（不包括内部）空格的字符串，也可以指定需要去除的字符
"""
print("        12467               ".strip())
print("++++++++++++1222222222++++++++++++++".strip("+"))



"""
3.4.7 translate
和replace方法一样，可以替换字符串中的某些部分，但是和前者不同的是，
translate方法只处理单个字符。它的优势在于可以同时进行多个替换，有些
时候比replace效率高得多
"""
#from string import maketrans   python3中取而代之的是内建函数

table = str.maketrans("cs","kz")
print("this is an incredible test".translate(table))








