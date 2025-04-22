import tkinter as tk
import random

root = tk.Tk()
root.title("dice roller")
root.geometry("300x200")

result_label = tk.Label(root, bg="white", text="", font=("Helvetica", 20), width=20, borderwidth=2, relief="solid")
result_label.pack(pady=20, padx=0)

def roll_d20():
    roll = random.uniform(0, 20)
    result_label.config(text=roll)
    result_label.config(bg="red")

def roll_d6():
    roll = random.uniform(1, 6)
    result_label.config(text=roll)
    result_label.config(bg="blue")

d20_roll_button = tk.Button(root, text="roll d20", command=roll_d20)
d20_roll_button.pack()

d6_roll_button = tk.Button(root, text="roll d6", command=roll_d6)
d6_roll_button.pack()


root.mainloop()