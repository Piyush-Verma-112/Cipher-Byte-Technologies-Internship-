import tkinter as tk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Function to handle user choice
def play(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    
    # Display result in a message box
    result_text = f"You chose: {user_choice}\nComputer chose: {computer_choice}\n\n{result}"
    messagebox.showinfo("Result", result_text)

# Creating the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")

# Adding a label
label = tk.Label(root, text="Choose your option:", font=("Arial", 14))
label.pack(pady=20)

# Creating buttons for each option
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_button = tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play('rock'))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play('paper'))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play('scissors'))
scissors_button.pack(side=tk.LEFT, padx=10)

# Running the main event loop
root.mainloop()
