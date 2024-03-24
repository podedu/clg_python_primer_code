def vowel_counting(name):
    # Convert the name to uppercase to make comparison case-insensitive
    name = name.upper()
    
    # Initialize a variable to count vowels
    vowel_count = 0
    
    # Loop through each character in the name
    for char in name:
        # Check if the character is a vowel
        if char in ['A', 'E', 'I', 'O', 'U']:
            # If it's a vowel, increment the vowel count
            vowel_count += 1
    
    # Print the name and the vowel count
    print(f"My name is {name} and it contains {vowel_count} vowels.")

vowel_counting("Pauline O'Donoghue")