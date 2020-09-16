import tkinter as tk
import time
import SSP

window = tk.Tk()

picks = ["Stein", "Schere","Papier"]

welcome = tk.Message(window,
                  #  width = 500,
                    text = "Schere, Stein, Papier Action - whoop!")
welcome.grid(row=0, column = 1)


schere = tk.Button(text = "Schere")
schere.grid(row = 1, column = 0)

stein = tk.Button(text = "Stein")
stein.grid(row = 1, column = 1)

papier = tk.Button(text = "Papier")
papier.grid(row = 1, column = 2)




window.mainloop()