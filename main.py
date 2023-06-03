import subject_module
import student_module

# creating 3 subjects
physics = subject_module.Subject("physics", 95)
programming = subject_module.Subject("Python", 99)
Arabic = subject_module.Subject("Arabic", 96)

# creating 3 students
s1 = student_module.Student("Deema", 20, "Gaza")
s2 = student_module.Student("Belal", 40, "Khan-Yonis")
s3 = student_module.Student("Rami", 45, "Ramallah")

# adding marks for deema
s1.add_mark(90)
s1.add_mark(80)
s1.add_mark(70)

# print avg
print(s1.Calc_average())

