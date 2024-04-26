class Student:
    
    def __init__(self, name, id, currentClass):
        self.name = name
        self.id = id
        self.currentClass = currentClass
        
    def __repr__(self) -> str:
        return f"Student name: {self.name}, id: {self.id}, class: {self.currentClass}"


class Teacher:
    def __init__(self, name, id, subject):
        self.name = name
        self.id = id
        self.subject = subject
        
    def __repr__(self) -> str:
        return f"Teacher name: {self.name}, id: {self.id}, subject: {self.subject}"


class School:
    
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
        
    def addTeacher(self, name, subject):
        id = len(self.teachers) +101
        teacher = Teacher(name, id, subject)
        self.teachers.append(teacher)

    def studentEnroll(self, name, fee):
        if fee < 6500:
            return f"Sorry {name} !!! Not enough fee, Fee amount is: 6500 BDT."
        else:
            id = len(self.students)+1
            self.students.append(Student(name,id,'C'))
            return f"{name} is enrolled with id: {id}, extra money {fee-6500} BDT."
            
    def __repr__(self) -> str:
        print(f"Welcome to {self.name}")
        print("----------------------------------")
        print("_________Our Teachers_________")
        for teacher in self.teachers:
            print(teacher)
        print("_________Our Students_________")
        for student in self.students:
            print(student)
            
        return ""
            

# ruma = Student("Ruma Bibi", 40, 6)
# shahid = Teacher("Shahid Afridi", 378, "Pyhton")
# print(ruma)
# print(shahid)

phitron = School("Phitron")

phitron.addTeacher("Shahid Afridi", "Phython")
phitron.addTeacher("Ayman Afridi", "Machine Learning")

phitron.studentEnroll("Ruma", 5000)
phitron.studentEnroll("Ayaan", 50000)
        

print(phitron)