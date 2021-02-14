import random

students_info = []
students_name = ["LEONIS", "BRIAN", "TYLER", "RACHEL", "SMIRA", "ISAAC", "THOMAS", "ALLISON", "YANA", "SAMUEL",
 "AIDAN", "NATALIE", "ALI", "JONATHAN", "AZIZA", "MICHAELA", "ALISTAIR", "PARAMEE", "EVELYN", "MAYA", "ISABEL",
 "ARIA", "XAVIER", "ALYSSA", "NATHAN", "DARREN"]
go_on = True
while go_on:
    random_number = random.randint(0,len(students_name)-1)
    print(students_name[random_number])
    student_name = students_name[random_number]
    teacher_input = input("""
    Present and answered question:
    Absent:
    Not attentive:
    Show:
    Exit:
    """)
    if  teacher_input == "p" or teacher_input == "P" or  teacher_input == "a" or  teacher_input == "A" or  teacher_input == "n" or  teacher_input == "N":
        student_info = [student_name,  teacher_input]
        students_info.append(student_info)
    if  teacher_input == "S" or  teacher_input == "s":
        print(students_info)
        print("Do you want to continue?")
        temp_go_on = input()
        if temp_go_on == "y" or temp_go_on == "Y":
            go_on = True
        else:
            go_on = False
    if teacher_input == "e" or teacher_input == "E":
        go_on = False
