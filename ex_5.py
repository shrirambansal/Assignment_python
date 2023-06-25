"""
Take input of age of 3 people by user and determine oldest and youngest among them. 
"""
age_1 = int(input("Enter the age 1 : "))
age_2 = int(input("Enter the age 2 : "))
age_3 = int(input("Enter the age 3 : "))
if (age_1 > age_2 and age_1 > age_3) :
    print("Oldest is ", age_1)
elif (age_2 > age_1 and age_2 > age_3):
    print("Oldest is ", age_2)
else :
    print("Oldest is ", age_3)

if (age_1 < age_2 and age_1  <age_3) :
    print("Youngest is ", age_1)
elif (age_2 < age_1 and age_2 < age_3):
    print("Youngest is ", age_2)
else :
    print("Youngest is ", age_3)
