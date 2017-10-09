
fibs = [0,1]
for i in range(8):
    fibs.append(fibs[-2] + fibs[-1])
print(fibs)


import math
x = 1
y = math.sqrt
print(hasattr(y,"__call__"))     # python3 判断对象是否可调用


def get(x,y):
    return x + y , x - y      #返回多个值
print(get(1,2))


"""
文档字符串
可代替pass + 注释
"""
def square(x):
    """我是文档字符串"""
print(square.__doc__)      #调用文档字符串


help(square)


def test():
    print("This is printed")
    return                      # None
    print("This is not")


def change(n):
    n[0] = "My dwl"
names = ['Mrs, Endtity','Mrs.Thing']
change(names)
print(names)     #发生变化，因为两个变量同时引用了一个列表


"""
6.4.3 关键字参数
"""
def hello(greeting = 'Hello',name = 'world'):
    print("%s,%s" % (greeting,name))
hello()
hello(greeting="my")
hello(name="dwl")
hello(greeting="my",name="dwl")


"""
6.4.4 收集参数
"""
def print_params(*params):
    print(params)
print_params("dwl")         # ('dwl',)

def print_params(title,*params ,**keypar):    #收集为元组、字典
    print(title)
    print(params)
    print(keypar)
print_params("dwl" , 1 , 2 , x = 1 , y = 2 , z = 3 )


"""
6.4.5 反转过程
"""
def add(x ,y):
    return x + y
params  = (1,2)
print(add(*params))

def foo(x,y,z,m=0,n=0):
    print(x,y,z,m,n)
def call_foo(*args,**kwds):
    print("Calling foo!")
    foo(*args,**kwds)

def story(**kwds):
    return "Once upon a time,there was a" \
            "%(job)s called %(name)s" % kwds
def power(x,y,*others):
    if others:
        print("Received redundant parameters:",others)
    return pow(x,y)
def interval(start,stop=None,step=1):
    "Imitates range() for step > 0"
    if stop is None:
        start,stop = 0 ,start
    result = []
    i = start
    while i < stop:
        result.append(i)
        i += step
    return result
print(story(job = "king",name = "Gumby"))
print(story(name = "Sir Robin",job = "brave knight"))
params = {"job":"language","name":"python"}
print(story(**params))
del params['job']
print(story(job = 'stroke of genius',**params))
power(2,3)
power(3,2)
params = (5,) * 2
print(params)
print(power(*params))
print(power(3,3,"hello,world"))
print(interval(10))
print(interval(1,5))
print(interval(3,12,4))
print(power(*interval(3,7)))





"""
6.5 作用域
"""

#“不可见”的字典
x = 1
scope = vars()   #返回这个字典
print(scope['x'])
scope['x'] += 1
print(x)


#这类“不可见字典”叫做命名空间或者作用域


#全局变量
#访问全局变量
def combine(parameter):
    print(parameter + globals()["parameter"])    #全局变量跟局部变量同名，但又想访问全局变量
parameter = 'berry'
combine(parameter)

#重绑定全局变量
x  = 1
def change_global():
    global x          #声明全局变量
    x = x + 1
change_global()
print(x)

#嵌套作用域
def multiplier(factor):
    def multiplyByFactor(number):
        return number * factor
    return multiplyByFactor
double  = multiplier(2)
print(double(5))
triple = multiplier(3)
print(triple(3))
print(multiplier(5)(4))

# python3  nonlocal关键字 可以让用户对外部作用域（但并非全局作用域）的
# 变量进行赋值



def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)

#二分查找
def search(sequence,number,lower,upper):
    if lower == upper:
        assert( number == sequence[upper])
        return upper
    else:
        middle = (lower + upper ) // 2
        if number > sequence[middle]:
            return search(sequence,number,middle + 1,upper)
        else:
            return search(sequence,number,lower,middle)

#使用标准库实现二分查找
import bisect


#函数型编程
import functools
#map
print(list(map(str,range(10))))

#filter
def func(x):
    return x.isalnum()  #如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
seq = ["foot",'x41','?!','***']
print(list(filter(func,seq)))
print([x for x in seq if x.isalnum()])
print(list(filter(lambda x:x.isalnum(),seq)))

#reduce
numbers = [72,101,108,108,111,44,32,119,111,114,108,100,33]
print(functools.reduce(lambda x,y:x+y,numbers))
print(sum(numbers))















