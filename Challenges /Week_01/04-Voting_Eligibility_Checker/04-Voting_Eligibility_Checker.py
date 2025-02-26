#____________________________________________________________________________________
#   Purpose: if your old enough to vote the bot will tell you
#   Author: Felix       Date: Feb. 25, 2025     Class: ICS3C
#____________________________________________________________________________________


# Simple input and if statement that is the same as 01 and 02
Age = int(input("Enter your age: "))

if Age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")