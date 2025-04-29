from tkinter import *
import random

window = Tk()
window.geometry("1200x700")
window.title("RNG Survival")

Plus1WoodCount = 0
Plus1BrickCount = 0

def RNGEvent():
    RNG = random.randint(1,100)
    global Plus1WoodCount
    global Plus1BrickCount
    if RNG > 50:
        Plus1WoodCount = Plus1WoodCount + 1
        print(f"wood {Plus1WoodCount}")
        CheckWoodCount()
        RolledEvent.config(text='Discovered Wood!')
    if RNG <= 50:
        RolledEvent.config(text="Discovered Stone!")
        Plus1BrickCount = Plus1BrickCount + 1
        CheckBrickCount()
        print(f"stone {Plus1BrickCount}")


def CraftCampfire():
    global CampFireCount
    global Plus1WoodCount
    CampFireCount = CampFireCount + 1
    Plus1WoodCount = Plus1WoodCount - 3
    print(Plus1WoodCount)
    InvCampFireCount.config(text=int(CampFireCount))
    if Plus1WoodCount < 3:
        CraftCampfireBox.config(state=DISABLED)

def CheckWoodCount():
    if Plus1WoodCount >= 3:
        CraftCampfireBox.config(state=NORMAL)

def CheckBrickCount():
    if Plus1BrickCount >= 3:
        CraftBrick.config(state=NORMAL)

def CraftBrick():
    global BrickCount
    global Plus1BrickCount
    BrickCount = BrickCount + 1
    Plus1BrickCount = Plus1BrickCount - 3
    print(f" stone {Plus1BrickCount}")
    print(Plus1BrickCount)
    InvBrickCount.config(text=int(BrickCount))
    if Plus1BrickCount < 3:
        CraftBrick.config(state=DISABLED)




CraftingStationBox = Label(window, width=20, height=250, bd=2, relief=SUNKEN)
CraftingStationBox.place(x=10, y=0)

CraftingTitleBox = Label(window, text="Crafting")
CraftingTitleBox.place(x=74, y=10)

CraftCampfireBox = Button(window, text="Craft Campfire", width=15, height=2, bd=2, relief=SUNKEN, state=DISABLED, command=CraftCampfire)
CraftCampfireBox.place(x=17, y=40)

RollBox = Button(window, text="Roll", width=15, height=2, bd=2, relief=SUNKEN, command=RNGEvent)
RollBox.place(x=515, y=350)

RolledEvent = Label(window, text="Rolled Event", width=35, height=2)
RolledEvent.place(x=440, y=250)

InventoryBox = Label(window, width=20, height=250, bd=2, relief=SUNKEN)
InventoryBox.place(x=1000, y=0)

InventoryTitleBox = Label(window, text="Inventory")
InventoryTitleBox.place(x=1065, y=10)

InvCampFire = Label(window, text="Campfire")
InvCampFire.place(x=1015, y=40)

CampFireCount = 0

InvCampFireCount = Label(window, text=CampFireCount, bd=2, relief=SUNKEN, width=1, height=1)
InvCampFireCount.place(x=1150, y=40)

CraftBrick = Button(window, text='Craft Brick', bd=2, relief=SUNKEN, width=15, height=2, state=DISABLED, command=CraftBrick)
CraftBrick.place(x=17, y=80)

InvBrick = Label(window, text="Brick")
InvBrick.place(x=1015, y=60)

BrickCount = 0

InvBrickCount = Label(window, text=BrickCount, bd=2, relief=SUNKEN, width=1, height=1)
InvBrickCount.place(x=1150, y=60)

window.mainloop()