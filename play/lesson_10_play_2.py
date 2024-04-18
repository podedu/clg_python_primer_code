import tkinter as tk

def is_palindrome(word):
    # Remove spaces and convert to lowercase
    word = word.replace(" ", "").lower()
    # Check if the word is equal to its reverse
    return word == word[::-1]

def check_palindrome():
    word = entry.get()
    if is_palindrome(word):
        result_label.config(text="Palindrome!")
    else:
        result_label.config(text="Not a Palindrome!")

# Create the main window
root = tk.Tk()
root.title("Palindrome Detector")

# Create and place widgets
entry_label = tk.Label(root, text="Enter a word:")
entry_label.pack(pady=5)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

check_button = tk.Button(root, text="Check", command=check_palindrome)
check_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Start the application
root.mainloop()
