from idlelib import window
from itertools import count
from tkinter import *
import time

'''count = 0
def click():
    global count
    count = count + 1
    label.config(text=count)



window = Tk()
window.geometry("1200x700")

label = Label(window, text=count)
label.pack()

button = Button(window, text="Click Me")
button.config(command=click)
button.pack()


window.resizable(width=False, height=False)
window.mainloop()
'''

text = 'hi'
def click():
    global text
    text = 'bye'
    label1.config(text=text)

window = Tk()

label1 = Label(window, text=text)
label1.pack()

button = Button(window, text="Click Me", command=click)
button.pack()

window.mainloop()