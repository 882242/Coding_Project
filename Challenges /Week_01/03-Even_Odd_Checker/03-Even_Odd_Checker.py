#____________________________________________________________________________________
#   Purpose: Make the bot idetify if the number is even or odd
#   Author: Felix       Date: Feb. 25, 2025     Class: ICS3C
#____________________________________________________________________________________


# make a varieble for the number input
NumberChecker = int(input("Enter a number: "))

#make it check if it is divisiable by 2 etc
if NumberChecker % 2 == 0:
    print("The number is even!")
else:
    print("The number is odd!")

#The % is an operator that divides the input by the set number
#The % operator also leaves behind remainders, so the % operator sees it as somewhat an elemantary school math
#If the remainder is 0 it would make it even, if it is not then it will be odd
#Then we put the conditional statements in