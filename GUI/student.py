import tkinter as tk
from tkinter import *
import random
import os

class Student:

    def __init__(self):
        self.name_list = []

        path = "Student_Names"
        os.chdir(path)

        name_file = open("Student_Names" + ".txt", "r")

        for line in name_file:
            self.name_list.append(line)

        self.random_end = len(self.name_list)-1
        self.current_name = ""

    def get_random_name(self):
        if self.random_end < 0 :
            self.current_name = "All students processed"
            return "All students processed"
        random_number = random.randint(0,self.random_end)
        self.current_name = self.name_list[random_number]
        self.name_list[random_number] = self.name_list[self.random_end]
        self.name_list[self.random_end] = self.current_name
        self.random_end -= 1
        return self.current_name

    def get_current_name(self):
        return self.current_name

    def is_list_empty(self):
        return self.random_end < 0