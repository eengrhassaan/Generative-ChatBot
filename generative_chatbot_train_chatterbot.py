# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 23:41:24 2021

@author: Hassaan
"""

# ---------------- Importing Required Libraries ----------------
# Importing ChatBot Module from chatterbot library
from chatterbot import ChatBot  

# Importing ListTrainer from chatterbot.trainer
from chatterbot.trainers import ListTrainer

# --------------------------------------------------------------



# --------- Variables Declaration and Initialization -----------
chatbot_name = 'Jarvis'

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

# --------------------------------------------------------------



# ---------------- Initializing Library Instances --------------

# Intializing chatterbot ChatBot instance as chat_bot
chat_bot = ChatBot(
                    chatbot_name,
                    logic_adapters=[
                        {
                            "import_path": "chatterbot.logic.BestMatch",
                            'default_response': 'I am sorry, I do not understand what you are saying.',
                        }
                    ]
            )

# Initialize chatterbot Trainer instance as trainer_chat_bot
trainer_chat_bot = ListTrainer(chat_bot)

# --------------------------------------------------------------



# ------------------------- Train ChatBot ----------------------
trainer_chat_bot.train(conversation)
# --------------------------------------------------------------



# ------------------- Testing ChatBot Code ----------------------
while True:
    user_input = input("You: ")
    
    # Covering with in Try Except for Exception Handling
    try:
        # Check for User input if its  not Bye
        if (user_input.lower().find("bye") == -1):
            bot_response = chat_bot.get_response(user_input)
            print(f"Jarvis: {bot_response}")
            
        else:
            print("Jarvis: Bye. Nice talking to you :)")
            break

    except:
        print("User Exception from Keyboard")
        break
    # -------------------------------------------------

# --------------------------------------------------------------