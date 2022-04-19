def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print(add(1, 2))
print(sub(1, 2))
print(mul(1, 2))
print(div(1, 2))

class Cal(object):

    # 생성자 : 메모리에 올라오는 순간 즉시 실행된다.
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


    def mul(self):
        return self.a * self.b


    def div(self):
        return self.a / self.b

# 메모리에 올라온다
cal1 = Cal(1, 2)
cal2 = Cal(3, 4)

print(dir(cal1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'a', 'add', 'b', 'div', 'mul', 'sub'] 
print(cal1.a)   # 1
print(cal1.b)   # 2
print(cal1.add())   # 3

print(cal2.a)   # 3
print(cal2.b)   # 4
print(cal2.add())   # 7
