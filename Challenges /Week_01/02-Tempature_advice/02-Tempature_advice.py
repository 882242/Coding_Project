#____________________________________________________________________________________
#   Purpose: Make the bot say somethign based on the Temp
#   Author: Felix       Date: Feb. 25, 2025     Class: ICS3C
#____________________________________________________________________________________

# Just copied the grading code and changed the conditional numbers and text/Print statments
Temp = int(input("Enter the tempature in Celsius: "))

if Temp >= 30:
    print("It is melting outside, stay home!")
elif Temp >= 15:
    print("It's hot today, leave your sweater behind!")
elif Temp >= 10:
    print("Wear a sweater!")
elif Temp >= 5:
    print("Wear a sweater and a vest!")
else:
    print("Wear a Jacket!")