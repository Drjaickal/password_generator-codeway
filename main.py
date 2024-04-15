import random  # Import the random module for generating random characters
from tkinter import *  # Import everything from the tkinter library for creating the GUI
import string  # Import the string module for accessing character sets

def generate_password():
  """
  This function generates a random password with a mix of uppercase and lowercase letters, symbols, and digits.
  """
  password = []  # Create an empty list to store the password characters
  for i in range(5):  # Loop 5 times to generate 5 characters
    alpha = random.choice(string.ascii_letters)  # Choose a random letter (uppercase or lowercase)
    symbol = random.choice(string.punctuation)  # Choose a random symbol
    numbers = random.choice(string.digits)  # Choose a random digit
    password.append(alpha)  # Add the chosen letter to the password list
    password.append(symbol)  # Add the chosen symbol to the password list
    password.append(numbers)  # Add the chosen digit to the password list

  y = "".join(str(x) for x in password)  # Join the password list elements into a single string
  lbl.config(text=y)  # Update the label text with the generated password


root = Tk()  # Create the main window for the GUI application
root.title("PASSWORD GENERATOR")  # Set the title of the window
root.geometry("250x200")  # Set the size of the window (250 pixels wide by 200 pixels tall)

btn = Button(root, text="Generate Password", command=generate_password)  # Create a button with text and functionality
btn.grid(row=2, column=2)  # Position the button in the grid layout (row 2, column 2)

lbl = Label(root, font=("times", 15, "bold"))  # Create a label with font properties
lbl.grid(row=4, column=2)  # Position the label in the grid layout (row 4, column 2)

root.mainloop()  # Start the event loop for the GUI application
