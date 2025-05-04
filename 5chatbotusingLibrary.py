from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create chatbot
chatbot = ChatBot('TechieBot')

# Create and train the chatbot with English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

# Chat loop
print("🤖 TechieBot: Hello! Ask me anything. Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("🤖 TechieBot: Goodbye!")
        break
    response = chatbot.get_response(user_input)
    print("🤖 TechieBot:", response)