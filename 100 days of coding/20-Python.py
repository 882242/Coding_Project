print("This is a CACULATOR!")
while True:
    Number1 = int(input("Number 1: "))
    Number2 = int(input("Number 2: "))
    Sign = input("addition, subtraction, division, or multiplying? (please type the signs specifically typed here!). ")
    if Sign == "addition":
        print(Number1 + Number2)
        continue
    elif Sign == "subtraction":
        print(Number1 - Number2)
        continue
    elif Sign == "division":
        print(Number1 / Number2)
        continue
    elif Sign == "multiplying":
        print(Number1 * Number2)
        continue
    else:
        print("Guess you don't need me!")
        break