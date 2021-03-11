import tkinter as tk
from tkinter import *

present_list = []
absent_list = []
needs_attention_list = []

def nBtn_Handler(event):
    name = nameTB.get()
    new_line = "\n"
    printing_stuff = new_line + name
    nLbl["text"] += printing_stuff

def aBtn_Handler(event):
    name = nameTB.get()
    new_line = "\n"
    printing_stuff = new_line + name
    aLbl["text"] += printing_stuff

def pBtn_Handler(event):
    name = nameTB.get()
    new_line = "\n"
    printing_stuff = new_line + name
    pLbl["text"] += printing_stuff

window = tk.Tk(className = "My Program")

nameLbl = tk.Label(text = "Selected Name:")
nameLbl.pack()

nameTB = tk.Entry()
nameTB.pack()

BtnFrame = tk.Frame()

pBtn = tk.Button(text = "P", master = BtnFrame)
pBtn.bind("<Button-1>", pBtn_Handler)
pBtn.pack(side = LEFT)

aBtn = tk.Button(text = "A", master = BtnFrame)
aBtn.bind("<Button-1>", aBtn_Handler)
aBtn.pack(side = LEFT)

nBtn = tk.Button(text = "N", master = BtnFrame)
nBtn.bind("<Button-1>", nBtn_Handler)
nBtn.pack(side = LEFT)

BtnFrame.pack()

listsFrame = tk.Frame()

pLbl = tk.Label(text = "Present:\n", master = listsFrame)
pLbl.pack()

aLbl = tk.Label(text = "Absent:\n", master = listsFrame)
aLbl.pack()

nLbl = tk.Label(text = "Needs Attention:\n", master = listsFrame)
nLbl.pack()

listsFrame.pack()

window.mainloop()

print("end")