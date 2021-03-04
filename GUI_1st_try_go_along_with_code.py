import tkinter as tk
from tkinter import *

window = tk.Tk(className = "Application")

button1 = tk.Button(text="Today's Meetings")
button1.pack(side = LEFT)

button2 = tk.Button(text="Yesterday's Meetings")
button2.pack(side = LEFT)

button3 = tk.Button(text="Tommorrow's Meetings")
button3.pack(side = LEFT)

button4 = tk.Button(text="More Meetings")
button4.pack(side = LEFT)

button5 = tk.Button(text="Add Meeting")
button5.pack(side = LEFT)

window.mainloop()