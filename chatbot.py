def chatbot_response(user_input):
    response = {
        "hello": "Well, hello there!",
        "how are you": "Living the dream in 0s and 1s.",
        "bye": "Goodbye, human. Come back soon."
    }
    for key in response: 
        if key in user_input.lower():
            return response[key]
    return "Hmm, I'm not sure what you mean."                                          

if __name__ == "__main__":
    print("Chatbot: Hi! I'm your friendly (or sarcastic) chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", chatbot_response(user_input))