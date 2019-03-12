"""
complicated stuff
"""
import sys

inputnum = input("Enter an integer\n")

#check if inputnum is actually an integer

try:
    savedNum = int(inputnum)
except ValueError:
    print("Oof")
    quit()

if savedNum == 2:
    print("Number is 2")
elif savedNum == 5:
    print("Number is 5")
elif savedNum % 2 == 0:
    print("even steven")
else:
    print("odd todd")
