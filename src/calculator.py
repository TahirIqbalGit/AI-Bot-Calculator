from chatterbot import ChatBot
import time

bot = ChatBot(name="Bot Calculator", read_only=True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter="chatterbot.storage.SQLStorageAdapter")

# Clear Screen
print('\033c')

# Start Calculator
print("Hello, I'm Bot Calculator. How can I help you?")
print("<--- How to use? Type 'info' --->")

while True:
    # Taking Input from User
    user = input('Me : ')

    # Quit / Exit
    if user.lower() == "quit" or user.lower() == "exit":
        print("\nExiting", end='')
        time.sleep(3)
        print("...")
        print("===================")
        print("Do you like it...?")
        time.sleep(3)
        print("\tYES")
        print("===================")
        print("<--- Follow on GitHub --->")
        print("https://www.github.com/TahirIqbalGit/")
        break
    
    # For information
    elif user.lower() == "info":
        print("> Plus --> for addition\n"
              "> Minus --> for subtraction\n"
              "> Times --> for multiplication\n"
              "> Divided by --> for division\n")
        continue

    # Execute the Input getting from User
    try:
        response = bot.get_response(user)
        print("Bot :", response)
    except:
        print("Bot : Please Enter Valid Input.")
