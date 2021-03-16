import tkinter as tk
from tkinter import *
import student

s1 = student.Student()

window = tk.Tk(className = "My Program")

nameLbl = tk.Label(text = "Selected Name:")
nameLbl.pack()

tmp=""
for i in range(0,25):
    tmp += s1.get_random_name() + "\n "

showNameLbl = tk.Label(text = tmp,fg="blue",bg="#66FFCC", width=50)
showNameLbl.pack()

window.mainloop()