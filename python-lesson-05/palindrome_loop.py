
def palindrome(user_input):
    cleaned_word = "".join(char.lower() for char in user_input if char.isalpha())
    return cleaned_word == cleaned_word[::-1]

while True:
    user_input = input("Hi, type in a word or phrase and I will tell you if it is a palindrome: ").lower()

    if palindrome(user_input):
        print("Well done! It is a palindrome.")
    else:
        print("Sorry! It is not a palindrome.")

    while True:
        try_again = input("Would you like to try a new word or phrase? Please choose yes or no.").lower()
    
        if try_again == "yes":
            break
        elif try_again == "no":
            print("Goodbye")
            exit()
        else:
            print("Please enter yes or no.")    

