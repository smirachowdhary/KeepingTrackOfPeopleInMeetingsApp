import tkinter as tk
from tkinter import *
import student
import studentList
# import Setting

s1 = student.Student()
# s2 = Setting.settings()

window = tk.Tk(className = "My Program")

nameLbl = tk.Label(text = "Selected Name:")
nameLbl.pack()

s1.get_random_name()
showNameLbl = tk.Label(text = s1.get_current_name())
showNameLbl.pack()

listsFrame = tk.Frame()

sl1 = studentList.StudentList(listsFrame,"Present", s1, showNameLbl, "p")
sl2 = studentList.StudentList(listsFrame,"Absent", s1, showNameLbl, "a")
sl3 = studentList.StudentList(listsFrame,"Needs Attention", s1, showNameLbl, "n")

listsFrame.pack()

window.mainloop()