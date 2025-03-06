#____________________________________________________________________________________
#   Purpose: Skip even numbers
#   Author: Felix       Date: March 3, 2025     Class: ICS3C
#____________________________________________________________________________________

#This if for the user input number
Number = int(input("Enter the number you want me to count to: "))

#This is the for loop
for i in range(1, Number + 1):
    if i % 2 == 1: #This is the remainder operator which does elementary division math | This is also a conditional statement which
        # - which checks if it has a remainder of 1 and then if it is it is able to print
        print(i)