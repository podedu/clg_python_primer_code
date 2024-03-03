word = input("Hi, type in a word or phrase and I will tell you if it is a palindrome: ")
letters_in_word = word.lower()
print(letters_in_word)
letters_in_word_list = list(letters_in_word)
print(letters_in_word_list)
letters_in_word_list.reverse()
print(letters_in_word_list)
string_from_list = "".join(letters_in_word_list)
print(string_from_list)
if string_from_list == letters_in_word:
    print("Well done! Your word or phrase is a palindrome.")
else:
    print("Your word or phrase is not a palindrome, better luck next time.")    

