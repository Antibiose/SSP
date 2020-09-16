import tkinter as tk
from time import sleep as sleep

window = tk.Tk()

welcome_message = tk.Label(text = "SCHERE - STEIN - PAPIER")
sleep = 0.5
second_message = tk.Label(text = "Hype.")


schere = tk.Button(text = "Schere")
schere.grid(row = 0, column = 0)

stein = tk.Button(text = "Stein")
stein.grid(row = 0, column = 1)

papier = tk.Button(text = "Papier")
papier.grid(row = 0, column = 2)




window.mainloop()