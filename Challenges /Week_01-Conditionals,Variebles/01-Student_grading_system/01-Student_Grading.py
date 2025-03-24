#____________________________________________________________________________________
#   Purpose: Make a grade score base on the number score
#   Author: Felix       Date: Feb. 25, 2025     Class: ICS3C
#____________________________________________________________________________________

# I already made this grading system so I will not add a psuedocode
# It converts your score into a grade
score = int(input("Enter your test score: "))

if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B!")
elif score >= 70:
    print("You got a C!")
else:
    print("You need to study more")

