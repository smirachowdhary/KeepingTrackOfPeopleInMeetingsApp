from tkinter import *

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master=master
        self.master.title("Application")
        self.pack(fill=BOTH, expand=True)

        self.headerFrame = Frame(self)
        self.headinglbl = self.regularLabel(frame=self.headerFrame, text="Welcome", side=None)
        self.headerFrame.pack(padx=5, pady=10)

        self.deatilsFrame = Frame(self, relief=RIDGE, borderwidth=1)
        self.lbl1 = Label(self.deatilsFrame, text="Title")
        self.lbl1.pack(side=LEFT, padx=5, pady=5)
        self.entry1 = Entry(self.deatilsFrame)
        self.entry1.pack(fill=X, padx=5, expand=True)
        self.deatilsFrame.pack(padx=5, pady=10,fill=BOTH, expand=True)

        self.footerFrame = Frame(self)
        self.savebtn = self.regularbutton(frame=self.footerFrame, text="Save", side=RIGHT)
        self.footerFrame.pack(side=RIGHT, padx=5, pady=10)
    
    def regularLabel(self, frame, text, side):
        lbl = Label(master=frame, text=text, font="Arial 15",fg="#000000")
        lbl.pack(side=side, padx=5, pady=5)

    def regularbutton(self, frame, text, side):
        lbl = Button(master=frame, text=text, font="Arial 12 bold",fg="#ffffff", bg="#0d6efd")
        lbl.pack(side=side, padx=5, pady=5)

        
rootwindow = Tk()
myapp = App(rootwindow)
myapp.mainloop()