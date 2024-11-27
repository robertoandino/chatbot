import random

def get_random_response(user_input):

    responses = {
        "hello": [
            "Hello human!",
            "Hi, there! Ready to chat?",
            "Hey! How's it going?"
        ],
        "how are you": [
            "Living the dream in 0s and 1s.",
            "I'm just a bot, but thanks for asking!",
            "Fantastic! I could run for days without getting tired."
        ],
        "bye": [
            "Goodbye! Come back soon!",
            "See you later, human",
            "Farewell! Don't forget to recharge."
        ],
        "joke": [
            "Why did the programmer quit his job? Because he didn't get arrays.",
            "What do computers snack on? Microchips!",
            "I would tell you a UDP joke, but you might not get it."
        ]
    }

    # Loop through hardcoded responses
    for key in responses:
        # Check if keyword exists in user's input (case-sensitive)
        if key in user_input.lower():
            # Choose random response from the list
            return random.choice(responses[key])
        
    # Default response if keyword does not match
    return "Don't know what you mean human."

# Just calls get_random_response
def chatbot_response(user_input):
    return get_random_response(user_input)      
       
#Main script
if __name__ == "__main__":
    
    print("Chatbot: Hi! I'm your friendly (or sarcastic) chatbot!")
    
    while True:
        
        user_input = input("You: ")
        
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        
        print("Chatbot:", chatbot_response(user_input))