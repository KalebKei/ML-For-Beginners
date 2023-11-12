# More improved bot with the ability to "relate" more.
import random
from textblob import TextBlob

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

print("Hello, I am a simple conversational bot. I am tasked with conversing with you, would you like to join me?\n")
print("To converse, please wait until I respond, then simply type into the command line. Finish your thought by pressing enter. To finish our conversation, please request to \"bye\".\n")

print("How are you doing today?")

userInput = input()
while(userInput.lower() != "bye"): 
    user_input_blob = TextBlob(userInput).correct()
    if user_input_blob.sentiment.polarity <= -0.5:
        response = "Oh dear, that sounds bad. "
    elif user_input_blob.sentiment.polarity < 0:
        response = "Hmm, that's not great. "
    elif user_input_blob.sentiment.polarity <= 0.5:
        response = "Well, that sounds good. "
    elif user_input_blob.sentiment.polarity <= 1:
        response = "Wow, that sounds great. "

    if(user_input_blob.noun_phrases != []):
        response += "Tell me more about " + user_input_blob.noun_phrases[0].pluralize()
    print(response)
# https://textblob.readthedocs.io/en/dev/quickstart.html#create-a-textblob
# DEBUG info
    # print("*********************")
    # print(user_input_blob)
    # print(user_input_blob.sentiment)
    # print(user_input_blob.sentiment.polarity)
    # print(user_input_blob.noun_phrases)
    # print("*********************")
    userInput = input()

print("Have a great rest of your day!")