import tkinter as tk

root = tk.Tk()
root.title("Phone Dialer")
root.geometry("300x400")

# dialed number string
dialed_number = tk.StringVar()

# display number text on top
display = tk.Entry(root, textvariable=dialed_number, font=("Helvetica", 24), justify="right", bd=5)
display.grid(row=0, column=0, columnspan=3, padx=10, pady=20, sticky="nsew")

buttons = [
    '1', '2', '3',
    '4', '5', '6',
    '7', '8', '9',
    '*', '0', '#'
]

def press(key):
    current = dialed_number.get()
    dialed_number.set(current + key)

# create buttons
for index, label in enumerate(buttons):
    row = (index // 3) + 1
    col = index % 3
    button = tk.Button(root, text=label, font=("Helvetica", 20), command=lambda l=label: press(l))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

# span grids 
for i in range(4):
    root.rowconfigure(i, weight=1)
for i in range(3):
    root.columnconfigure(i, weight=1)

root.mainloop()