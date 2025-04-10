import threading
import time


class timer:
    def __init__(self):
        self.running = False

    def start_timer(self, seconds):
        self.running = True

        timer_thread = threading.Thread(target=self._timer, args=(seconds,))
        timer_thread.start()

        listening_thread = threading.Thread(target=self._listen)
        listening_thread.start()

    def _timer(self, seconds):
        while self.running:
            print(f" {seconds}")
            time.sleep(0.1)
            seconds -= 0.1
        if not self.running:
            print("timer stopped")
            print(f" {seconds}")
            if seconds == 10:
                print("you won")
            else:
                print("you failed")
        elif seconds == 0:
            print("you failed")

    def _listen(self):
        while self.running:
            user_input = input(" ")
            if user_input.strip().lower() == "a":
                self.running = False
                break

if __name__ == "__main__":
    timer = timer()
    print("the goal of the game is to get the timer to stop at 10 seconds exact")
    print("press a and enter to stop the timer")
    input("press enter to start")
    timer.start_timer(20)