"""
A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not. 
"""
total_class = int(input("Enter the total class held : "))
attand_class = int(input("Enter the attanded class : "))
percent = (attand_class / total_class) * 100
if percent > 75 :
    print(percent)
    print("Yes, is allowed to sit in exam")
else :
    print(percent)
    print("No, is not allowed to sit in exam")
