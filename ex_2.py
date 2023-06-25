"""
Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly. 
"""
student_choice = input("Enter the choice (y for yes or n or no) : ")
if student_choice == 'y':
    print("medical cause")
elif student_choice == 'n':
    print("Not medical cause")
else :
    print("Invalid Input")
