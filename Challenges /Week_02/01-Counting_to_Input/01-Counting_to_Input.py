#____________________________________________________________________________________
#   Purpose: Make a counter to the max of the uesr input
#   Author: Felix       Date: March 3, 2025     Class: ICS3C
#____________________________________________________________________________________

#Making a varieable for the user's input number
Number = int(input("Enter the number you want me to count to: "))


#Using the For loop, it will create a loop that prints from 1 to the number once
#We will use + 1 on the vareiable because the system counts the number as the max and the print statement
# - can't go beyond the number
for i in range(1, Number + 1):
    print(i)
    #i is the variable for all the numbers or the index of numbers
#a