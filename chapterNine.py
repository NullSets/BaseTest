
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





