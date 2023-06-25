"""
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.
"""
year = int(input("Enter the year of service : "))
salary = int(input("Enter the Salary : "))
if year > 5:
    new_amount = (5 / 100) * salary
    print(salary + new_amount)
