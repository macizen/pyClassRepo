import tkinter as tk

root = tk.Tk()
root.title("grid layout")
root.geometry("300x300")

for i in range(3):
    for j in range(3):
        btn = tk.Button(root, text="a")
        btn.grid(row=i, column=j, sticky="nsew")

for i in range(3):
    root.rowconfigure(i, weight=1)
    root.columnconfigure(i, weight=1)



root.mainloop()