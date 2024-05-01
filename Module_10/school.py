class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {} #{'bangla' : teacher object}
        self.classrooms = {} # {"Eight" : classroom object}


    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_addmission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_student(student)


    @staticmethod
    def calculateGrade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        elif 0 <= marks < 33:
            return 'F'
        else:
            return "Invalid Marks"
    
    @staticmethod
    def grade_to_gpa(grade):
        grade_gpa= {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00,
        }
        return grade_gpa[grade]
    
    @staticmethod
    def gpa_to_grade(gpa):
        if 5 <= gpa:
            return 'A+'
        elif 4 <= gpa < 5:
            return 'A'
        elif 3.5 <= gpa < 4:
            return 'A-'
        elif 3 <= gpa < 3.5:
            return 'B'
        elif 2 <= gpa < 3:
            return 'C'
        elif 1 <= gpa < 2:
            return 'D'
        elif gpa < 1:
            return 'F'
        else:
            return "Invalid GPA"
    
    def __repr__(self) -> str:
        
        # All Classroom
        for key in self.classrooms.keys():
            print(key)
        
        # All Students
        print('------- All Students -------')
        result = ""
        for key, value in self.classrooms.items():
            result += f"--- {key.upper()} Classroom's Students ---\n"
            for student in value.students:
                result += f"\t{student.name}\n"
        print(result)       

        # All Subjects
        print('------- All Subjects -------')
        result = ""
        for key, value in self.classrooms.items():
            result += f"--- {key.upper()} Classroom's Subject ---\n"
            for subject in value.subjects:
                result += f"\t{subject.name}\n"
        print(result)    


        # All students result
        print('------- All students result -------')
        for key , value in self.classrooms.items():
            for student in value.students:
                for sub, mark in student.marks.items():
                    print(student.name, sub, mark, student.subject_grade[sub])
                print(student.calculate_final_grade())

        return ''