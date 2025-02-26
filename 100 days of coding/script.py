import time

# rigged ahh game
while True:
    print("left or right?")
    direction = input("> ")
    if direction == "left":
        print("loading answer...")
        time.sleep(1)
        break
    elif direction == "right":
        time.sleep(1)
        print("Nice your alive!")
        continue
    else:
        time.sleep(1)
        print("are you seroius?")
        time.sleep(5)
        print("Your a genuis you got it right!")
        exit()
print("The game is over, you've failed!")

