import tkinter as tk

def on_enter(event):
    button.config(text="Hovering!")

def on_leave(event):
    button.config(text="Click Me!")

root = tk.Tk()
button = tk.Button(root, text="Click Me!")
button.pack()

button.bind("<Enter>", on_enter)
button.bind("<Leave>", on_leave)

root.mainloop()
