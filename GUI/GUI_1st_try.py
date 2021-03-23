import tkinter as tk
from tkinter import *
import random

present_list = []
absent_list = []
needs_attention_list = []
name_list = ["LEONIS", "BRIAN", "TYLER", "RACHEL", "SMIRA", "ISAAC", "THOMAS", "ALLISON", "YANA", "SAMUEL",
 "AIDAN", "NATALIE", "ALI", "JONATHAN", "AZIZA", "MICHAELA", "ALISTAIR", "PARAMEE", "EVELYN", "MAYA", "ISABEL",
 "ARIA", "XAVIER", "ALYSSA", "NATHAN", "DARREN"]

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

def create_buttons(text, handler):
    name = tk.Button(text = text, master = BtnFrame)
    name.bind("<Button-1>", handler)
    name.pack(side = LEFT)

create_buttons("P", pBtn_Handler)
create_buttons("A", aBtn_Handler)
create_buttons("N", nBtn_Handler)

BtnFrame.pack()

listsFrame = tk.Frame()

pLbl = tk.Label(text = "Present:\n", master = listsFrame)
pLbl.pack(side = LEFT)

aLbl = tk.Label(text = "Absent:\n", master = listsFrame)
aLbl.pack(side = LEFT)

nLbl = tk.Label(text = "Needs Attention:\n", master = listsFrame)
nLbl.pack(side = LEFT)

listsFrame.pack()

window.mainloop()

print("end")