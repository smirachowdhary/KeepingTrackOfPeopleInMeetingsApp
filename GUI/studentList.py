import tkinter as tk
from tkinter import *
import student

class StudentList:
    prossesedList = []

    def __init__(self, parentFrame, title, sObj, showNameLbl, typeOfBtn):
        self.typeOfBtn = typeOfBtn
        self.sObj = sObj
        self.showNameLbl = showNameLbl
        self.students = []
        
        if typeOfBtn == "p":
            childFrame = tk.Frame(master = parentFrame)
            btn = tk.Button(text = title, master = childFrame)
            btn.bind("<Button-1>", self.handler)
            btn.pack()
            titleLbl = tk.Label(text = title, master = childFrame)
            titleLbl.pack()
            self.pLbl = tk.Label(text = "", master = childFrame)
            self.pLbl.pack()
            childFrame.pack(side = LEFT)
        
        if typeOfBtn == "a":
            childFrame = tk.Frame(master = parentFrame)
            btn = tk.Button(text = title, master = childFrame)
            btn.bind("<Button-1>", self.handler)
            btn.pack()
            titleLbl = tk.Label(text = title, master = childFrame)
            titleLbl.pack()
            self.aLbl = tk.Label(text = "", master = childFrame)
            self.aLbl.pack()
            childFrame.pack(side = LEFT)
        
        if typeOfBtn == "n":
            childFrame = tk.Frame(master = parentFrame)
            btn = tk.Button(text = title, master = childFrame)
            btn.bind("<Button-1>", self.handler)
            btn.pack()
            titleLbl = tk.Label(text = title, master = childFrame)
            titleLbl.pack()
            self.nLbl = tk.Label(text = "", master = childFrame)
            self.nLbl.pack()
            childFrame.pack(side = LEFT)
    
    def handler(self, event=None):
        if len(StudentList.prossesedList) == 26:
            doneLbl = tk.Label(text = "There are no more names left.")
            doneLbl.pack()
        else:
            if self.typeOfBtn == "p":
                self.students.append(self.sObj.get_current_name())
                self.pLbl["text"] = "\n".join(self.students)
                self.sObj.get_random_name()
                self.showNameLbl["text"] = self.sObj.get_current_name()
            
            if self.typeOfBtn == "a":
                self.students.append(self.sObj.get_current_name())
                self.aLbl["text"] = "\n".join(self.students)
                self.sObj.get_random_name()
                self.showNameLbl["text"] = self.sObj.get_current_name()
            
            if self.typeOfBtn == "n":
                self.students.append(self.sObj.get_current_name())
                self.nLbl["text"] = "\n".join(self.students)
                self.sObj.get_random_name()
                self.showNameLbl["text"] = self.sObj.get_current_name()