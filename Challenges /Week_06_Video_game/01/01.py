from tkinter import *
import random

window = Tk()
window.geometry("1200x700")
window.title("Real Life RNG")

def RandomDiscovery():
    global RNG
    RNG = random.randint(5000,10000)
    if RNG < 5000:
        Rolled.config(text="You got Grass 1/2")
        print("GRASS")
    if RNG <= 7500 and RNG > 5000:
        Rolled.config(text="You got Dog Feces 1/4")
        print("dog")
    if RNG <= 8200 and RNG > 7500:
        Rolled.config(text="You got Rock 1/16")
        print("rovk")
    if RNG <= 8800 and RNG > 8200:
        Rolled.config(text="You got Water 1/32")
        print("water")
    if RNG <= 9000 and RNG > 8800:
        Rolled.config(text="You got Snow 1/64")
        print("snow")
    if RNG <= 9100 and RNG > 9000:
        Rolled.config(text="You got Shattered Bottle Glass 1/128")
        print("shattered")
    if RNG <= 9150 and RNG > 9100:
        Rolled.config(text="You got $5 Bill 1/256")
        print("$5 bill")
    if RNG <= 9175 and RNG > 9150:
        Rolled.config(text="You got $20 Bill 1/512")
        print("$20 bill")
    if RNG <= 9200 and RNG > 9175:
        Rolled.config(text="You got $50 Bill 1/512")
        print("$50 bill")
    if RNG <= 9300 and RNG > 9175:
        Rolled.config(text="You got Leather Gloves 1/128")
        print("leather")
    if RNG <= 9400 and RNG > 9300:
        Rolled.config(text="You got Key Chain 1/128")
        print("keychain")
    if RNG <= 9500 and RNG > 9300:
        Rolled.config(text="You got Slime 1/64")
        print("slime")
    if RNG <= 9600 and RNG > 9300:
        Rolled.config(text="You got Garbage 1/32")
        print("garbage")
    if RNG <= 9900 and RNG > 9300:
        Rolled.config(text="You got Empty Bottled Can 1/16")
        print("empty can")
    if RNG <= 9950 and RNG > 9900:
        Rolled.config(text="You got Unopened Pepsi 1/512")
        print("unopened")
    if RNG <= 9975 and RNG > 9950:
        Rolled.config(text="You got Unopened Coke 1/1024")
        print("unopened")
    if RNG <= 9990 and RNG > 9975:
        Rolled.config(text="You got Wallet 1/4148")
        print("wallet")
    if RNG <= 9995 and RNG > 9990:
        Rolled.config(text="You got Keys 1/8269")
        print("keys")
    if RNG <= 9997 and RNG > 9995:
        Rolled.config(text="You got Gun 1/15000")
        print("gun")
    if RNG <= 9999 and RNG > 9997:
        Rolled.config(text="You got Bank Key Card 1/25000")
        print("bank card")
    if RNG == 10000:
        Rolled.config(text="You got 100lb Diamond 1/50000")
        print("100lb")

def SaveToInvetory():
    global Rolled
    global SaveLabel
    current_roll_text = Rolled.cget("text")
    SaveLabel.config(text=current_roll_text)



InventoryBox = Label(window, pady=10, padx=1, bd=1, relief=RIDGE, width=20, height=50 )
InventoryBox.place(x=10)

InventoryTitle = Label(window, text="Inventory")
InventoryTitle.place(x=25, y=10)

SaveButton = Button(window, text="Save To Inventory", command=SaveToInvetory)
SaveButton.place(x=525, y=400)

SaveLabel = Label(window, text="Save To Inventory")
SaveLabel.place(x=25, y=40)

RollButton = Button(window, text="Roll", width=3, height=1, bd=1, relief=RIDGE, command=RandomDiscovery)
RollButton.place(x=565, y=350)

Rolled = Label(window, text="Rolled", width=50, height=1)
Rolled.place(x=367, y=300)

window.mainloop()

