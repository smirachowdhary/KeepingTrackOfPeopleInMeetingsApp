import tkinter as tk
from tkinter import *
from tkinter import font
import student
import studentList2
    

s1 = student.Student()

window = tk.Tk(className = "My Program2")

nameLbl = tk.Label(text = "Selected Name:")
nameLbl.pack()

s1.get_random_name()
showNameLbl = tk.Label(
    text = s1.get_current_name(),
    justify= CENTER,
    width=100,
    height=2,
    bg="black",
    fg="white",
    relief = GROOVE)
showNameLbl.pack()

listsFrame = tk.Frame(relief=RAISED)

sl1 = studentList2.StudentList(listsFrame,"Present", s1, showNameLbl)
sl2 = studentList2.StudentList(listsFrame,"Absent", s1, showNameLbl)
sl3 = studentList2.StudentList(listsFrame,"Needs Attention", s1, showNameLbl)

listsFrame.pack()

def save_handler(event):
    dectory = dectoryEntry.get()

    target = open(dectory + ".txt", "w")
    target.truncate()

    meeting = meetingEntry.get()

    target.write(f"{meeting} Meeting Info:\n\n\n\n")
    target.write(sl1.get_all_names())
    target.write(sl2.get_all_names())
    target.write(sl3.get_all_names())

save_btn = tk.Button(text = "Save")
save_btn.bind("<Button-1>", save_handler)
save_btn.pack()

meeting_nameFrame = tk.Frame()
meetingLbl = tk.Label(text = "What meeting is this?", master = meeting_nameFrame)
meetingLbl.pack()
meetingEntry = tk.Entry(master = meeting_nameFrame)
meetingEntry.pack()
meeting_nameFrame.pack(side = LEFT)

dectoryFrame = tk.Frame()
dectoryLbl = tk.Label(text = "Enter a new file's name here:", master = dectoryFrame)
dectoryLbl.pack()
dectoryEntry = tk.Entry(master = dectoryFrame)
dectoryEntry.pack()
dectoryFrame.pack(side = LEFT)

window.mainloop()