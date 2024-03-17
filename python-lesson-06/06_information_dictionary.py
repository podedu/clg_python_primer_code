pauline_information = {"occupation": "public servant", "favourite food": "chocolate", "height in cm": 165, "current pet": "Monty the cat",  "most likely cause of death": "Monty the cat, AKA \"Murder Mittens\""}

pauline_information.update({"hill I will die on": "the Oxford comma"})
pauline_information.pop("occupation")

for key, value in pauline_information.items():
    print (f"My {key} is {value}.")

pauline_information.clear()
