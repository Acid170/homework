#import datetime
'''
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
'''
'''
x = datetime.datetime(1995, 7 , 2)
print(x)
print(x.strftime("%A"))
'''
#JSON
#import json
'''
#from JSON to python
#some JSON
x = '{"name":"Gyan", "age":"30", "city":"Tema"}'

#parse x:
y = json.loads(x)

#the result is a python dictionary
print(y["city"])
'''
#from python JSON
#a python object (dict)
'''
x = {
        "name":"Gyan",
        "age" : 30,
        "city":"Tema"
}

#convert into JSOn
y = json.dumps(x)

#the result is a JSON string
print(y)
'''

#Converting python objects into JSON
import json

print(json.dumps({"name":"Gyan","age":"30"})) #dictionary
print(json.dumps(["apple","banana"])) #list
print(json.dumps(("apple", "banana")))  #tuple
print(json.dumps("Eliezer")) #string
print(json.dumps(38)) #int
print(json.dumps(31.54))  #float
print(json.dumps(True)) #boolean
print(json.dumps(False)) #boolean
print(json.dumps(None)) #None
