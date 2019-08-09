'''
def take_list():
    numbers = []
    user_input = []
    while(user_input != "s"):
            user_input = input("Add a number: ")
            print("Enter 's' to save list")
            numbers.append(user_input)
    numbers.pop()
    print(numbers)
#take_list()
'''

def minimum_values(my_list):
    least_values = []
    first_least = min(my_list)
    second_least = [0]
    least_values.append(first_least)
    my_list.remove(first_least)
    second_least = min(my_list)
    least_values.append(second_least)
    print(least_values)

my_list = [1,34,-56,12]
minimum_values(my_list)
