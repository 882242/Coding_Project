#____________________________________________________________________________________
#   Purpose: Create a set and freeze it, then confirm it is frozen by trying to modify it
#   Author: Felix       Date: April 29, 2025     Class: ICS3C    Last Updated:
#____________________________________________________________________________________

from tkinter import *
import random

window = Tk()

def greet(name1):
    print(f"Hello {name1}")
    greet1 = ['hello', 'hi', 'wsg', 'howdy']
    greetrandom = random.choice(greet1)
    Nameplace.config(text=f"{greetrandom} {name1}")

def submit():
    GetName = entry.get()
    greet(GetName)


window.geometry("700x200")
window.title("Name greeter")
entry = Entry(window)

GetNameButton = Button(window, text="Get Name", command=submit)
GetNameButton.place(x=350, y=2)

Name = Label(window, text="Name: ")
Name.place(x=200, y=2)

Nameplace = Label(window, text=" ")
Nameplace.place(x=300, y=40)

entry.pack()
window.mainloop()


