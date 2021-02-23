import random
from sys import argv
from os.path import exists

info_list = []
processed_list=[]
name_list = ["LEONIS", "BRIAN", "TYLER", "RACHEL", "SMIRA", "ISAAC", "THOMAS", "ALLISON", "YANA", "SAMUEL",
 "AIDAN", "NATALIE", "ALI", "JONATHAN", "AZIZA", "MICHAELA", "ALISTAIR", "PARAMEE", "EVELYN", "MAYA", "ISABEL",
 "ARIA", "XAVIER", "ALYSSA", "NATHAN", "DARREN"]
go_on = True
while go_on:
    random_number = random.randint(0,len(name_list)-1)
    student_name = name_list[random_number]
    if len(processed_list)-1 == 25:
        print(f"""
        For this meeting, all names have been exhausted.
        There is the info:
        """)
        i = 0
        while i < 26:
            print(f"{info_list[i][0]} is {info_list[i][1]}.")
            i+=1
        break
    
    if student_name in processed_list:
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
        info_list.append(student_info)
        processed_list.append(student_name)
    
    elif  teacher_input == "s":
        print(info_list)
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

dectory = input("Enter a path to a new file here(word prefrebly).")
print("Opening the file...")
target = open(dectory + ".txt", "w")

print("Clearing everything that is in the new file. Goodbye.")
target.truncate()

print("I am going to write the students' info in the new file.")

meeting = input("What meeting is this?")
target.write(f"{meeting} Meeting Info:\n\n\n\n")

i=0
while i < len(info_list):
    target.write(f"{info_list[i][0]} is {info_list[i][1]}.")
    target.write("\n")
    i+=1

print("And fianally, we close it.")
target.close()

print("It is done. Open that file to see!")