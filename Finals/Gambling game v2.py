#____________________________________________________________________________________
#   Purpose: Make my gambling game have visuals and easier to play
#   Author: Felix       Date: Feb. 25, 2025     Class: ICS3C
#____________________________________________________________________________________

from tkinter import *
import random
import time
import threading

window = Tk() #Tkinter shortcut

Coins = 100 #this is the coin
twoxWIN = False #everything here and under are the unlocks of abilities which are set to false cause you don't spawn with them
TripleWIN = False
Income1 = False
Income2 = False
HalfTheChance = False
GodWIN = False
GodINCOME = False
GodCHANCE = False
#_______________________________________________________________________________________

#These are all the buttons and labels of the things in the game, Basically everything here is the visuals

Gamble_button = Button(window, text="Gamble", command=lambda: Gamble())
Gamble_button.place(x=355, y=175)

Coin_Background = Label(window, padx=100, pady=150, relief=SUNKEN)
Coin_Background.place(x=35, y=45)

Coin_Balance = Label(window, text=Coins)
Coin_Balance.place(x=200, y=55)

Coin_text = Label(window, text="Coins")
Coin_text.place(x=55, y=55)

Goal = Label(window, text="Get to 1M coins!!!")
Goal.place(x=342, y=275)

Win_lose = Label(window, text="Win lose")
Win_lose.place(x=368, y=225)

Gamble_1 = Label(window, text="7")
Gamble_1.place(x=340, y=100)

Gamble_2 = Label(window, text="7")
Gamble_2.place(x=390, y=100)

Gamble_3 = Label(window, text="7")
Gamble_3.place(x=440, y=100)

Shop_background = Label(window, relief=SUNKEN, padx=100, pady=150)
Shop_background.place(x=550, y=45)

Shop_text = Label(window, text="Shop")
Shop_text.place(x=633.5, y=55)

Double_Gamble = Label(window, text="2x Win   (50)")
Double_Gamble.place(x=560, y=75)

Purcahse_DG = Button(window, text='buy', padx=1, pady=1, relief=SUNKEN, command=lambda: UNlock_2x())
Purcahse_DG.place(x=690, y=70)

Triple_Gamble = Label(window, text="3x Win   (150)")
Triple_Gamble.place(x=560, y=100)

Purchase_TG = Button(window, text='buy', padx=1, pady=1, relief=SUNKEN, command=lambda: UNlockTrip())
Purchase_TG.place(x=690, y=95)

Passive_Income1 = Label(window, text="Income  (100)")
Passive_Income1.place(x=560, y=124)

Purchase_Income1 = Button(window, text="buy", command=lambda: BuyPI1())
Purchase_Income1.place(x=690, y=121)

FasterINC = Label(window, text="Income2 (500)")
FasterINC.place(x=560, y=148)

Purchase_FASTERINC = Button(window, text="buy", command=lambda: BuyPI2())
Purchase_FASTERINC.place(x=690, y=145)

Half_Chance = Label(window, text="Half Chance (1000)")
Half_Chance.place(x=560, y=170)

HCBuy = Button(window, text="buy", command=lambda: Half_Chances())
HCBuy.place(x=690, y=168)

Godly_WIN = Label(window, text="Godly Win (5000)")
Godly_WIN.place(x=560, y=190)

Buy_Godly_WIN = Button(window, text="buy", command=lambda: UnLockGodlyWin())
Buy_Godly_WIN.place(x=690, y=190)

Buy_Godly_WIN = Button(window, text="buy", command=lambda: UnlockGodINCOME())
Buy_Godly_WIN.place(x=690, y=210)

Godly_INcome = Label(window, text="Godly Income (10000)")
Godly_INcome.place(x=560, y=210)

PURCHInsaneGODChance = Button(window, text="buy", command=lambda: BUYGODCHANCE())
PURCHInsaneGODChance.place(x=690, y=235)

InsanceFODCHANE = Label(window, text="Godly Chance (10000)")
InsanceFODCHANE.place(x=560, y=240)
#_______________________________________________________________________________________

#These are all the Functions to unlock a certain ability

def BUYGODCHANCE():
    global Coins
    global GodCHANCE
    if Coins >= 10000 and GodCHANCE == False:
        Coins = Coins - 10000
        GodCHANCE = True
        Coin_Balance = Label(window, text=Coins)


def UnlockGodINCOME():
    global GodINCOME
    global Coins
    if Coins >= 10000 and GodINCOME == False:
        Coins -= 10000
        GodINCOME = True
        Coin_Balance.config(text=Coins)
        GODINCOMES()

def GODINCOMES():
    global Coins
    window.after(100, GODINCOMES)
    Coins += 100
    Coin_Balance.config(text=Coins)

def UnLockGodlyWin():
    global GodWIN
    global Coins
    if Coins >= 5000 and GodWIN == False:
        Coins -= 5000
        GodWIN = True
        Coin_Balance.config(text=Coins)

def Half_Chances():
    global HalfTheChance
    global Coins
    global r1
    global r2
    global r3
    if Coins >= 1000 and HalfTheChance == False:
        Coins -= 1000
        HalfTheChance = True
        Coin_Balance.config(text=Coins)


def BuyPI1():
    global Income1
    global Coins
    if Coins >= 100 and Income1 == False:
        Coins -= 100
        Income1 = True
        Coin_Balance.config(text=Coins)
        BogthINCOME = Label(window, text="Income Bought")
        BogthINCOME.place(x=55, y=120)
        PI1()

def PI1():
    global Coins
    window.after(1000, PI1)
    Coins += 1
    Coin_Balance.config(text=Coins)

def BuyPI2():
    global Coins
    global Income2
    if Coins >= 500 and Income2 == False:
        Coins -= 500
        Income2 = True
        Coin_Balance.config(text=Coins)
        BoughtINC2 = Label(window, text="Income2 Bought")
        BoughtINC2.place(x=55, y=120)
        PI2()

def PI2():
    global Coins
    window.after(500, PI2)
    Coins += 1
    Coin_Balance.config(text=Coins)

def UNlockTrip():
    global TripleWIN
    global Coins
    if Coins >= 150 and TripleWIN == False and twoxWIN == True:
        Coins = Coins - 150
        TripleWIN = True
        Coin_Balance.config(text=Coins)
        BoughtUNLCOKTRIPE = Label(window, text="3x Win Bought")
        BoughtUNLCOKTRIPE.place(x=55, y=97)

def UNlock_2x():
    global twoxWIN
    global Coins
    if Coins >= 50 and twoxWIN == False:
        Coins -= 50
        Coin_Balance.config(text=Coins)
        twoxWIN = True
        BoughtUNLOCK2x = Label(window, text="2x Win Bought")
        BoughtUNLOCK2x.place(x=55, y=75)
#_______________________________________________________________________________________

#This function in particular is the Gambling function which I had to copy and paste a specific code (Half the Chance and GodCHANCE)
#So I can skip some code so i Lowk went lazy

def Gamble():
    global Coins
    global r1
    global r2
    global r3
    global HalfTheChance
    global GodCHANCE
    if Coins > 0:
        Coins = Coins - 1
        WinCoinAmount = 50
        if HalfTheChance == False:
            r1 = random.randint(1, 10)
            r2 = random.randint(1, 10)
            r3 = random.randint(1, 10)
            Gamble_1.config(text=r1)
            Gamble_2.config(text=r2)
            Gamble_3.config(text=r3)
            Coin_Balance.config(text=Coins)
            if r1 == r2 == r3:
                if twoxWIN == True:
                    Coins = Coins + WinCoinAmount * 2
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                if TripleWIN == True:
                    Coins = Coins + WinCoinAmount * 3
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                if GodWIN == True:
                    Coins = Coins + WinCoinAmount * 500
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                else:
                    Coins = Coins + WinCoinAmount
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
            else:
                Win_lose.config(text="lose")
        if HalfTheChance == True:
            r1 = random.randint(1, 5)
            r2 = random.randint(1, 5)
            r3 = random.randint(1, 5)
            Gamble_1.config(text=r1)
            Gamble_2.config(text=r2)
            Gamble_3.config(text=r3)
            Coin_Balance.config(text=Coins)
            if r1 == r2 == r3:
                if twoxWIN == True:
                    Coins = Coins + WinCoinAmount * 2
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                if TripleWIN == True:
                    Coins = Coins + WinCoinAmount * 3
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                if GodWIN == True:
                    Coins = Coins + WinCoinAmount * 500
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                else:
                    Coins = Coins + WinCoinAmount
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
            else:
                Win_lose.config(text="lose")
                if HalfTheChance == True and GodCHANCE == False:
                    r1 = random.randint(1, 5)
                    r2 = random.randint(1, 5)
                    r3 = random.randint(1, 5)
                    Gamble_1.config(text=r1)
                    Gamble_2.config(text=r2)
                    Gamble_3.config(text=r3)
                    Coin_Balance.config(text=Coins)
                    if r1 == r2 == r3:
                        if twoxWIN == True:
                            Coins = Coins + WinCoinAmount * 2
                            Coin_Balance.config(text=Coins)
                            Win_lose.config(text="Win")
                        if TripleWIN == True:
                            Coins = Coins + WinCoinAmount * 3
                            Coin_Balance.config(text=Coins)
                            Win_lose.config(text="Win")
                        if GodWIN == True:
                            Coins = Coins + WinCoinAmount * 500
                            Coin_Balance.config(text=Coins)
                            Win_lose.config(text="Win")
                        else:
                            Coins = Coins + WinCoinAmount
                            Coin_Balance.config(text=Coins)
                            Win_lose.config(text="Win")
                    else:
                        Win_lose.config(text="lose")
        if GodCHANCE == True:
            HalfTheChance = False
            r1 = random.randint(1, 2)
            r2 = random.randint(1, 2)
            r3 = random.randint(1, 2)
            Gamble_1.config(text=r1)
            Gamble_2.config(text=r2)
            Gamble_3.config(text=r3)
            Coin_Balance.config(text=Coins)
            if r1 == r2 == r3:
                if twoxWIN == True:
                    Coins = Coins + WinCoinAmount * 2
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                if TripleWIN == True:
                    Coins = Coins + WinCoinAmount * 3
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                if GodWIN == True:
                    Coins = Coins + WinCoinAmount * 500
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
                else:
                    Coins = Coins + WinCoinAmount
                    Coin_Balance.config(text=Coins)
                    Win_lose.config(text="Win")
            else:
                Win_lose.config(text="lose")
        if Coins == 0:
            Win_lose.config(text="Broke ahh")

#_______________________________________________________________________________________

#windows configurations

window.title("Gambling Game")
window.geometry("800x400")
window.mainloop()

#This is a basic copy of the Old gambling game and then we just added Visuals, but we also got rid of a while true loop