"""

第五章  条件、循环和其他语句


"""



# 取别名
import math as foobar
from time import sleep as sl



"""
5.2 赋值魔法
"""
"""
5.2.1 序列解包
"""
x,y,z = 1,2,3
print(x,y,z)

x , y = y ,x
print(x,y,z)

values = 1,2,3
print(values)
x,y,z = values
print(x)

s = {"name":"robom","girlfriend":"marion"}
key,value = s.popitem()
print(key)
print(value)

"""
5.2.2 链式赋值
"""

m = n = 1
# x = y = somefunction()
#等价于
# y = somefunction()
# x = y


"""
5.2.3 增量赋值
"""
n += 1




"""
5.4 条件和条件语句
 假 : False   None  0  ""   ()  []  {}
 其他一切为真
"""



print(True + False + 52)   # 53


# bool 函数
print(bool(42))  # True


#  is  : 判断两个对象是否是同一对象
#  is not
x = y = [1,2,3]
z =  [1,2,3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)


print(0 < 1 < 100)


print("alpha" < "beta")
print("FnOrd".lower() == "Fnord".lower() )
print([1,2]<[2,1])
print([2,[1,4]]<[2,[1,5]])


#name = input("Please enter your name:") or "<unknown>"

# 三元运算
# a if b else c
a = 1
c = 2
print(a if a > c else c)


"""
5.4.7 断言
 assert
"""
age = -10
assert( 0 <age < 100 , "The age must be realistic")


# name = ""
# while not name or name.isspace():
#     name = input("enter your name:")


for x in range(10):
    print(x)
print(range(0,10))


"""
5.5.4 一些迭代工具

"""

"""
1.并行迭代
zip : 可以作用于任意多序列，应付不等长的序列时，最短的用完的时候就会停止
"""
names = ['anne','beth','george','damon']
ages = [12,45,32,102]
print(zip(names,ages))
for name,age in zip(names,ages):
    print(name,"is",age,"years old")

"""
2. 编号迭代

"""
strings = ["111",'2222']
for index ,string in enumerate(strings):
    if "11" in string:
        strings[index] = "censored"


"""
3 . 翻转和排序迭代
"""
print(sorted([4,3,6,8,3]))
print(sorted("hello,world!"))
print(list(reversed("hello,world!")))
print("".join(reversed("hello,world!")))



"""
5.5.6 循环中的else子句
"""
from math import sqrt
for n in range(98,81,-1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
else:
    print("Didn't find it")




"""
 5 .6 列表推导式 --- 轻量式循环
 利用其他列表创建新列表的一种方法
"""
print([ x * x for x in range(10)])
print([ x * x for x in range(10) if x % 3 == 0])

print([(x,y) for x in range(3) for y in range(3)])
girls = ['alice','bernice','clarice']
boys = ['chris','arnold','bob']
#print([ b + "+" + g for b in boys for g in girls if b[0] == g[0]])
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0],[]).append(girl)
print([b + " + " + g for b in boys for g in letterGirls[b[0]]])



"""
5.7  pass 、del 和exec  eval
"""
a = [1,3,5]
a[:] = []
a = None

x = 1
del x   #移除一个对象的引用，也会移除那个名字本身

x = ['Hello','world']
y = x
del x
print(y)


#动态地创建python代码   exec
#执行Python程序相同的方式来执行字符串
exec("print('hello world')")
#注意作用域

# eval : 对写在字符串中的表达式进行计算并且返回结果
scope = {}
scope['x'] = 2
scope['y'] = 3
eval(" x * y",scope)











print(chr(12))
print(ord("1"))












