print("Hey there! I'm your friendly chatbot.")
while True:
    user_input = input("You: ").lower().strip()
    if user_input in ["bye", "exit", "quit"]:
        print("ChatBot: It was nice talking to you. Take care!")
        break
    elif user_input == "hello":
        print("ChatBot: Hello! How's your day going?")
    elif user_input == "how are you":
        print("ChatBot: I'm just a bunch of code, but I'm happy to chat with you!")
    elif user_input == "what is your name":
        print("ChatBot: I'm just called ChatBot, but you can give me a cool name if you like!")
    elif user_input == "i'm fine" or user_input == "i am fine":
        print("ChatBot: That's great to hear!")
    elif user_input == "what can you do":
        print("ChatBot: I can chat with you! Want to talk about something?")
    elif user_input == "Tell about today":
        print("Chatbot: today is thursday such a great day")
    elif user_input == "Anything special":
        print("chatbot:  yeah we are friends now")
    elif user_input == "Thank you dear friend":
        print("Chatbot:you are welcome")
    else:
        print("ChatBot: I'm still learning. Can you try saying something else?",user_input)
