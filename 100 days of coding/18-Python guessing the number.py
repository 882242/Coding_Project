import random

print("This is a number guessing game!")
#it is not randomized yet
import time
X = random.randint(1, 10000)

while True:
    GuessingNumber = int(input("Guess the number from 1, 10000! "))
    if GuessingNumber < X:
        print("Too low")
        continue
    elif GuessingNumber > X:
        print("Too high")
        continue
    elif GuessingNumber == X:
        time.sleep(1)
        print("You got it right!")
        break