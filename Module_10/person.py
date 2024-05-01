import random
from school import School

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)

    def evaluate_exam(self):
        return random.randint(1,100)

class Student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom = classroom # classroom is a object
        self.__id = None
        self.marks = {} # {'bangla':71, 'english':80}
        self.subject_grade = {} # {'bangla': 'A', 'english': 'A+'}
        self.grade = None

    def calculate_final_grade(self):
        sum=0
        for grade in self.subject_grade.values():
            point = School.grade_to_gpa(grade)
            sum +=point
        if sum ==0:
            gpa = 0
            self.grade = 'F'
        else:
            gpa = sum / len(self.subject_grade)
            self.grade = School.gpa_to_grade(gpa)
        return f"{self.name}'s Final Grade: {self.grade} with GPA: {gpa}\n"
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self,value):
        self.__id = value
