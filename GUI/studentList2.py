import tkinter as tk
from tkinter import *
import student

class StudentList:

    def __init__(self, parentFrame, title, studentObj, showNameLbl):
        self.studentObj = studentObj
        self.showNameLbl = showNameLbl
        self.students = []

        self.childFrame = tk.Frame(master = parentFrame)
        self.btn = tk.Button(text = title, master = self.childFrame)
        self.btn.bind("<Button-1>", self.update_list)
        self.btn.pack()
        self.titleLbl = tk.Label(text = title, master = self.childFrame)
        self.titleLbl.pack()
        self.Lbl = tk.Label(text = "", master = self.childFrame)
        self.Lbl.pack()
        self.childFrame.pack(side = LEFT)

    def update_list(self,event=None):
        self.students.append(self.studentObj.get_current_name())
        self.Lbl["text"] = "\n".join(self.students)
        self.studentObj.get_random_name()
        self.showNameLbl["text"] = self.studentObj.get_current_name()

    def get_all_names(self):
        temp = self.titleLbl.cget("text") + "\n"
        temp += "\n".join(self.students)
        temp += "\n\n"
        return temp

