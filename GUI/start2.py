import tkinter as tk
from tkinter import *
from tkinter import font
import student
import studentList2
import datetime

# Info color = #cff4fc 
 
s1 = student.Student()

window = tk.Tk()
window.title("PAN Application")
window.configure(bg='#f8f9fa')

meetingFrame = tk.Frame()
meetingLbl = tk.Label(text = "Meeting Name", master = meetingFrame,bg='#f8f9fa', font = "Arial 15")
meetingLbl.pack(side = LEFT)
meetingEntry = tk.Entry(master = meetingFrame,bg='#f8f9fa', font = "Arial 15")
meetingEntry.pack(side = LEFT)
meetingFrame.pack(padx=5, pady=5)

nameLbl = tk.Label(text = "Selected Name:",bg='#f8f9fa', pady=10, padx=10, font="Arial 15")
nameLbl.pack(padx=5, pady=5)

s1.get_random_name()
showNameLbl = tk.Label(
    text = s1.get_current_name().strip(),
    relief = RIDGE,
    font = 'Verdana 36 bold',
    bg = "#d1e7dd",
    fg = "#0f5132")
showNameLbl.pack(padx=5, pady=10, ipadx=20, ipady=10)

listsFrame = tk.Frame(relief=RAISED, bg='#f8f9fa')

sl1 = studentList2.StudentList(listsFrame,"Present", s1, showNameLbl)
sl2 = studentList2.StudentList(listsFrame,"Absent", s1, showNameLbl)
sl3 = studentList2.StudentList(listsFrame,"Needs Attention", s1, showNameLbl)

listsFrame.pack()

def save_handler(event):
    nameP1 = meetingEntry.get().strip()
    if not nameP1:
        nameP1 = "Meeting"
    d1 = datetime.datetime.now()
    file_name = f"{nameP1}_Notes_{d1.year}_{d1.month}_{d1.day}_{d1.hour}.txt"
    output_file = s1.get_data_dir() + "\\" + file_name

    target = open(output_file , "w")
    target.truncate()

    meeting = meetingEntry.get()

    target.write(f"{meeting} Meeting Info:\n\n\n\n")
    target.write(sl1.get_all_names())
    target.write(sl2.get_all_names())
    target.write(sl3.get_all_names())

    infoLabel["text"] += "\n" + "Your data is now at:" + "\n" + output_file

footerFrame = tk.Frame()
save_btn = tk.Button(text = "Save",bg='#0d6efd', fg = "#fff", font = "Arial 15", master=footerFrame)
save_btn.bind("<Button-1>", save_handler)
save_btn.pack(padx=5, pady=5, side = RIGHT)

infoLabel = tk.Label(
    text = s1.get_input_filename(),
    font = 'Arial 15',
    bg = "#cff4fc",
    fg = "#055160",
    master=footerFrame)
infoLabel.pack(padx=5, pady=10, ipadx=20, ipady=10)

footerFrame.pack(side=BOTTOM, padx=5, pady=10)

window.mainloop()