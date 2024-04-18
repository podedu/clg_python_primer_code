import tkinter as tk
from palindrome_checker import is_palindrome


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Palindrome Checker")
        self.label_1 = tk.Label(self, text="Enter a word or phrase:", font=("Times", 16), fg="#000000", bg="#31906e")
        self.label_1.pack()
        self.entry_1 = tk.Entry(self, font=("Courier", 16), fg="#072a75", bg="#b2ecd9")
        self.entry_1.pack()
        self.result_label = tk.Label(self, fg="#000000", bg="#31906e")
        self.result_label.pack()
        self.btn = tk.Button(self, text="Check", command=self.check_palindrome, bg="#dd5c9b")
        self.btn.pack()

    def check_palindrome(self):
        text = self.entry_1.get()
        if is_palindrome(text):
            self.result_label.config(text="Well done! It's a palindrome!", fg="#e70d0d")
        else:
            self.result_label.config(text="Doh! It's not a palindrome.", fg="#800080")

if __name__ == "__main__":
    root = Root()
    root ["bg"] = "#31906e"
    root.geometry("400x200")
    root.mainloop()