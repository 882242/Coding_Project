#____________________________________________________________________________________
#   Purpose: Create a student list that can add, remove, and modify things in an array
#   Author: Felix       Date: March 19, 2025     Class: ICS3C    Last Updated:
#____________________________________________________________________________________



# i made a class to idetify them for their major name and age
class students_info:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

#this is the list of students
students = [
    students_info("John", 15, "Computer Science"),
    students_info("Jane", 12, "Engineering"),
    students_info("Bob", 16, "Business Administration"),
    students_info("Alice", 14, "Computer Science")]

def _student_list(): #this is just a function to print the list of students
    for student in students:
        print(student.name, student.age, student.major)

print("you can use commands add, find, remove, print and modify")

while True:
    Operator = input(" ") #This is our operator that can find, print, add, remove, and modify students
    if Operator == "print": #if operator is print it will print
        _student_list()
    elif Operator == "find": #if operator is find it will ask yo this vvv
        sectionFinder = input("What section are you looking for? (name/age/major) : ")
        if sectionFinder == "name": #if it is the name it will print all students, and it's student_info
            name = input("What is the name? : ")
            for student in students:
                if student.name == name:
                    print(student.name, student.age, student.major)
        elif sectionFinder == "age": #this does the same but with age
            age = int(input("What is the age? : "))
            for student in students:
                if student.age == age:
                    print(student.name, student.age, student.major)
        elif sectionFinder == "major": #and this with it's major
            major = input("What is the major? : ")
            for student in students:
                if student.major == major:
                    print(student.name, student.age, student.major)
    elif Operator == "add": #if the operator is add, the it will ask name,age,and major for it to add in students
        addingname = input("What is the name of the new student? : ")
        addingage = int(input("What is the age of the new student? : "))
        addingmajor = input("What is the major of the new student? : ")
        students.append(students_info(addingname, addingage, addingmajor))
        print(f"Student {addingname} added successfully!")
        continue
    elif Operator == "remove": #if the operator is remove it will remove the student by name
        removing = input("Who are we removing? (precise spelling) : ")
        for student in students:
            if student.name == removing:
                students.remove(student)
                print(f"Student {removing} removed successfully!")
    elif Operator == "modify": #this will modify a students_info and you can change the name age and major
        modifying = input("Who are we modifying? (precise spelling) : ")
        for student in students:
            if student.name == modifying:
                index = students.index(student)
                modifyingName = input("What are we changing the name to? : ")
                modifyingAge = int(input("What are we changing the age to? : "))
                modifyingMajor = input("What are we changing the major to? : ")
                students[index] = students_info(modifyingName, modifyingAge, modifyingMajor)
                print(f"Student {modifying} modified successfully!")


