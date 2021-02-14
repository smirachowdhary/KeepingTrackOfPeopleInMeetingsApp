import random

students_status = []
students_name = ["LEONIS", "BRIAN", "TYLER", "RACHEL", "SMIRA", "ISAAC", "THOMAS", "ALLISON", "YANA", "SAMUEL",
 "AIDAN", "NATALIE", "ALI", "JONATHAN", "AZIZA", "MICHAELA", "ALISTAIR", "PARAMEE", "EVELYN", "MAYA", "ISABEL",
 "ARIA", "XAVIER", "ALYSSA", "NATHAN", "DARREN",
]
students_info = []

i = 0
while i < 26:
    random_number = random.randint(1,26)
    print(students_name[random_number])
    j = 0
    while j < 26:
        if j+1 == random_number:
                student_status = input("""
                Present and answered question:
                Absent:
                Not attentive:
                """)
                students_status.append(student_status)
                students_info.append(students_status)
                students_info.append(students_name)
        j+=1
    i+=1

print(students_info)