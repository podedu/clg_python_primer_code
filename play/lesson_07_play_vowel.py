def vowel_counting(user_input):
    total = 0
    vowels = ["a", "e", "i", "o", "u"]

user_input = input("Hi, Type in your full name and I will tell you how many vowels it contains: ").lower()

for char in user_input:
    if char in vowels:
        total += 1



print(f"Your name is {user_input}. It contains {count} vowels.")        