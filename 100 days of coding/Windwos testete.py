from tkinter import *

#window = Tk()

#widgets = Gui elements: buttons, Textboxes, labels, images
#windwos = Serves as a container to hold or contain these widgets

#window.geometry("1200x700")
#window.title("Windwos Testete")
#for photos Icon = PhotoImage(file='Imagename.png')
#+
#window.iconphoto(True,Icon)

#window.configure(bg="red")  #bg is a short for background

#label = Label(window, text="Hello World!", bg="black", fg="Blue") #You can also use font, relief + bd for border, padx + pady for space
# You can add photo by image, and use compound BOTTOM TOP RIGHT LEFT for the position of the photo

#label.pack()
#label.place(x=100, y=100)
#first recognize the window, then have a text, bg, and fg. (foreground)

#photos
#photo = PhotoImage(file='FileLocation')

#buttons
#button = Button(window,text='click me',command=)
#You can also add the command by using Button.config(command='the command')
#the additional config of activebackground lets you change the colour of the button when it is pressed
#config lets you config things using the command
#You can use state to disable the status of the button ex: config(state=DISABLED)
#button.pack()


#User inputs
#entry = Entry()
#entry.pack()
#You can use config(show='*') to hide the characters like a password
#The submimt function

#def submit():
#username = entry.get()
#print(username)

#def delete():
#username = entry.delete(0,END) Delete the line of text

#def backspace():
#username = entry.delete(entry.get())-1,END) Delete the last character
#window.mainloop()

#progress bar
#For progress bar the script is { bar = Progressbar(window,orient=HORIZONTAL)
#       bar.pack(pady=10) }
# To access the bar's value the code is { bar['value'} }
#to have to bar value actually look like it is updating we need to use { window.update_idletasks() }
import tkinter as tk

def click(char):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + char)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=30, font=('Arial', 18), borderwidth=3, relief="ridge", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
    ('=', 5, 0, 4)
]

for (text, row, col, colspan) in [b if len(b) == 4 else (*b, 1) for b in buttons]:
    action = lambda x=text: click(x)
    if text == 'C':
        action = clear
    elif text == '=':
        action = calculate
    tk.Button(root, text=text, width=10, height=2, font=('Arial', 14),
              command=action).grid(row=row, column=col, columnspan=colspan, padx=5, pady=5)

root.mainloop()
