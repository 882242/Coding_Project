import threading
import time


class CountdownTimer:
    def __init__(self):
        self.running = False  # Variable to control if the timer is running

    def start_timer(self, seconds):
        # Set the running flag to True
        self.running = True

        # Create a thread for the countdown timer
        timer_thread = threading.Thread(target=self._countdown, args=(seconds,))
        timer_thread.start()

        # Create another thread to listen for the "stop" command
        input_thread = threading.Thread(target=self._listen_for_stop)
        input_thread.start()

    def _countdown(self, seconds):
        while seconds > 0 and self.running:
            print(f"Time left: {seconds} seconds")
            time.sleep(1)  # Wait for 1 second
            seconds -= 1

        if not self.running:
            print("Timer stopped by user!")
        elif seconds == 0:
            print("Countdown finished!")

    def _listen_for_stop(self):
        # Continuously listen for the "stop" input
        while self.running:
            user_input = input(" ")
            if user_input.strip().lower() == "stop":
                self.running = False  # Stop the countdown
                break


# Main function
if __name__ == "__main__":
    timer = CountdownTimer()

    # Ask the user for the countdown duration
    duration = int(input("Enter the countdown time in seconds: "))
    print("Type 'stop' at any time to stop the timer.")

    # Start the countdown timer
    timer.start_timer(duration)


