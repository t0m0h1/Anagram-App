import tkinter as tk
from tkinter import messagebox
import string

# Function to check if two strings are anagrams
def are_anagrams(str1, str2):
    # Clean the strings: convert to lowercase, remove spaces and punctuation
    clean_str1 = ''.join(char.lower() for char in str1 if char in string.ascii_letters)
    clean_str2 = ''.join(char.lower() for char in str2 if char in string.ascii_letters)
    
    # Check if sorted versions of cleaned strings are equal
    return sorted(clean_str1) == sorted(clean_str2)

# Function triggered when the button is pressed
def check_anagram():
    word1 = entry1.get()
    word2 = entry2.get()
    
    if are_anagrams(word1, word2):
        result_label.config(text="Anagram: Yes!", fg="green")
    else:
        result_label.config(text="Anagram: No", fg="red")

# Initialize the main window
root = tk.Tk()
root.title("Anagram Checker")
root.geometry("300x200")

# Labels and entry boxes for user input
label1 = tk.Label(root, text="Enter first word:")
label1.pack(pady=10)

entry1 = tk.Entry(root, width=30)
entry1.pack()

label2 = tk.Label(root, text="Enter second word:")
label2.pack(pady=10)

entry2 = tk.Entry(root, width=30)
entry2.pack()

# Button to trigger the anagram check
check_button = tk.Button(root, text="Check Anagram", command=check_anagram)
check_button.pack(pady=20)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
