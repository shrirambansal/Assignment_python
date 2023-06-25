"""
A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
"""
quantity = int(input("Enter the quantity : "))
amount = quantity * 100
if amount <= 1000 :
    print(amount)
else :
    new_amount = (10 / 100) * amount
    print(amount-new_amount)
