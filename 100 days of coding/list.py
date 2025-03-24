class students:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major


students = [
    students("John", 15, "Computer Science"),
    students("Jane", 12, "Engineering"),
    students("Bob", 16, "Business Administration"),
    students("Alice", 14, "Computer Science")]

for student in students:
    if student.major == "Computer Science":
        print(student.name, student.age)