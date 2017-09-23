
#三引号制作文档字符串，每个对象都有一个属性__doc__,这个属性用于描述该对象的作用
class Hello():
    """hello class"""
    def printHello(self):
        """print hello world"""
        print("hello world")

print(Hello.__doc__)
print(Hello.printHello.__doc__)



