'''
def add(x,y,z):
    print (x + y + z)
    return x + y + z

def add(x,y):
    print (x + y)
    return x + y

#add(3,2,4)
add(2,3)
'''
'''
class Emp:
    #class attribute
    department = "Python"

    def __init__(self,id,name):
        self.id = id
        self.name = name

    def get_name(self):
        return self.name

    def get_department():
        return Emp.department

emp = Emp(45, "Lele Rice")
emp.get_name
#print(emp.department)
#print(emp.get_department)
'''
'''
class Employee(object):
    emp_count = 0

    def __init__(self,name,salary):
            self.name = name
            self.salary = salary

    def display_count(self):
            print("Total Employees: {}".format(Employee.emp_count))

    def display_employee(self):
            print("Name: {}".format(self.name))

emp = Employee("Van",344)
emp.display_employee()
'''
class Parent(object):
    def parent_method(self):
        print("Parent method")
    def __init__(self,name):
        self.parent_name = name

class Child(Parent):
    child_attribute = "I be 16 years"
    def __init__(self,name):
        self.child.
