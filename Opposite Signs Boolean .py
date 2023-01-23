#Camrenn Wallace-Rivera
#This program defines a Boolean function opposites that takes
#two integers as parameters and returns True if they have opposite signs,
#False otherwise.

num1=int(input("enter number 1:  "))
num2=int(input("enter number 2:  "))
if num1 >= 0 and num2 >= 0:
    print('false')
elif num1 < 0 and num2 < 0:
    print('false')
elif num1 < 0 and num2 >= 0:
    print('true')
else:
    print('false')
