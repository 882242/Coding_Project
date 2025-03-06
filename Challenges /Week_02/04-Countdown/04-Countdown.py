#____________________________________________________________________________________
#   Purpose: Countdown timer
#   Author: Felix       Date: March 3, 2025     Class: ICS3C
#____________________________________________________________________________________
import time
import threading


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

#The self is self btw, I don't really know how to explain in detail, it is self. You can kind of see when i print in the parnthesis it's dog1.name which copies the self.name
'''

class CountdownTimer: #This class is for the timer
    def __init__(self):
        self.running = False #This is a variable for if the system is running or a boulian value

    def start_timer(self, seconds): #This is the function for starting and we have an array for seconds
        self.running = True  #This is to let the timer to start

        timer_thread = threading.Thread(target=self._countdown, args=seconds) #I created a thread that runs the countdown in the backround, args is the list of arrays you want or a tuple value
        timer_thread.start()

        #Now we need to create a thread that checks if i said stop to stop the countdown
        listenForStop = threading.Thread(target=self._listen_for_stop) #This does not need args since we are looking for 'stop' and not seconds
        listenForStop.start()

    def _countdown(self, seconds): #This is function is for the target of the thread and is also the countdown timer
        while seconds > 0 and self.running: #this loop checks if this class is running which Countdown.start_timer must be started
            print(f"Time left: {seconds} seconds") #The f in front of the string makes me be able to call something using {} which i called seconds in the string
            time.sleep(1)  # Wait for 1 second
            seconds = seconds - 1 # this subtracts the timer
            if not self.running: #This makes sense for the next function as it stops the timer
                print("Timer stopped by user!")
            elif seconds == 0: #This checks if the seconds is 0, and if it is it stops
                print("Countdown finished!")
                break

    def _listen_for_stop(self): #This function basicially checks if you put stop, and if you do it stops the countdown
        while self.running:
            User_input = input()
            if User_input.strip().lower() == "stop":
                self.running = False #Thsi stops the process of counting down
                break


if __name__ == "__main__": #This allows the class function to become a variable
    timer = CountdownTimer()
    duration = int(input("Enter the countdown time in seconds: ")) #This puts in the array of the functions which would be seconds
    print("Type 'stop' at any time to stop the timer.") #This reminds the user to type in stop to stop the timer anytime
    timer.start_timer(duration) #This puts the number that the user inputted into the functions which becomes the seconds
#iasdjaodij

