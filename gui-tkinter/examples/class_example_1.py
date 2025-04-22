import tkinter as tk
import random

root = tk.Tk()
root.title("dice roller")
root.geometry("300x200")

result_label = tk.Label(root, text="", font=("Helvetica", 48), width=2, borderwidth=2, relief="solid")
result_label.pack(pady=20, padx=20)

def roll_d20():
    roll = random.randint(1, 20)
    result_label.config(text=roll)

def roll_d6():
    roll = random.randint(1, 6)
    result_label.config(text=roll)

d20_roll_button = tk.Button(root, text="roll d20", command=roll_d20)
d20_roll_button.pack()

d6_roll_button = tk.Button(root, text="roll d6", command=roll_d6)
d6_roll_button.pack()


root.mainloop()