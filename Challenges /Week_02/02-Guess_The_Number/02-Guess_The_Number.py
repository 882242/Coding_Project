#____________________________________________________________________________________
#   Purpose: Guess the number game
#   Author: Felix       Date: March 3, 2025     Class: ICS3C
#____________________________________________________________________________________
import random
Number = random.randint(1, 100) # This is our number which is randomized which will generate from the random library
# We will create a variable for the guessed number in a while true loop so it can keep looping to the quesiton
while True:
    GuessingNumber = int(input("Guess the number: ")) # This is the guessing number or our user
    #The next amount of codes are conditional statements and will tell the user if it's too low or high
    if GuessingNumber < Number: #This is for the # if it is too low
        print("Too low")
        continue #This operator is here to bring us back to the loop so we can guess again
    elif GuessingNumber > Number: #This is for the # if it is too high
        print("Too high")
        continue
    elif GuessingNumber == Number: #And this is for the number if it is correct
        print("You got it right!")
        break # This operator is here so when we guess it write the loop breaks
