import datetime
import json
import re
#from pprint import pprint as pretty_print
#help(json)
'''
lambda x, y : x + y
x = lambda x, y : x + y
print(x(4, 5))
'''
'''
y = lambda x : x
print(y(4))
'''
'''
d = datetime.datetime.now()
#print(d.strftime("%b"))
#pretty_print(d.strftime('%b'))
#convert to json
x = {"JSON":"So what?"}
#convert from json
y = '{"JSON":"So what?"}'

#print(json.dumps(x))
#print(json.loads(y))

txt = "The quick brown fox jumps over the lazy dog"
x = re.search("The",txt)
if x:
    print("Yes we have a match")
else:
    print("Aww, no match")
'''
'''
date = "2004-12-12"
x = re.search("^2\d{4}",date)
'''

#file = input("Enter file name with extension: ")
f = open("demofile.txt", "rt")
#Read first 5 words
#print(f.read(5))
#print(f.readline())
'''
for x in f:
    print(x)
'''
f.close()
