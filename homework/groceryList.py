#!/usr/bin/env python

def groceryList():
    myList = []
    menuItem = None
    userinputItem = None
    while (menuItem != ":d"):
        menuItem = input("(:a)dd (:v)iew (:d)one: ")
        if (menuItem == ":a"):
            print("(enter) to move to next line (:c)ancel")
            while (userinputItem != ":c"):
                userinputItem = input()
                myList.append(userinputItem)
                if (userinputItem == ":c"):
                    myList.pop()
                    break
        if (menuItem == ":v"):
            print(myList)
        if (menuItem) == ":d":
            exit()

groceryList()
