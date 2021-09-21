print("Program to get the type of lines in pair of linear equations in two variables")
print()
print()
print("copyright by ©Akshat")
print()

import math
print("enter the value of a1,a2,b1,b2,c1,c2")
print()
print("Example to help you out: 2x^2+x+8 and 6x^2+12x+16")
print("here a1=2/a2=6/b1=4/b2=12/c1=8/c2=24")
print("the lines are coincident")
print()
print()
a1=int(input("Enter the value of a1: "))
a2=int(input("Enter the value of a2: "))
b1=int(input("Enter the value of b1: "))
b2=int(input("Enter the value of b2: "))
c1=int(input("Enter the value of c1: "))
c2=int(input("Enter the value of c2: ")) 

condition1=a1/a2
condition2=b1/b2
condition3=c1/c2
print("a1/a2,b1/b2,c1/c2", condition1,condition2,condition3)

if (condition1 != condition2):
    print("Since The equation has 1 zero. Thus, The lines are intersecting")

elif (condition1 == condition2 != condition3):
    print("Since the equation has no zero. Thus, The lines are parallel")

elif (condition1 == condition2 == condition3):
    print("Since the equation has infinite number of zeroes. Thus, The lines are coincidental")  
      
  

