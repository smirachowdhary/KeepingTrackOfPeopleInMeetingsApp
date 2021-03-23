import random

students_info = []
students_processed=[]
students_name = ["LEONIS", "BRIAN", "TYLER", "RACHEL", "SMIRA", "ISAAC", "THOMAS", "ALLISON", "YANA", "SAMUEL",
 "AIDAN", "NATALIE", "ALI", "JONATHAN", "AZIZA", "MICHAELA", "ALISTAIR", "PARAMEE", "EVELYN", "MAYA", "ISABEL",
 "ARIA", "XAVIER", "ALYSSA", "NATHAN", "DARREN"]
go_on = True
while go_on:
    random_number = random.randint(0,len(students_name)-1)
    student_name = students_name[random_number]
    if len(students_name)-1 == len(students_info)-1:
        print(f"""
        For this meeting, all names have been exhausted.
        There is the info:
        """)
        i = 0
        while i < 26:
            print(f"{students_info[i][0]} is {students_info[i][1]}.")
    if student_name in students_processed:
        continue

    print(student_name)
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
        students_processed.append(student_name)
    elif  teacher_input == "s":
        print(students_info)
        temp_go_on = input("Do you want to continue?")
        temp_go_on = temp_go_on.lower()
        if temp_go_on == "y":
            go_on = True
        else:
            go_on = False
    elif teacher_input == "e":
        go_on = False
    else:
        print("You did not answer with PANSE, so try again. This try will not be shown.")
        go_on = True