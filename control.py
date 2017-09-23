
#Python 中没有switch 语句

#第一种,可以通过字典实现switch语句的功能
x = 1
y = 2
operator = "/"
result = {
    "+": x + y,
    "-": x - y,
    "*": x * y,
    "/": x / y
}
print(result.get(operator))

#第二种，创建switch类，不推荐




"""
for 循环
for ... in ...:
    ....
else:            #可省略，最后步循环结束后将执行else子句
    ....

"""

