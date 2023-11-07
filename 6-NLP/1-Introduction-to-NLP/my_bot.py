# I made my own file because I want to make the bot. I don't want it done for me
import random

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

print("Hello, I am a simple conversational bot. I am tasked with conversing with you, would you like to join me?\n")
print("To converse, please wait until I respond, then simply type into the command line. Finish your thought by pressing enter. To finish our conversation, please request to \"exit\".\n")

print("Please begin our conversation...")

userInput = input().lower()
while(userInput != "exit"): 
    print(random_responses[random.randint(0, len(random_responses) - 1)])
    userInput = input().lower()
