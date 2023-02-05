import random 
import datetime

print("Jo Bot: Hi there! I'm Jo Bot, what's your name?")
name = "Jo Bot"
user_name = input()
print(f"Hi there {user_name}, talk to me")
current_time = datetime.datetime.now().strftime("%H:%M:%S")

def respond(message): 
   
    default_responses = ["This is awkward" ,
                        "Sorry, I didn't get that.",
                        "I can't answer that, please ask me something else",
                        "Can you rephrase that please?",
                        "Sorry, you have written something I don't understand yet"]
    

    keywords = {
                "hello": ["Hello there!", "Hi"],
                "hi": ["Hello"],
                "goodbye": ["Goodbye!"],
                "bye": ["Bye!"], 
                "thanks": ["You're welcome!", "My pleasure"],
                "thank you": ["You're welcome!", "My pleasure"],
                "what's your name?": ["My name is Jo Bot"],
                "are you a robot?": ["I am", "What's a robot?... That was a joke :)", "Yes I am "],
                "how was your day?": ["Super!", "Great, thanks for asking"],
                "good": [ "I'm glad!","That's great!"],
                "what time is it?": [f"The time is {current_time}"],
                "tell me a joke": ["Why did the scarecrow win an award? Because he was outstanding in his field.",
                "Why don't scientists trust atoms? Because they make up everything.",
                "Why was the math book sad? Because it had too many problems.",
                "Why did the tomato turn red? Because it saw the salad dressing!",
                "Why did the cookie go to the doctor? Because it was feeling crumbly."],
                "how are you?": ["I'm wonderful, thanks for asking!", "I feel amazing!"]

                }
    
  
    for keyword in keywords.keys():
        if keyword in message.lower():
            bot_message = random.choice(keywords[keyword])
            return bot_message
    return random.choice(default_responses)

while True:
    message = input('{}: '.format(user_name) )
    response = respond(message)
    print("Jo Bot: " + response)
    if message == "stop" or message =="exit":
        break
