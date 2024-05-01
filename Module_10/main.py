from school import School
from person import Student, Teacher
from subject import Subject
from classroom import ClassRoom

school = School('ABC',"Dhaka")

eight = ClassRoom("Eight")
nine = ClassRoom("Nine")
ten = ClassRoom("Ten")

school.add_classroom(eight)
school.add_classroom(nine)
school.add_classroom(ten)


#Adding student
shahid = Student('Shahid Afridi', ten)
ruma = Student('Ruma Khatun', ten)
ayman = Student('Ayman Afridi', eight)
karina = Student('Karina Kapur', eight)
bean = Student('Mr. Bean' , nine)
chaplin = Student('Charlie Chaplin', nine)

school.student_addmission(shahid)
school.student_addmission(ayman)
school.student_addmission(ruma)
school.student_addmission(karina)
school.student_addmission(bean)
school.student_addmission(chaplin)

# Adding teacher
jhankar = Teacher('Jhankar Mahbub')
naim = Teacher('Abdullah AL Naim')
pahtan = Teacher('Rahat Khan Pathan')

# Adding subject 
python = Subject('Python', jhankar)
django = Subject('Django', naim)
algo = Subject('Algorithm', pahtan)
ds = Subject('Data Structure', pahtan)


eight.add_subject(algo)
eight.add_subject(ds)
nine.add_subject(ds)
nine.add_subject(algo)
nine.add_subject(python)
ten.add_subject(ds)
ten.add_subject(algo)
ten.add_subject(python)
ten.add_subject(django)


eight.take_semester_final_exam()
nine.take_semester_final_exam()
ten.take_semester_final_exam()

print(school)