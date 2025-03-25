#____________________________________________________________________________________
#   Purpose: Have a tuple and then count the amount of things that is the same in there
#   Author: Felix       Date: March 25, 2025     Class: ICS3C    Last Updated:
#____________________________________________________________________________________

Fruits = ('apple', 'banana', 'orange','apple', 'banana', 'orange','apple', 'banana', 'orange','apple', 'banana', 'orange')
#this is the tuple, 4 of each containing only apple orange and banana

#Simple input that will count the fruit you input and print the value
fruit = input('Enter a fruit you want to count (apple orange banana): ')
if fruit in Fruits: #if your input is in fruit if will run this
    NumberOfFruit = Fruits.count(fruit) #this is the variable of the integer of fruits
    TheFruit = fruit.title() #this is what you put in
    print(f"you have {NumberOfFruit} {TheFruit} in total") #we print it


