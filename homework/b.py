import a

print ("Starting B")
print ("Started B")

def hi_from_b():
    print("Hi from B")

if __name__ == "__main__":
    hi_from_b()
    a.hi_from_a()
