import time


#this makes the console sing lingangguli by Don Pollo
def singlingaguliguliguli():
    print("linganguliguliguli")
    time.sleep(3)
    print("Wacha")
    time.sleep(1.1)
    print("linganguuu")
    time.sleep(1.4)
    print("linganguuu")
    time.sleep(1.4)

while True:
    SingLingAngguliguliguli = input("Sing linganguliguliguli? ")
    if SingLingAngguliguliguli == "yes":
        singlingaguliguliguli()
        singlingaguliguliguli()
        singlingaguliguliguli()
        singlingaguliguliguli()
        singlingaguliguliguli()
        print("Thank you.")
        break
    if SingLingAngguliguliguli == "no":
        print("Why?")
        continue
    else:
        print("Please answer yes or no.")




