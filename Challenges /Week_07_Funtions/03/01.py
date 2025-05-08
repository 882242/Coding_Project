#____________________________________________________________________________________
#   Purpose: timer
#   Author: Felix       Date: April 30, 2025     Class: ICS3C    Last Updated:
#____________________________________________________________________________________

from tkinter import *

window = Tk()
window.geometry("300x300")

Input_SECONDS = Entry(window, width=10)
Input_SECONDS.pack()

Timer_GPHIC = Label(window, text='0000')
Timer_GPHIC.pack()

def update_timer(remaining_seconds):
    if remaining_seconds >= 0:
        Timer_GPHIC.config(text=str(remaining_seconds))
        if remaining_seconds > 0:
            window.after(1000, update_timer, remaining_seconds - 1)
        else:
            window.destroy()

def start_timer(seconds):
    try:
        seconds1 = int(seconds)
        update_timer(seconds1)
    except ValueError:
        Timer_GPHIC.config(text="Error")

StartButton = Button(window, text="Start", command=lambda: start_timer(Input_SECONDS.get()))
StartButton.pack()

window.mainloop()
