import tkinter as tk
from tkinter import *
import student
import studentList

s1 = student.Student()

window = tk.Tk(className = "My Program")

nameLbl = tk.Label(text = "Selected Name:")
nameLbl.pack()

s1.get_random_name()
showNameLbl = tk.Label(text = s1.get_current_name())
showNameLbl.pack()

listsFrame = tk.Frame()

sl1 = studentList.StudentList(listsFrame,"Present", s1, showNameLbl)
sl2 = studentList.StudentList(listsFrame,"Absent", s1, showNameLbl)
sl3 = studentList.StudentList(listsFrame,"Needs Attention", s1, showNameLbl)

listsFrame.pack()

window.mainloop()