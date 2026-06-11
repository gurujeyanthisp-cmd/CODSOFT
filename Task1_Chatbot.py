# File: task1_chatbot.py
# Task 1: Rule-Based Chatbot for CodeSoft AI Internship

import random
import datetime

print("Bot: Hello! I am CodeBot. Type 'bye' to exit.")

# Predefined responses
greetings = ["Hello!", "Hi there!", "Hey! How are you?"]
farewells = ["Goodbye!", "See you later!", "Bye! Have a great day!"]

while True:
    user_input = input("You: ").lower().strip()  # Convert to lowercase and remove spaces

    # Greeting responses
    if user_input in ["hi", "hello", "hey"]:
        print("Bot:", random.choice(greetings))

    # How are you response
    elif "how are you" in user_input:
        print("Bot: I'm doing well, thank you! How about you?")

    # Bot name response
    elif "your name" in user_input:
        print("Bot: I am CodeBot, your friendly assistant!")

    # Date response
    elif "date" in user_input:
        today = datetime.date.today()
        print(f"Bot: Today is {today}")

    # Time response
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Bot: Current time is {now}")

    # Goodbye response
    elif "bye" in user_input:
        print("Bot:", random.choice(farewells))
        break

    # Unknown input
    else:
        print("Bot: Sorry, I didn't understand that.")
