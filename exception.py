

# raise BaseException
# raise BaseException("dwl")
# raise


try:
    pass
except ZeroDivisionError:
    pass
except TypeError:
    pass


try:
    pass
except (ZeroDivisionError,TypeError):
    pass


try:
    #1 / 0
    pass
except (ZeroDivisionError,TypeError) as e:
    print(e)


try:
    pass
except BaseException as e:
    pass


try:
    pass
except BaseException as e:
    pass
else:          #try没有发生异常，else会被执行
    pass


while True:
    try:
        x = input("Enter the first number:")
        y = input("Enter the second number")
        value = int(x) / int(y)
        print('x/y is',value)
    except:       #捕获所有异常
        print('Invalid input.Please try again')
    else:
        break


x = None
try:
    x = 1 / 0
except NameError:
    print("Unknown variable")
else:
    print("That went well")
finally:
    print("Cleaning up...")


class FooBar:
    def __init__(self):
        self.somevar = 42





