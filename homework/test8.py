#Still on JSON
import json

x = {
        "name":"Gyan",
        "age" : "100",
        "married": False,
        "divorced" : False,
        "children" : ("Eliezer","Grace"),
        "pets"     : None,
        "cars"     : [
        {"model":"BMW 230", "mpg":27.5},
        {"model":"Ford Edge", "mpg":24.1}
        ]
}

# use four indents to make it easier to read the result:
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
# sort the result alphabetically by keys:
print(json.dumps(x, indent = 4, sort_keys = True, separators = (".","=")))


#A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
    print("Yes we have a match")
else:
    print("Aww, no match")


#Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", "9", txt)

print (x)

'''
old_id = "10342324"
new_id = input("Please Enter new ID:")
str = "Change Student with ID number" + old_id + "to" + new_id
x = re.sub("^10", new_id, str)

print (str)
'''
