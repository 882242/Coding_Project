import threading
import time


# Define a background task
def background_task():
    while True:
        print("Running in the background...")
        time.sleep(2)  # Simulate work


# Create and start a thread
background_thread = threading.Thread(target=background_task,
                                     daemon=True)  # Set daemon=True to stop the task when the main program exits
background_thread.start()

# Main program
print("Main program is running...")
time.sleep(10)
print("Main program finished!")
