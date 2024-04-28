class Student:
    def __init__(self, name, id, phone, email) -> None:
        self.name = name
        self.id = id
        self.phone = phone
        self.email = email
        
    def __repr__(self) -> str:
        return f"Name: {self.name}, Phone: {self.phone}"
    
class Course:
    def __init__(self, name,id, fee, duration) -> None:
        self.name = name
        self.id = id
        self.fee = fee
        self.duration = duration
        
    def __repr__(self) -> str:
        return f"Course - Name: {self.name}, Fee: {self.fee}, Duration: {self.duration} week."


class Coaching:
    def __init__(self, name, phone, address) -> None:
        self.name = name
        self.phone = phone
        self.address = address
        self.students = []
        self.courses = []
        self.erolled = []
        
    def __repr__(self) -> str:
        return f"Coaching: {self.name}, Address: {self.address}"

    def add_student(self, name, phone, email):
        id = len(self.students)
        student = Student(name,id, phone,email)
        self.students.append(student)
        
    def add_course(self, name, fee, duration):
        id = len(self.courses)
        course = Course(name,id,fee,duration)
        self.courses.append(course)
    
    def courseEnroll(self, studentEmail, courseName) :
        enroll = []
        for student in self.students:
            if student.email == studentEmail:
                enroll.append(student)
        for course in self.courses:
            if course.name == courseName:
                enroll.append(course)
        self.erolled.append(enroll)
    
ph = Coaching("Programming Hero", "01712345678", "Banani, Dhaka")       
phitron = Coaching("Phitron", "01555555555", "Banani, Dhaka")

ph.add_course("Full Stack Web Development", 5500, 26)
phitron.add_course("CSE Fundamentals", 6500, 52)

ph.add_student("Shahid", "01704805886", "shahidafridi.cse@gmail.com")
phitron.add_student("Shahid", "01704805886", "shahidafridi.cse@gmail.com")

ph.courseEnroll("shahidafridi.cse@gmail.com","Full Stack Web Development")

print(ph.erolled)
        