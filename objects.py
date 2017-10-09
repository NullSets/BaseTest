
print("abc".count('a'))

from random import choice
x = choice(['Hello,world',[1,2,'e',4,5]])
print(x)
print(x.count('e'))

def add(x,y):
    return x + y

from operator import add
print(add(1,2))

def length_message(x):
    print("The length of",repr(x),"is",len(x))
length_message("Fnord")
length_message([1,2,3])



"""
7.2 类和类型
"""

class Person:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name
    def greet(self):
        print("Hello,world! I'm %s" % self.name)

foo = Person()
foo.setName("dwl")
foo.greet()
Person.greet(foo)   # foo.greet()可以看作Person.greet(foo)方便的简写


class Secretive:
    def __inaccessible(self):    #私有方法，双下划线
        print("Bet you can't see me..")
    def _inaccessible1(self):  # 单下划线，虽然能访问，但希望将其视为私有
        print("Bet you can't see me..")
    def accessible(self):
        print("The secret message is:")
        self.__inaccessible()
s = Secretive()
s.accessible()
s._Secretive__inaccessible()     #仍能在外部访问私有方法



class MemberCounter:
    members = 0
    def init(self):
        self.members += 1
        print(self.members)
    def init1(self):
        MemberCounter.members += 1
        print(MemberCounter.members)
m1 = MemberCounter()
m1.init()
m1.init1()
print(MemberCounter.members)


class Filter:
    def init(self):
        self.blocked = []
    def filter(self,sequence):
        return [x for x in sequence if x not in self.blocked]
class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']
f  = Filter()
f.init()
print(f.filter([1,2,3]))
s = SPAMFilter()
s.init()
print(s.filter(['SPAM',1,2,34]))



"""
一个类是否是另一个的子类 
"""
print(issubclass(SPAMFilter,Filter))
print(issubclass(Filter,SPAMFilter))
print(SPAMFilter.__bases__)   #已知类的基类
print(Filter.__bases__)
"""
一个对象是否是一个类的实例 
"""
s = SPAMFilter()
print(isinstance(s,SPAMFilter))
print(isinstance(s,Filter))
print(s.__class__)    #如果想知道一个对象属于哪个类
print(type(s))
"""
是否存在
"""
print(hasattr(s,"__class__"))
#是否可调用
print(hasattr(getattr(s,'init',None),'__call__'))
# getattr对应的是setattr，用来设置对象的特性
setattr(s,'name','dwl')
print(s.name)
print(s.__dict__)  #查看对象内所有存储的值










