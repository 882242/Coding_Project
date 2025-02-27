#____________________________________________________________________________________
#   Purpose: if your old enough to vote the bot will tell you
#   Author: Felix       Date: Feb. 25, 2025     Class: ICS3C    Last Updated: Feb 27
#____________________________________________________________________________________


# Simple input and if statement that is the same as 01 and 02
Age = int(input("Enter your age: "))
#adding randomizer or which party to vote using varieble
import random
Party = random.randint(1,6)

if Age >= 18:
    print("You are eligible to vote!")
    if Party == 1:
        print("Vote for the Liberal Party!")
    if Party == 2:
        print("Vote for the Conservative Party!")
    if Party == 3:
        print("Vote for the New Democratic Party!")
    if Party == 4:
        print("Vote for the Bloc Québécois")
    if Party == 5:
        print("Vote for the Green Party")
    if Party == 6:
        input("Who are you going to vote for?: ")
        print("Nice")
else:
    print("You are not eligible to vote!")