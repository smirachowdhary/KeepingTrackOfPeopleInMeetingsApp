import random

dictionary  =  {
        1   : "LEONIS",
        2   : "BRIAN",
        3   : "TYLER",
        4   : "RACHEL",
        5   : "SMIRA",
        6   : "ISAAC",
        7   : "THOMAS",
        8   : "ALLISON",
        9   : "YANA",
        10  : "SAMUEL",
        11  : "AIDAN",
        12  : "NATALIE",
        13  : "ALI",
        14  : "JONATHAN",
        15  : "AZIZA",
        16  : "MICHAELA",
        17  : "ALISTAIR",
        18  : "PARAMEE",
        19  : "EVELYN",
        20  : "MAYA",
        21  : "ISABEL",
        22  : "ARIA",
        23  : "XAVIER",
        24  : "ALYSSA",
        25  : "NATHAN",
        26  : "DARREN",
}

i = 0
while i < 26:
    random_number = random.randint(1,26-i)
    print(dictionary[random_number])
    j = 0
    while j < 26:
        if j+1 == random_number:
                p = input("Present and answered question:")
                if p == "Y" or p == "y":
                        student = dictionary[random_number]
                        dictionary[random_number] = "present and has answered question."
                        print(student, "is", dictionary[random_number])
                        j+=1
                        continue
                a = input("Absent:")
                if a == "Y" or a == "y":
                        student = dictionary[random_number]
                        dictionary[random_number] = "absent."
                        print(student, "is", dictionary[random_number])
                        j+=1
                        continue
                n = input("Here but not here:")
                if n == "Y" or n == "y":
                        student = dictionary[random_number]
                        dictionary[random_number] = "here but not here."
                        print(student, "is", dictionary[random_number])
        j+=1
    i+=1