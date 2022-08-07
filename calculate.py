
Amt=int(input("enter the ammount: "))
pm=input("payment method(credit,cash,upi):")

if Amt>1000:
    Amt -= Amt * .03
if pm == 'credit':
    Amt -= 100
    Amt += Amt * .18
print('your final ammount is :' ,Amt)