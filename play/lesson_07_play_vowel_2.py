def vowel_counting(name):
    vowel_count = 0    
    
    for char in name:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
            
    print(f"My name is {name}. My name contains {vowel_count} vowels.")   

vowel_counting("Pauline O'Donoghue")

