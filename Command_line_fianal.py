import random

students_info = []
students_name = ["LEONIS", "BRIAN", "TYLER", "RACHEL", "SMIRA", "ISAAC", "THOMAS", "ALLISON", "YANA", "SAMUEL",
 "AIDAN", "NATALIE", "ALI", "JONATHAN", "AZIZA", "MICHAELA", "ALISTAIR", "PARAMEE", "EVELYN", "MAYA", "ISABEL",
 "ARIA", "XAVIER", "ALYSSA", "NATHAN", "DARREN"]
go_on = True
while go_on:
    random_number = random.randint(0,len(students_name)-1)
    if random_number in students_info:
        continue
    else:
        print(students_name[random_number])
        student_name = students_name[random_number]
        teacher_input = input("""
        Present and answered question:
        Absent:
        Not attentive:
        Show:
        Exit:
        """)
        teacher_input = teacher_input.lower()
        if  teacher_input == "p" or  teacher_input == "a" or  teacher_input == "n":
            student_info = [student_name,  teacher_input]
            students_info.append(student_info)
            temp_go_on = input("Do you want to continue?")
            temp_go_on = temp_go_on.lower()
            if temp_go_on == "y":
                go_on = True
            else:
                go_on = False
        if  teacher_input == "s":
            print(students_info)
            temp_go_on = input("Do you want to continue?")
            temp_go_on = temp_go_on.lower()
            if temp_go_on == "y":
                go_on = True
            else:
                go_on = False
        if teacher_input == "e":
            go_on = False
        else:
            go_on = True