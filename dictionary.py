




"""
4.2.1  dict函数
dict函数根本不是真正的函数，它是个类型，就像list、tuple和str一样
"""
items = [('name','Gumby'),('age',42)]
d = dict(items)
print(d)
print(d['name'])

d = dict(name = 'Gumby',age = 42)
print(d)


"""
4.2.2 基本字典操作
"""
print(len(d))
print(d['name'])
d['name'] = 'dwl'
del d['name']
print('age' in d)    #查的是键

"""
键可以为任何不可变类型
"""




"""
4.2.3 字典的格式化字符串
"""
phonebook = {'Beth':'9102','Alice':'2341','Cecil':'3258'}
print("Cecil's phone number is %(Cecil)s." % phonebook)



"""
4.2.4 字典方法
"""
"""
1.clear
清除字典中所有的项。这个是原地操作（类似于list.sort），所以无返回值（或者说返回None）
"""
d = {"name":"Gumby","age":42}
d.clear()
print(d)



"""
2,copy 
返回一个具有相同键值对的新字典（这个方法实现的是浅复制，因为值本身就是相同的，而不是副本）
"""
x = {'username':'admin','machines':['foot','bar','baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)   #{'username': 'mlh', 'machines': ['foot', 'baz']}
print(x)   #{'username': 'admin', 'machines': ['foot', 'baz']}
#避免这个问题一种方法就是使用深复制，复制其包含所有的值
from copy import deepcopy
d = {}
d['names'] = ['Alfred','Bertrand']
c = d.copy()
dc  = deepcopy(d)
dc['names'].append('Clive')
print(c)       #{'names': ['Alfred', 'Bertrand']}
print(dc)      #{'names': ['Alfred', 'Bertrand', 'Clive']}



"""
3. fromkeys
使用给定的键建立新的字典，每个键默认对应的值为None
"""
print({}.fromkeys(['name','age']))
print(dict.fromkeys(['name','age']))
print(dict.fromkeys(['name','age'],'unknown'))   #使用自己的默认值



"""
4.  get 
使用get访问一个不存在的键时，没有任何异常，而得到了None值
而d['name'] 如果不存在这个键，则会出错
"""
d = {}
#print(d['name'])
print(d.get('name'))
print(d.get('name','N/A'))    #改变不存在时返回的默认值



"""
5.has_key        python3中不存在这个函数，--------->   故使用  k  in   d
"""



"""
6.  items 
items  返回一个所有字典项的迭代器对象 。返回时没有特殊的顺序
"""
d = {'title':'Python',"url":"http://www.python.org",'spam':0}
print(d.items())
print(type(d.items()))
for k,v in d.items():
    print("key = %s, value = %s" % (k,v))


"""
7. keys  和 values
 keys   返回一个针对键迭代器对象  
 values 返回一个针对值迭代器对象  
"""
print(d.keys())
print(d.values())
for k in d.keys():
    print("key = %s" % k)
for v in d.values():
    print("value = %s" % v)




"""
8. pop
  用于获取对应于给定键的值，然后将这个键值对从字典中移除
"""
d = {'x': 1, "y":2}
a = d.pop("x")
print(a)
print(d)



"""
9.  popitem
 类似于list.pop，但不同的是popitem弹出随机的项，因为字典没有”最后的元素“或者有关顺序的概念
 若想一个一个地移除并处理项，这个方法非常有效，因为不用先获取键的列表
"""
d = {'title':'Python Web Site',"url":"http://www.python.org",'spam':0}
a = d.popitem()
print(a)
print(d)



"""
10 setdefault
在某种程度上类似于get方法，就是能够获取给定键相关联的值，除此之外，还能在字典中不含有给定键
的情况下设置相应的键值
"""
d = {}
d.setdefault("name",'N/A')
print(d)
d['name'] = 'Gumby'
d.setdefault('name')
print(d)



"""
11.  update
可以利用一个字典项更新另外个字典
"""
d = {'title':'Python Web Site',"url":"http://www.python.org",'changed':0}
x = {'title':'Python '}
d.update(x)
print(d)


