# app/main.py
import datetime

def greet_user(name):
    now = datetime.datetime.now()
    return f"Hello {name}! Current server time is {now.strftime('%Y-%m-%d %H:%M:%S')}."

if __name__ == "__main__":
    name = input("Enter your name: ")
    message = greet_user(name)
    print(message)
