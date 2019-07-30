from customers import customer
from datetime import datetime

kwasi = customer()

def attendant_record():
    car_washing_date = datetime.now()
    attendant_list = []
    attendant_list.append(kwasi.take_details())
    attendant_list.append(car_washing_date)

    return attendant_list

save = attendant_record()
print(save)
