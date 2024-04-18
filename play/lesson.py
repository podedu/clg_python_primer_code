def check_palindrome(self):
        text = self.entry_1.get()
        if is_palindrome(text):
            self.result_label.config(text="Well done! It's a palindrome!", fg="#e70d0d")
        else:
            self.result_label.config(text="Doh! It's not a palindrome.", fg="#800080")
