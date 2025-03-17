#____________________________________________________________________________________
#   Purpose: Countdown timer
#   Author: Felix       Date: March 3, 2025     Class: ICS3C    Last Updated: March 6, 2025
#____________________________________________________________________________________



#This is a class function, which is like a function built up by alot of functions
#An example is a car, it needs a gas pedal, a brake, or the window wipers, the class funciton
#Would have all those things inside which we can then identify as ClassName.ClassFunction
''' 
class Dog:
    def __init__(self, name, breed): #the 'init', i actually don't really know what it does, every class has it and i only know that it is there to idetify things in the class
        self.name = name   #The above is an array which we identify the name varieable as the variable on top
        self.breed = breed  #This is the same thing


dog1 = Dog("Rover", "Labrador") #Now we can put dog 1 as a variable for the variable for the arrays
print(dog1.name) #This prints ROver
print(dog1.breed) #This prints Labrador

#The self is self, I don't really know how to explain in detail, it is self. You can kind of see when i print in the parnthesis it's dog1.name which copies the self.name
'''
import time
import threading

class timer:
    def __init__(self): #this init is a part of the class function that can help easily identify things like self
        self.running = False #we put the class it self to false so it basicially stops the whole class function

    def start(self, seconds): #here we define a function to start, the self and seconds is an array that we are using
        self.running = True #this makes running true and now it will run the things at the buttom
        #these 2 threads make it so it can run 2 things at once, the timer is for the countdown and the stop input is to stop the timer
        Timer = threading.Thread(target=self._countdown, args=(seconds,))
        Timer.start()
#we have to define the target function which we did in the "target="
        StopInput = threading.Thread(target=self._listen_for_stop)
        StopInput.start()
#and we have to start it
    def _countdown(self, seconds): #here we define the cd
        while seconds > 0 and self.running: #we check if seconds is greater than 0 and if self.running is true
            print(f"time left: {seconds} seconds") #this is the cd loop
            time.sleep(1)
            seconds -= 1
        if not self.running: #here this checks if self.running is false if it does it does wants on the bottom
            print("timer stopped by user")
        elif seconds == 0: #this checks if seconds is 0 and tells the user the cd is finished
            print("Countdown finished!")

    def _listen_for_stop(self): #this is our listen for stop function
        while self.running:
            user_input = input(" ") #this is the user input
            if user_input.strip().lower() == "stop":  #this checks it the user saids stop
                self.running = False #if it sees stop self.running would = False and it does what our loop on top does, print timer has been stopped by user
                break

if __name__ == "__main__": #this operator allows classes, which is the whole thing above to be able to be named
    timer = timer() #here we name the timer
    Duration = int(input("Enter the duration in seconds: ")) #this is the duration that the user wants to put in
    timer.start(Duration) #we put the duration in, and now it acts as a seconds in the class function
    #the function timer.start() would've not worked if it wasn't for the name operator since we can't access the child of the class, or the start so it can start the cd
