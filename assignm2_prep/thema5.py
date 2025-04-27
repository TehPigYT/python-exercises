import tkinter as tk

root = tk.Tk()
root.title("Color Picker")

def change_color(color):
    root.configure(bg=color)

red_button = tk.Button(root, text="R", command=lambda: change_color("red"))
red_button.pack()

green_button = tk.Button(root, text="G", command=lambda: change_color("green"))
green_button.pack()

blue_button = tk.Button(root, text="B", command=lambda: change_color("blue"))
blue_button.pack()

root.mainloop()