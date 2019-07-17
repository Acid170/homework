#List of dictionaries
acnt1 = {'last name':'Gyan','first name':'Eliezer','balance':45,'type':'savings'}
acnt2 = {'last name':'Chris','first name':'Joshua','balance':2000,'type':'savings'}
acnt3 = {'last name':'Acquah','first name':'Grace','balance':5000,'type':'investment'}

b_acnts = [acnt1,acnt2,acnt3]
print(b_acnts)

#dictionary of lists
acnt1 = ['Gyan','Eliezer',45,'savings']
acnt2 = ['Chris','Joshua',2000,'savings']
acnt3 = ['Acquah','Grace',5000,'current']

b_acnts = {"0001":acnt1,"0002":acnt2,"0003":acnt3}
print(b_acnts)

# Dictionary of dictionaries
acnt1 = {'last name':'Gyan','first name':'Eliezer','balance':45,'type':'savings'}
acnt2 = {'last name':'Chris','first name':'Joshua','balance':2000,'type':'savings'}
acnt3 = {'last name':'Acquah','first name':'Grace','balance':5000,'type':'investment'}

b_acnts = {"0001":acnt1,"0002":acnt2,"0003":acnt3}
print(b_acnts)
#print(b_acnts["0001"])


#Deposit Function
def deposit (balance , amount_to_deposit):
    return balance+amount_to_deposit

#Withdrawal Function
def withdraw (balance , amount_to_withdraw):
    return balance-amount_to_withdraw

#Implementing the deposit Function
print(deposit(acnt1.get('balance'),500))

#Implementing the withdraw Function
print(withdraw(acnt1.get('balance'),5))
