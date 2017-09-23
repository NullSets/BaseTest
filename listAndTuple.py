
"""
Python 包含6种内建的序列：列表、元祖、字符串、Unicode字符串、buffer对象和xrange对象
列表可变，远组和字符串不可变

python3 现在字符串只有str一种类型，但它跟2.x版本的unicode几乎一样。
xrange() 改名为range()，要想使用range()获得一个list，必须显式调用
"""


"""
索引
"""
greeting = "hello"
print(greeting[0])
print(greeting[-1])
print("hello"[1])

#例子
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
endings = ["st","nd","rd"] + 17 * ["th"] \
    + ["st","nd","rd"] + 7 * ["th"] \
    + ['st']
# year = input("Year: ")
# month = input("Month(1-12) ")
# day = input("Day(1-31) ")
# month_number = int(month)
# day_number = int(day)
# month_name = months[month_number - 1]
# oridinal = day + endings[day_number -1]
# print(month_name ,oridinal,year)



"""
切片
"""
url = "http://www.python.org"
print(url[0:2])        #第二个不包含在切片内
print(url[11:-4])      #需最左边的索引比它右边的索引早出现，否则返回空序列
print(url[:6:-2])



"""
序列相加
"""
print([1,2,3] + [4,5,6])



"""
乘法
"""
print("python" * 5)
print([None] * 10)  #长度为10的列表
#例子
sentence = "He's a very naugthy boy!"
screen_width = 80
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)  // 2
print()
print(" " * left_margin + "+" + "-" * (box_width -2 ) + "+")
print(" " * left_margin + "|  " + " " *   text_width   + "  |")
print(" " * left_margin + "|  " +         sentence     + "  |")
print(" " * left_margin + "|  " + " " *    text_width  + "  |")
print(" " * left_margin + "+" + "-" * (box_width -2 )+ "+")
print()



"""
成员资格：in
"""
permissions = "rwertuii"
print("wer" in permissions)   # True
print("x" in permissions)     # False
users = ["mln","foo","bar"]
print(["foo"] in users)       #True



"""
长度、最小值和最大值
"""
print(len(permissions))
print(max(users))
print(min(users))
print(max(2,3))
print(min(9,3,2,5))




"""
2.3 列表：Python的“苦力”
"""
"""
2.3.1 list函数:适用于所有类型的序列，而不只是字符串
并不是真正的函数，而是一种类型  print(type(list))
"""
print(list("hello"))  # ['h','e','l','l','o']
print("".join(['h','e','l','l','o']))    #将一个由字符组成的列表转换为字符串


"""
2.3.2 基本列表操作
"""
x = [1,1,1]
x[1] = 2    #元素赋值
print(x)

names = ['Alice','Beth','Cecil','Dee-Dee','Earl']
del names[2]  #删除元素
del names[1:3]
print(names)
"""
分片赋值
"""
name = list('Perl')
print(name)
name[2:] = list('ar')  #分片赋值
print(name)

name = list('Perl')
name[1:] = list('ython')  #不等长赋值
print(name)

numbers = [1,5]
numbers[1:1] = [2,3,4]   #在不替换任何原有元素的情况下插入新的元素
print(numbers)   #[1,2,3,4,5]

numbers[1:4] = []   #删除元素
print(numbers)   #[1,5]


"""
2.3.3 列表方法
直接修改原来的列表：append、extend、insert、pop、remove、reverse、sort
pop方法是唯一一个既能修改列表又返回元素值（除了None）的列表方法
"""
lst = [1,2,3]
lst.append(4)  #往列表末尾追加新的对象 ,直接修改原来的列表

x = [1,1,1,2,[4,5]]
x.count(1)  #统计某个元素在列表中出现的次数

a = [1,2,3]
b = [4,5,6]
a.extend(b)  #在列表的末尾一次性追加另一个序列中的多个值, 直接修改原来的列表
print(a)

# 使用连接操作
a = [1,2,3]
b = [4,5,6]
print(a + b)  # 返回的是一个全新的列表
#print(id(a))

a = a + b   #效率比extend低，且并不会修改原来的列表
print(a)
#print(id(a))

#使用分片
a = [1,2,3]
b = [4,5,6]
a[len(a):] = b
print(a)

knights = ['We','are','the','knights','who','say','ni']
knights.index('who')  #返回某个值第一个匹配项的索引位置

numbers = [1,2,3,5,6,7]
numbers.insert(3,'four')  #插入
numbers = [1,2,3,5,6,7]
numbers[3:3] = ['four']  #利用分片插入

#pop方法是唯一一个既能修改列表又返回元素值（除了None）的列表方法
x = [1,2,3]
y = x.pop()  #移除列表中的一个元素（默认最后一个），并且返回该元素的值
print(y)
print(x.pop(0))
#可利用append和pop 实现先进先出的队列

x = ['to','be','or','not','to','be']
x.remove('be')     #移除列表中某个值得第一个匹配项

x = [1,2,3]
x.reverse()  #将列表中的元素反向存放
print(x)

x = [4,6,2,1,7,9]
x.sort()   #在原位置对列表进行排序，即修改了原列表
print(x)
#排序但不修改原列表
x = [4,6,2,1,7,9]
y = x[:]
y.sort()
#另一种获取已排序的列表副本的方法是用sorted函数
x =[4,6,2,1,7,9]
y = sorted(x)  #该函数可以用于所有序列，却总是返回一个列表。（该函数可以用于任何可迭代的对象）
print(list(reversed([9,2,1])))   #另类达到降序目的


#Python默认升序排序
#python3 中sort sorted 取消了对cmp的支持
x =[4,6,2,1,7,9]
x.sort(reverse=True)    #降序
print(x)
x = ['aardvark','abalone','acme','add','aerate']
x.sort(key=len)      #根据长度来排序
print(x)
x = [4,6,2,1,7,9]
a = x[:]
a.sort()
a.reverse()      #另类达到降序目的
print(a)
x.sort()
print(x[::-1])    #另类达到降序目的






"""
2.4 元组：不可变序列      (字符串也是)
"""
x = 1,2,3
print(x)
print((1,2,3))
print(())    #空元组
print((1,))  #一个值的元组，逗号很重要
x = 42,      #一个值的元组，逗号很重要
print(x)

"""
2.4.1 tuple函数      
并不是真正的函数，而是一种类型   print(type(tuple))
"""
#以一个序列作为参数并把它转换为元组
print(tuple([1,2,3]))
print(tuple('abc'))
print(tuple((1,2,3)))  #原样返回



"""
 2.4.2 基本元组操作
"""
x = 1,2,3
print(x[1])
print(x[0:2])
print(x.index(1))
print(x.count(1))





