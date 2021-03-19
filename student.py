import random

class Student:
    name_list = []
    random_end = 0
    current_name = ""
    def __init__(self):
        Student.name_list = ["LEONIS", "BRIAN", "TYLER", "RACHEL", "SMIRA", "ISAAC", "THOMAS", "ALLISON", "YANA", "SAMUEL",
        "AIDAN", "NATALIE", "ALI", "JONATHAN", "AZIZA", "MICHAELA", "ALISTAIR", "PARAMEE", "EVELYN", "MAYA", "ISABEL",
        "ARIA", "XAVIER", "ALYSSA", "NATHAN", "DARREN"]
        Student.random_end = len(Student.name_list)-1
    def get_random_name(self):
        random_number = random.randint(0,Student.random_end)
        selectedName = Student.name_list[random_number]
        Student.name_list[random_number] = Student.name_list[Student.random_end]
        Student.name_list[Student.random_end] = selectedName
        Student.random_end -= 1
        Student.current_name = selectedName
        return selectedName
    def get_current_name(self):
        return Student.current_name

    # def get_teacher_input(self):
        
    # def update_to_list(self):
    
    # def add_to_file(self):