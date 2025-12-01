import tkinter as tk
from tkinter import *

def Game_active():
    print("This is FiSim. I game to help kids understand money better.")

window= tk.Tk()
window.title("FiSim")

window.geometry("400x300")
window.config(background="Cyan")

btn = tk.Button(window, text="Click the Button to Start your Adventure!", command=Game_active)
btn.pack()

window.mainloop()
