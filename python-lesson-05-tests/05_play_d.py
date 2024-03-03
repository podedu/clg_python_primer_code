# Palindrome checker

word = input("Hi, type in a word or phrase and I will tell you if it is a palindrome: ").lower()
print(word)

word = "".join(x for x in word if x.isalpha())
if word == word[::-1]:
    print("Well done! Your word or phrase is a palindrome.")
else:
    print("Your word or phrase is not a palindrome, better luck next time.")    


    try_again = input("Would you like to try again? Type yes or no.").lower()
while try_again ==
    if try_again == "yes":
        print(word)
        continue
    elif try_again == "no":
        break
    else:
        print("Please type either yes or no.")

        






     
   


   