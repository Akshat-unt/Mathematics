import math
import pyautogui
import os
import sys #provides information about constants, functions and methods

while True:
        a = int(input("Enter first number:\n"))
        b = int(input("Enter second number:\n"))

        maxNum = max(a, b)

        while(True):
                if(maxNum%a==0 and maxNum%b == 0):
                        break
                maxNum = maxNum + 1

        print(f"The LCM of {a} and {b} is {maxNum}")
pyautogui.PAUSE = 6   