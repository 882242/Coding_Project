from os import WCONTINUED

print("This is a gambling game!")
print("The goal of the game is to get all three numbers to be the same!")
print("You can type in 'shop' to buy buffs")
print("This is (V1.0)")
balance = 50
DoubleJackpotReward = False
MoneyBackPassive = False
SecretFound1 = False
print("Your staring Balance is :", balance)
import random
import time
import threading

PassiveIncome = False
PassiveDebounce = False

def passiveincomefunction():
    global balance
    balance = balance + 25
    print("passive income added!")

def passiveincome():
    global PassiveDebounce
    global PassiveIncome
    if PassiveIncome == True:
        if PassiveDebounce == False:
            PassiveDebounce = True
            passiveincomefunction()
            time.sleep(60)
            PassiveDebounce = False












while True:
    AinputToGamble = input("Put the letter a to start the game!: ")
    balance = balance

    if PassiveIncome == True:
        PassiveIncomeWorking = threading.Thread(target=passiveincome)
        PassiveIncomeWorking.start()


    if balance == 0:
        print("You have no more money! Broke Boi!")
        break

    if AinputToGamble == "Secret":
        if SecretFound1 == False:
            print("You found the secret!")
            print("50 coins added to your balance!")
            SecretFound1 = True
            balance = balance + 50
            continue
        if SecretFound1 == True:
            print("You already found this secret!")
            continue

    if AinputToGamble == "shop":
        print("Welcome to the shop!")
        print("Here are the buffs you can purchase: ")
        print("1 = Get %50 money back after you gamble once, 50 coins")
        print("2 = Double jackpot amount, 50 coins")
        print("3 = Passive income of 25 a minute, 100 coins")
        Purchasing = int(input("Put the number you want to purchase: "))

        if Purchasing == 1:
            if 50 <= balance:
                print("Buff is purchased!")
                balance = balance - 50
                MoneyBackPassive = True
                continue
            if balance <= 50:
                print("You don't have enough money to buy this buff!")

        if Purchasing == 2:
            if 50 <= balance:
                DoubleJackpotReward = True
                print("Buff is purchased!")
                balance = balance - 50
                continue
            if balance <= 50:
                print("You don't have enough money to buy this buff!")
                continue
            if DoubleJackpotReward == True:
                print("You already purchased this buff!")
                continue

        if Purchasing == 3:
            if 100 <= balance:
                print("buff is purchased!")
                PassiveIncome = True
                balance = balance - 100
            if balance <= 100:
                print("You don't have enough money to buy this buff!")
            if PassiveIncome == True:
                print("You already purchased this buff!")
                continue

    if AinputToGamble == "a":
        X = random.randint(1, 10)
        Y = random.randint(1, 10)
        Z = random.randint(1, 10)
        print(X, Y, Z)
        if X == Y == Z:
            time.sleep(1)
            print(" YOU WON THE JACKPOT!")
            balance = balance + 50
            print("Your Balance is :", balance)
            if DoubleJackpotReward == True:
                balance = balance + 50
                print("Since you have Double Jackpot rewards 50 coins have been added to your balance!")
            continue
        else:
            print("Nothing, try again!")
            balance = balance - 1
            if MoneyBackPassive == True:
                balance = balance + 0.5
            print("Your Balance is :", balance)
            continue
    else:
        time.sleep(1)
        print("You didn't type a or you typed too many a's, try again!")
        continue