# Palindrome checker

word = input("Hi, type in a word or phrase and I will tell you if it is a palindrome: ").lower()
alphabet_only = ""
for char in word:
    if char.isalpha():
        alphabet_only += char

(alphabet_only == alphabet_only[::-1]):
    print("Well done! You have written a palindrome.")
else:
    print("You have not written a palindrome. ")

