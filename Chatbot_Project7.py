import nltk
from nltk.chat.util import Chat, reflections

set_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you doing today ?", ]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there", ]
    ],
    [
        r"what is your name?",
        ["I am your friendly neighborhood chatbot", ]
    ],
    [
        r"how are you ?",
        ["I am fine, thank you! How can i help you?", ]
    ],
    [
        r"I am fine, thank you",
        ["great to hear that, how can i help you?", ]
    ],
    [
        r"I am a student at YearUp. Have you heard about YearUp?",
        ["YearUp! I have heard about YearUp. They are doing a lot for students.", ]
    ],
    [
        r"Do you like to watch movies?",
        ["I love to watch movies.The last movie that I watched was Glass Onion.", ]
    ],
    [
        r"i have watched that one too",
        ["It was good right?", ]
    ],
    [
        r"Yes, I enjoyed it a lot. I have to go now",
        ["ok we will talk later", ]
    ],
    [
        r"quit",
        ["Take care. See you soon :) ", "It was nice talking to you. See you soon :)"]
    ],
]


def chatbot():
    print("Hi, I'm the chatbot you built")


chatbot()

chat = Chat(set_pairs, reflections)
chat.converse()
if __name__ == "__main__":
    chatbot()
