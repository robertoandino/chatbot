import tkinter as tk
from tkinter import scrolledtext
import random

#TO UPDATE .exe file
#python -m PyInstaller --onefile --windowed chatbot_gui.py

# Bot response logic
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
        "thoughts": [
            "Is AI the future?",
            "Is it possible to upload a brain to the net?",
            "We'll we live in the net?"
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

# Handles user input and display chatbot's response
def handle_input():
    
    user_input = input_field.get()
    
    if user_input.lower() in ["bye", "exit", "quit"]:
        chat_area.insert(tk.END, "Chatbot: Goodbye human!\n")
        window.destroy()
        return
    
    #Display user input
    chat_area.insert(tk.END, f"You: {user_input}\n")

    #Get chatbot's response
    response = get_random_response(user_input)
    chat_area.insert(tk.END, f"Chatbot: {response}\n")
    input_field.delete(0, tk.END) #Clears input field


# Tkinter GUI Window
window = tk.Tk()
window.title("Chatbot")
window.geometry("500x600")
window.configure(bg="#2c3e50")

# Chat area 
chat_area = scrolledtext.ScrolledText(
    window, wrap=tk.WORD, font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50", state="normal"
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input field
input_frame = tk.Frame(window, bg="#2c3e50")
input_field = tk.Entry(
    input_frame, font=("Arial", 12), bg="#bdc3c7", fg="#2c3e50", relief=tk.FLAT
)
input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5),
send_button = tk.Button(
    input_frame, 
    text="Send", 
    command=handle_input,
    bg="#3498db",
    fg="white",
    font=("Arial", 12, "bold"),
    relief=tk.FLAT,
    activebackground="#2980b9",
)
send_button.pack(side=tk.RIGHT, padx=5, pady=5)
input_frame.pack(pady=5, padx=10, fill=tk.X)

# Inital greeting
chat_area.insert(tk.END, "Chatbot: Hello human!")

# Tkinter event loop
window.mainloop()