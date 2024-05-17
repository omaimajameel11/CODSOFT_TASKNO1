# CODSOFT_TASKNO1

# Chatbot with rule-based responses
This is a simple chatbot implemented in Python. The chatbot responds to user inputs based on predefined rules using if-else statements. This project is designed to help you understand the basics of natural language processing (NLP) and conversation flow.

## Features
- Responds to user inputs with predefined replies.
- Uses if-else statements to match user queries with appropriate responses.
- Provides a basic understanding of chatbot interaction and flow.

## Getting Started
These instructions will help you set up and run the chatbot on your local machine.

### Prerequisites
- Python 3.x

### Usage

When you run the chatbot script, it will prompt you to enter a message. The chatbot will respond based on the predefined rules set in the script. 

Example interaction:

Hello! I'm a simple chatbot. How can I help you today?

> What is your name?

My name is SimpleBot.

> How are you?

I'm just a bunch of code, so I don't have feelings, but thank you for asking!

> Bye

Goodbye! Have a great day!

### Customization

You can customize the chatbot by adding more if-else conditions to handle different user inputs. For example, to handle a new query like "What is the weather?", you can add:

```python
elif user_input.lower() == 'what is the weather?':
    print("I don't have access to the internet right now, so I can't check the weather for you.")
```

### Output

[Screenshot 2024-05-17 091317](https://github.com/omaimajameel11/CODSOFT_TASKNO1/assets/167120544/16c1ee85-7b61-4502-9e4c-951219427c1d)

