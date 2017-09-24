
#新式的类
class NewStyle(object):
    pass
#老式的类
class OldStyle:
    pass
#python3中没有“旧式”的类，也不需要显示地子类化object或者将元类设置为type
#所有的类都会隐式地成为object的子类----如果没有明确超类的话，就会直接子类化；
#否则会间接子类化



class FooBar:
    def __init__(self,value = 42):   #__del__ : 析构方法，尽力避免使用
        self.somevar = value
f = FooBar()
print(f.somevar)




class Bird:
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print("Aaaah..")
            self.hungry = False
        else:
            print("No,thanks!")
class SongBird(Bird):
    def __init__(self):
        #Bird.__init__(self)                   # 第一种
        super(SongBird,self).__init__()        # 第二种  python3 应该使用super
        #super().__init__()              # 可以简化为
        self.sound = "dwl"
    def sing(self):
        print(self.sound)
sb = SongBird()
sb.sing()
sb.eat()
"""
  在调用一个实例的方法时，该方法的self参数会被自动绑定到实例上，这称为绑定方法。
  但如果直接调用类的方法（比如Bird.__init__），那么就没有实例会被绑定。这样就可以自由地提供需要的self参数。这样的方法称为未绑定方法
  通过将当前的实例作为self参数提供给未绑定方法，SongBird就能够使用其超类构造方法的所有实现，也就是说属性hungry能被设置
"""


"""
 9.3 成员访问
"""
"""
 9.3.1 基本的序列和映射规则
 __len__ 、 __setitem__ 、 __getitem__ 、 __delitem__
"""
def checkIndex(key):
    if not isinstance(key,int):
        raise TypeError
    if key < 0:
        raise IndexError
class ArithmeticSequence:
    def __init__(self,start=0, step=1):
        self.start = start
        self.step = step
        self.changed = {}
    def __getitem__(self, key):
        checkIndex(key)
        try:
            return self.changed[key]
        except KeyError:
            return self.start + key * self.step
    def __setitem__(self, key, value):
        checkIndex(key)
        self.changed[key] = value

s = ArithmeticSequence(1,2)
print(s[4])
s[4] = 2
print(s[4])



"""
 9.3.2 子类化列表，字典和字符串
"""

class CountList(list):
    def __init__(self,*args):
        super(CountList, self).__init__(*args)
        self.counter = 0
    def __getitem__(self, index):
        self.counter += 1
        return super(CountList,self).__getitem__(index)
c1 = CountList(range(10))
print(c1)
print(c1.reverse())
del c1[3:6]
print(c1)
print(c1.counter)
print(c1[4] + c1[2])
print(c1.counter)



"""
9.5 属性
"""
"""
 9.5.1 property
"""

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def setSize(self,size):
        self.width,self.height = size
    def getSize(self):
        return self.width,self.height
    size = property(getSize,setSize)   #创建一个属性 , 四个参数 fget、fset、fdel、doc
    #size = property(fget=getSize,doc="111")  #只读，并有一个文档字符串的属性
r = Rectangle()
r.width = 10
r.height = 5
print(r.size)
r.size = 150,100
print(r.width)


"""
 9.5.2 静态方法和类成员方法
"""
class MyClass:
    @staticmethod
    def smeth():
        print("This is a static method")
    @classmethod
    def cmeth(cls):
        print("This is a class method of",cls)
MyClass.smeth()
MyClass.cmeth()


"""
 9.5.3 __getattr__、__setattr__ 和它的朋友们
"""
class Rectange:
    def __init__(self):
        self.width = 0
        self.height = 0
    def __setattr__(self,name,value):
        if name == 'size':
            self.width,self.height = value
        else:
            self.__dict__[name] = value   #字典里面是所有实例的属性
    def __getattr__(self, name):
        if name == 'size':
            return self.width,self.height
        else:
            raise AttributeError
"""
__getattribute__ 拦截所有特性的访问，也拦截对__dict__的访问，使用超类的__getattribute__
方法（使用super）是唯一安全的途径
"""



"""
 9.6 迭代器
 __iter__
 （对实现__iter__方法的对象进行迭代）
python3: __iter__返回一个迭代器，具有__next__方法
而新的内建函数next可以用于访问这个方法，next(it)等同于3.0之前的it.next()

一个实现了__iter__方法的对象是可迭代的，一个实现了__next__方法的对象则是迭代器
"""
class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        return self.a
    def __iter__(self):
        return self          #返回迭代器本身
fibs = Fibs()
for f in fibs:
    if f > 1000:
        print(f)
        break

"""
内建函数iter可以从可迭代的对象中获取迭代器
"""
it = iter([1,2,3])
print(it.__next__())
print(it.__next__())
print(next(it))        #使用内建函数next
"""
从迭代器得到序列
"""
class TestIterator:
    value = 0
    def __next__(self):
        self.value += 1
        if self.value > 10:
            raise StopIteration
        return self.value
    def __iter__(self):
        return self
ti = TestIterator()
print(list(ti))



"""
 9.7 生成器
 生成器是一种用普通的函数语法定义的迭代器
  返回是一个迭代器
"""
nested = [[1,2],[3,4],[5]]
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element             #任何包含yield语句的函数称为生成器
for num in flatten(nested):          #可通过在生成器上迭代来使用所有的值
    print(num)

print(list(flatten(nested)))

"""
生成器推导式
"""
g = ((i +2) ** 2 for i in range(2,27))     #注意圆括号
print(g.__next__())
print(sum(i ** 2 for i in range(10)))


"""
 9.7.2 递归生成器
"""
def flatten1(nested):
    try:
        try:
            nested + ""              #排除字符串
        except TypeError:
            pass
        else:
            raise TypeError

        for sublist in nested:
            for element in flatten1(sublist):
                yield element
    except TypeError:
        yield nested
print(list(flatten1([[[1],2],3,4,[5,[6,7]],8])))


"""
 9.7.4 生成器方法
"""
def repeater(value):
    while True:
        new = (yield value)
        if new is not None:
            value = new
r = repeater(42)
print(r.__next__())
print(r.send("hello,world!"))



"""
 9.8 八皇后问题
"""
def conflict(state,nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0,nextY - i):
            return True
    return False

def queens(num = 8,state= ()):
    for pos in range(num):
         if not conflict(state,pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num,state + (pos,)):
                    yield (pos,) + result

print(list(queens(8)))









