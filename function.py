
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




















