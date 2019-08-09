'''
class className:
      def createName(self, name):
            self.name = name

      def displayName(self):
            return self.name

      def saying(self):
            print ("Hello %s" %self.name)

pythonClass = className()
javaClass = className()
pythonClass.createName('Acid')
javaClass.createName('Gyan')
pythonClass.displayName()
javaClass.displayName()
pythonClass.saying()
javaClass.saying()
'''
#Classes and SubClasses
'''
class parentClass:
    var1 = "I am var1"
    var2 = "I am var2"

class childClass(parentClass):
    pass

parentObj1 = parentClass()
print(parentObj1.var1)
print(parentObj1.var2)

childObj1 = childClass()
print(childObj1.var1)
print(childObj1.var2)
'''
'''
class parent:
    var1 = "Bread"
    var2 = "Eggs"

class child(parent):
    var2 = "Sausage"

pob = parent()
cob = child()
print(pob.var2)
print(cob.var2)
'''
'''
#Multiple Parents
class Mom:
    var1 = "Hey i'm mum"

class Dad:
    var2 = "Hey i'm dad"

class child(Mom,Dad):
    var3 = "I'm a son"

childObj = child()
print(childObj.var1)
print(childObj.var2)
print(childObj.var3)
'''
'''
#Constructors
class swine:
    def apples(self):
        print ("Beef pie")

obj = swine()
obj.apples()

class new:
    def __init__(self):
        print ("This is a Constructor")
        print ("This also prints out")

newObj = new()
'''
# Operator Overloading
class A:
    def __init__(self,a):
        self.a = a

    #adding two objects
    def __add__(self, o):
        return self.a + o.a
ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)
