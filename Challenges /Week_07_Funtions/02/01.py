#____________________________________________________________________________________
#   Purpose: Caculaotr app
#   Author: Felix       Date: April 29, 2025     Class: ICS3C    Last Updated:
#____________________________________________________________________________________

from tkinter import *

window = Tk()
#this is the window, kinda creates the window
window.geometry('225x200')
#this makes it pop out as 225x200, so a small rectangle
Answer = Entry(window) #this is the entry or where we can see the line
Answer.config(width=55) #this configs the width
Answer.place(x=1, y=0) #this places it at where ever x and y is

#this is the add number function to add in the numbers
def addNumber(NumberButton):
    Current_Value = Answer.get()
    GotNumber = NumberButton.cget('text')
    Answer.delete(0, END) #I made it delete the current and add it back plus the new number to reverse it
    Answer.insert(0, Current_Value + GotNumber)

#This is the operator which if it clicks a operator it will do the corrisponging thing
def operator(OperatorButton):
    GotOperator = OperatorButton.cget('text')
    Current_Value = Answer.get()
    if GotOperator == '+':
        Answer.delete(0, END)
        Answer.insert(0, Current_Value + GotOperator)
    if GotOperator == '-':
        Answer.delete(0, END)
        Answer.insert(0, Current_Value + GotOperator)
    if GotOperator == 'x':
        Answer.delete(0, END)
        Answer.insert(0, Current_Value + '*')
    if GotOperator == '÷':
        Answer.delete(0, END)
        Answer.insert(0, Current_Value + '/')

#this is the equal where you get the asnwer
def Equal():
    AnswerAnswer = Answer.get()
    result = str(eval(AnswerAnswer)) #I had the code evaluate the answer
    Answer.delete(0, END) #Then delete and repaste
    Answer.insert(0, result)

#this clears the entry or answer from the chosen index to END
def Clear():
    Answer.delete(0, END)







#these are all the buttons, where i made them into what look clean and stuff
but1 = Button(window, text="1", height=2, width=2, command=lambda: addNumber(but1)) #I asked ai for the lamba since u need it to have function brackets for some reason
but1.place(x=5, y=35)

but2 = Button(window, text="2", height=2, width=2, command=lambda: addNumber(but2))
but2.place(x=55, y=35)

but3 = Button(window, text="3", height=2, width=2, command=lambda: addNumber(but3))
but3.place(x=105, y=35)

but4 = Button(window, text="4", height=2, width=2, command=lambda: addNumber(but4))
but4.place(x=5, y=75)

but5 = Button(window, text="5", height=2, width=2, command=lambda: addNumber(but5))
but5.place(x=55, y=75)

but6 = Button(window, text="6", height=2, width=2, command=lambda: addNumber(but6))
but6.place(x=105, y=75)

but7 = Button(window, text="7", height=2, width=2, command=lambda: addNumber(but7))
but7.place(x=5, y=115)

but8 = Button(window, text="8", height=2, width=2, command=lambda: addNumber(but8))
but8.place(x=55, y=115)

but9 = Button(window, text="9", height=2, width=2, command=lambda: addNumber(but9))
but9.place(x=105, y=115)

but0 = Button(window, text="0", height=2, width=2, command=lambda: addNumber(but0))
but0.place(x=55, y=155)

butX = Button(window, text="x", height=2, width=2, command=lambda: operator(butX))
butX.place(x=165, y=35)

but_Divide = Button(window, text="÷", height=2, width=2, command=lambda: operator(but_Divide))
but_Divide.place(x=165, y=75)

but_add = Button(window, text="+", height=2, width=2, command=lambda: operator(but_add))
but_add.place(x=165, y=115)

but_sub = Button(window, text="-", height=2, width=2, command=lambda: operator(but_sub))
but_sub.place(x=165, y=155)

but_equal = Button(window, text="=", height=2, width=2, command=Equal)
but_equal.place(x=105, y=155)

but_clear = Button(window, text="clear", height=2, width=2, command=Clear)
but_clear.place(x=5, y=155)

#mainloop is where it activates it pretty much or bring it to life
window.mainloop()