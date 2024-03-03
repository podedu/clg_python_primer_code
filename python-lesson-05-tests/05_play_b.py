# Palindrome checker

word = input("Hi, type in a word or phrase and I will tell you if it is a palindrome: ").lower

print(word)
alphabet_only = ""
for char in word:
    if char.isalpha():
        alphabet_only += char

 

if alphabet_only == alphabet_only[::-1]:
    print("Well done! Your word or phrase is a palindrome.")
else:
    print("Your word or phrase is not a palindrome, better luck next time.")



     
   


   