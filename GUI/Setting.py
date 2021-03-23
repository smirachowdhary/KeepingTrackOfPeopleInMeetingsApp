import tkinter as tk
from tkinter import *
import student
import studentList

class settings():

    def settings_page(self):
        settingsBtn = tk.Button(text = "Back")
        settingsBtn.bind("<Button-1>")
        settingsBtn.pack()

    def settings_handler(event):
        settings_page()
    
    def create_settings_Btn(self):
        SettingsFrame = tk.Frame()
        
        settingsBtn = tk.Button(text = "Settings", master = SettingsFrame)
        settingsBtn.bind("<Button-1>", settings_handler)
        settingsBtn.pack()

        SettingsFrame.pack(side = RIGHT)