# Simple Chatbot using rule-based logic
def get_response(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input or 'hi' in user_input:
        return "Hello! How can I help you?"
    elif 'name' in user_input:
        return "I'm a simple chatbot."
    elif 'weather' in user_input:
        return "I can't check the weather, but I hope it's nice!"
    elif 'bye' in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."

if __name__ == "__main__":
    print("Chatbot: Type 'bye' to exit.")
    while True:
        user = input("You: ")
        if 'bye' in user.lower():
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", get_response(user))
