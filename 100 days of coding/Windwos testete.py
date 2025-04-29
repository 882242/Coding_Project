from tkinter import *

window = Tk()

#widgets = Gui elements: buttons, Textboxes, labels, images
#windwos = Serves as a container to hold or contain these widgets

window.geometry("1200x700")
window.title("Windwos Testete")
#for photos Icon = PhotoImage(file='Imagename.png')
#+
#window.iconphoto(True,Icon)

window.configure(bg="red")  #bg is a short for background

label = Label(window, text="Hello World!", bg="black", fg="Blue") #You can also use font, relief + bd for border, padx + pady for space
# You can add photo by image, and use compound BOTTOM TOP RIGHT LEFT for the position of the photo

#label.pack()
label.place(x=100, y=100)
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
window.mainloop()

#progress bar
#For progress bar the script is { bar = Progressbar(window,orient=HORIZONTAL)
#       bar.pack(pady=10) }
# To access the bar's value the code is { bar['value'} }
#to have to bar value actually look like it is updating we need to use { window.update_idletasks() }
