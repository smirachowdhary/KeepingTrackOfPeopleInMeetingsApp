import tkinter as tk
from tkinter import *
import student
import studentList2

class saveBtn:

    def save_handler(self, event=None):
        s1 = studentList2.StudentList()

        dectoryFrame = tk.Frame()
        dectoryLbl = tk.Label(text = "Enter a new file's name here:", master = dectoryFrame)
        dectoryLbl.pack()
        dectoryEntry = tk.Entry(master = dectoryFrame)
        dectoryEntry.pack()
        dectoryFrame.pack(side = LEFT)

        target = open(dectory + ".txt", "w")
        target.truncate()

        meeting_nameFrame = tk.Frame()
        meetingLbl = tk.Label(text = "What meeting is this?", master = meeting_nameFrame)
        meetingLbl.pack()
        meetingEntry = tk.Entry(master = meeting_nameFrame)
        meetingEntry.pack()
        meeting_nameFrame.pack(side = LEFT)

        meeting = meetingEntry.get()

        target.write(f"{meeting} Meeting Info:\n\n\n\n")

        s1.get_all_names()

    def create_save_btn(self):
        save_btn = tk.Button(text = "Save")
        save_btn.bind("<Button-1>", self.save_handler)
        save_btn.pack()