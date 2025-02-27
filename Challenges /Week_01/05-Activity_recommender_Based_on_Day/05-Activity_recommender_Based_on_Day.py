#____________________________________________________________________________________
#   Purpose: Activity recomeder for days of the week +
#   Author: Felix       Date: Feb. 25, 2025     Class: ICS3C
#____________________________________________________________________________________
from threading import Thread

#First make the varieble for the if statement
DayOfTheWeek = input("What day of the week is it?: ")
#Import random number maker for the random activity so it isn't always the same
import random
#Make a varieble for each of the days with random numbers so they can check and answer
MondayR = random.randint(1, 2)
TuesdayR = random.randint(1, 2)
WednesdayR = random.randint(1, 2)
ThursdayR = random.randint(1, 2)
FridayR = random.randint(1, 2)
SaturdayR = random.randint(1, 2)
SundayR = random.randint(1, 2)
#In the If it will check if it is 1 or 2 and if it's 1 it will be diffreent form 2

#Now i have the variebles create the conditonals in conditionals
if DayOfTheWeek == "monday":
    #I make it check if mondayR is 1 or 2 and i will od for every other conditional statmenst for the days
    if MondayR == 1:
        print("Do your homework!")
    if MondayR == 2:
        print("Go to the gym!")
elif DayOfTheWeek == "tuesday":
    if TuesdayR == 1:
        print("Go eat out")
    if TuesdayR == 2:
        print("Draw something")
elif DayOfTheWeek == "wednesday":
    if WednesdayR == 1:
        print("Go to the library")
    if WednesdayR == 2:
        print("Play some music")
elif DayOfTheWeek == "thursday":
    if ThursdayR == 1:
        print("Go to the park")
    if ThursdayR == 2:
        print("Play a game")
elif DayOfTheWeek == "friday":
    if FridayR == 1:
        print("Go to the recreational centre")
    if FridayR == 2:
        print("Relax at home")
elif DayOfTheWeek == "saturday":
    if SaturdayR == 1:
        print("Sleep in")
    if SaturdayR == 2:
        print("Hang out with friends")
elif DayOfTheWeek == "sunday":
    if SundayR == 1:
        print("Study for class")
    if SundayR == 2:
        print("Start a party")
else:
    print("You did not enter a valid day rerun the program")

#Now if you type in monday it has a chance to recomend you option 1 or 2 instead of always giving you the same activity
