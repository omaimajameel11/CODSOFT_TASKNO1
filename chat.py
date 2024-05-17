def chatbot(input_text):
    if "hello" in input_text.lower():
        return "Hello! How can I assist you today?"
    elif "how are you" in input_text.lower():
        return "I'm just a bot, but thanks for asking!"
    elif "what is your name" in input_text.lower():
        return "I'm a simple chatbot. You can call me ChatBot."
    elif "bye" in input_text.lower():
        return "Goodbye! Have a great day!"
    elif "weather" in input_text.lower():
        return "I'm sorry, I can't provide real-time weather updates."
    elif "joke" in input_text.lower():
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "how old are you" in input_text.lower():
        return "I'm just a program, so I don't have an age!"
    elif "thanks" in input_text.lower() or "thank you" in input_text.lower():
        return "You're welcome! If you have any more questions, feel free to ask."
    elif "how to" in input_text.lower():
        return "I'm sorry, I'm not equipped to provide tutorials. You can try searching online for resources."
    elif "help" in input_text.lower() or "support" in input_text.lower():
        return "Sure, I'm here to help. What do you need assistance with?"
    elif "what can you do" in input_text.lower():
        return "I can answer basic questions, tell jokes, provide simple assistance, and more. Feel free to ask!"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase or ask something else?"

def main():
    print("Welcome to the Simple ChatBot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(chatbot(user_input))
            break
        else:
            print("Bot:", chatbot(user_input))

if __name__ == "__main__":
    main()
