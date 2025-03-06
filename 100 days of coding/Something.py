import time
import threading


class Countdown:
    def __init__(self):
        self.running = False

    def start_timer(self, seconds):
        self.running = True

        timer_thread = threading.Thread(target=self._countdown, args=(seconds,))
        timer_thread.start()

        listen_thread = threading.Thread(target=self._listenforstop)
        listen_thread.start()

    def _countdown(self, seconds):
        while seconds > 0 and self.running:
            print(f"time left : {seconds}")
            time.sleep(1)
            seconds = seconds - 1
        if not self.running:
            print("timer stopped")
        elif seconds == 0:
            print("countdown finished")

    def _listenforstop(self):
        while self.running:
            UUserinput = input("  ")
            if UUserinput.strip().lower() == "stop":
                self.running = False
                break


if __name__ == "__main__":
    timer = Countdown()
    duration = int(input("Type in the number for me to countdown:  "))
    timer.start_timer(duration)
