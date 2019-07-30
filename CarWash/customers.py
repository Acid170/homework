#Taking Customer Details
class customer:
        def take_details(self):
# Attributes
            l1 = []
            print("Please fill the car washing forms:")
            self.first_name = input("First Name:")
            l1.append(self.first_name)
            self.last_name = input("Last Name:")
            l1.append(self.last_name)
            self.phone_number = input("Phone Number:")
            l1.append(self.phone_number)
            self.email = input("Email:")
            l1.append(self.email)
            self.twitter_handle = input("Twitter Handle:")
            l1.append(self.twitter_handle)
            self.car_model = input("Car Model:")
            l1.append(self.car_model)
            self.car_number = input("Car Number:")
            l1.append(self.car_number)
            return l1









#kwasi.take_details()

'''
customer_details = take_details()
print(customer_details)
'''
'''        customer_details = take_details()
        print(customer_details)

print("Please Confirm details\n")
confirm = input("Press 's' to save or 'x' to discard")
if confirm == 'x':
    exit()
elif confirm == 's':
    print("Data saved")
'''
