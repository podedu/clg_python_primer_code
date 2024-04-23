import tkinter as tk
import random


coins = ["Heads", "Tails"]

def generate_label():
    string1=random.choice(coins)
    string2=random.choice(coins)

    string=string1+" and "+string2

    font_size = 14  
    font_color = "#174754" 
    font = ("Helvetica", font_size, "bold") 

    label = tk.Label(text=string, font=font, fg=font_color)
    x = random.randrange(600)
    y = random.randrange(600)
    label.place(x=x, y=y)

root = tk.Tk()
root.title("Two-up")
root.geometry("1000x1000")
root ["bg"] = "#92C8D7"

explanation_label = tk.Label(root, text="Click 'Play' to have a game of Two-up", font=("Courier", 16), fg="#000000", bg="#31906e")
explanation_label.pack()

generate_label()

btn = tk.Button(root, text="Play", command = generate_label)
btn.pack()

root.mainloop()
