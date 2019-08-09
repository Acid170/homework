#import mymodule as mx
#import platform
from mymodule import person
'''
mytuple = ("apple", "banana", "mango")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
'''
'''
acid = "ELiezer"
myit = iter(acid)
print(next(myit))
print(next(myit))
for x in acid:
    print (x)
'''
'''
class MyNumbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 2
            return x
        else:
            raise StopIteration

myClass = MyNumbers()
myiter = iter(myClass)

for x in myiter:
    print(x)
'''
'''
mymodule.greeting("Eliezer")

a = mymodule.person["age"]
print (a)

b = mymodule.person["name"]
print (b)

c = mymodule.person["country"]
print (c)
'''
'''
d = mx.food
print (d)
'''
'''
x = platform.system()
print(x)
'''
'''
y = dir(platform)
print(y)
'''
print(person["age"])
