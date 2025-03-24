#____________________________________________________________________________________
#   Purpose: Create a grocery list that can add, remove, and modify things in an array
#   Author: Felix       Date: March 19, 2025     Class: ICS3C    Last Updated:
#____________________________________________________________________________________

import threading
import time
from os import remove

grocery_list = []
#this is gonna be a loop function while true which always makes sure that you have everything or not
while True:
    print(f"this is your grocery list {grocery_list}!")
    confirm = input("Is this everything you need? (yes/no) ") #the first question is if this is everything yes/no?
    if confirm.strip().lower() == "yes":
        print(grocery_list)
        print("This is all that we need!")
    elif confirm.strip().lower() == "no":
        Operater = input("Would you like to add, remove, or modify? ") #this asks to modify, add, or remove and done
        if Operater.strip().lower() == "add":
            adding = input("What are we adding? : ")
            grocery_list.append(adding) #appening adds to an array
        elif Operater.strip().lower() == "remove":
            removing = input("What are we removing? (precise spelling) : ")
            grocery_list.remove(removing) #remove removes something from the array through precise spelling
        elif Operater.strip().lower() == "modify":
            modifying = input("What are we modifying? (precise spelling) : ")
            if modifying in grocery_list: #this is an advance code i made to modify the index
                index = grocery_list.index(modifying) #this variable is = to the index of the modifying item in the list
                adding2 = input("What are we changing it to? : ") #this is what we are going to change into
                grocery_list[index] = adding2 #then we make the index of the modifying = to adding2 which is gonna change it without moving the index
            else:
                print("item not found") # if it is not found in the list it will print this
        else:
            print("Please choose an action")
            continue