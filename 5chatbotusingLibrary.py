import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot pairs (patterns and responses)
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I'm TechieBot. Your friendly assistant."]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "All good! How can I assist you?"]
    ],
    [
        r"what is your refund policy ?",
        ["Our refund policy allows returns within 30 days of purchase."]
    ],
    [
        r"(.*) (order|status) (.*)",
        ["Please provide your order ID, and I'll check it for you."]
    ],
    [
        r"bye|exit",
        ["Goodbye! Have a nice day.", "Bye! Come back if you need help."]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Could you please rephrase?", "Interesting! Tell me more."]
    ]
]

# Initialize chatbot
chatbot = Chat(pairs, reflections)

# Start chat
print("🤖 TechieBot: Hello! Type 'bye' or 'exit' to end.")
chatbot.converse()