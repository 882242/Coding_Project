import time
import threading

class timer:
    def __init__(self):
        self.running = False

    def start(self, seconds):
        self.running = True

        Timer = threading.Thread(target=self._countdown, args=(seconds,))
        Timer.start()

        StopInput = threading.Thread(target=self._listen_for_stop)
        StopInput.start()

    def _countdown(self, seconds):
        while seconds > 0 and self.running:
            print(f"time left: {seconds} seconds")
            time.sleep(1)
            seconds -= 1
        if not self.running:
            print("timer stopped by user")

    def _listen_for_stop(self):
        while self.running:
            user_input = input(" ")
            if user_input.strip().lower() == "stop":
                self.running = False
                break

if __name__ == "__main__":
    timer = timer()
    Duration = int(input("Enter the duration in seconds: "))
    timer.start(Duration)