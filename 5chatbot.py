def customer_support_bot():
    responses = {
        "hello": "Hello! Welcome to TechieStore Customer Support. How can I help you today?",
        "hi": "Hi there! How can I assist you with your TechieStore experience?",
        "how are you": "I'm just a support bot, but I'm here to help you!",
        "order status": "Sure! Please provide your order ID to check the status.",
        "refund policy": "Our refund policy allows returns within 30 days of delivery. Would you like to initiate a return?",
        "contact": "You can reach our support team at support@techiestore.com or call 1800-TECHIE.",
        "bye": "Thanks for visiting TechieStore! Have a wonderful day!",
        "help": "I can assist with order tracking, refund policies, and contact info. What would you like to know?",
        "default": "I'm sorry, I didn't understand that. Could you please rephrase your question or type 'help'?"
    }

    def get_response(user_input):
        for key in responses:
            if key in user_input:
                return responses[key]
        return responses["default"]

    print("🤖 TechieBot: Hello! Welcome to TechieStore Customer Support. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()
        if user_input == "bye":
            print("🤖 TechieBot:", responses["bye"])
            break
        response = get_response(user_input)
        print("🤖 TechieBot:", response)

if __name__ == "__main__":
    customer_support_bot()