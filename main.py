class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        mid_grades = sum_kursov = 0
        for kurs in self.grades.values():
            for grades in range(len(kurs)):
                    mid_grades += kurs[grades]
                    sum_kursov += 1
        return (f'Имя: {self.name}, \nФамилия: {self.surname}\nСредняя оценка за д\з: {mid_grades/sum_kursov}'
                f'\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}')

    def __eq__(self, other):
        mid_grades = sum_kursov = 0
        for kurs in self.grades.values():
            for grades in range(len(kurs)):
                    mid_grades += kurs[grades]
                    sum_kursov += 1
        if sum_kursov != 0:
             avarge_1 = mid_grades/sum_kursov
        mid_grades = sum_kursov = 0

        mid_grades = sum_kursov = 0
        for kurs in other.grades.values():
            for grades in range(len(kurs)):
                    mid_grades += kurs[grades]
                    sum_kursov += 1
        if sum_kursov != 0:
             avarge_2 = mid_grades/sum_kursov
        return avarge_1 == avarge_2

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Lecturer (Mentor):
     def __str__(self):
        mid_grades = sum_kursov = 0
        for kurs in self.grades.values():
            for grades in range(len(kurs)):
                mid_grades += kurs[grades]
                sum_kursov += 1
        if sum_kursov == 0:
            return ('Ошибка')
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредний бал: {mid_grades/sum_kursov}\n')

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}, \nФамилия: {self.surname}\n')

def avarge_grades(spisok, kurs): # для студентов и лекторов одинаково
    summa = kol_grades = 0
    for i in spisok:
        if i.grades.get(kurs) != None:
            for y in i.grades.get(kurs):
                summa += y
                kol_grades += 1
    if kol_grades == 0:
        return ('Ошибка')
    return (f'Cредний балл по курсу {kurs} : {summa/kol_grades}\n')

# Реализуйте возможность сравнивать (через операторы сравнения) между
# собой лекторов по средней оценке за лекции и студентов по средней оценке за домашние задания.

spisok_studentov = []
spisok_lectorov = []
spisok_reviewer = []

student = Student('Ivan', 'Petrov', 'man')
student.courses_in_progress += ['Python', 'Java']
student.add_courses('C#')
spisok_studentov.append(student)

student = Student('Vasiliy', 'Sergeev', 'man')
student.courses_in_progress += ['Python']
student.add_courses('Java')
spisok_studentov.append(student)

mentor = Reviewer('Sergey', 'Ivanov')
mentor.courses_attached += ['Python', 'Java']
spisok_reviewer.append(mentor)

mentor = Reviewer('Denis', 'Orlov')
mentor.courses_attached += ['Python', 'C++']
spisok_reviewer.append(mentor)

mentor = Lecturer ('Maxim', 'Egorov')
mentor.courses_attached += ['Python', 'Java']
spisok_lectorov.append(mentor)

mentor = Lecturer ('Oleg', 'Zhukin')
mentor.courses_attached += ['Python', 'Java', 'C++']
spisok_lectorov.append(mentor)

spisok_studentov[0].rate_lector(spisok_lectorov[0], 'Python', 10)
spisok_studentov[0].rate_lector(spisok_lectorov[0], 'Python', 5)
spisok_studentov[0].rate_lector(spisok_lectorov[0], 'Java', 3)
spisok_studentov[0].rate_lector(spisok_lectorov[1], 'Python', 7)
spisok_studentov[0].rate_lector(spisok_lectorov[1], 'Java', 6)
spisok_reviewer[0].rate_hw(spisok_studentov[0], 'Python', 3)
spisok_reviewer[1].rate_hw(spisok_studentov[0], 'Python', 9)
spisok_reviewer[0].rate_hw(spisok_studentov[0], 'Java', 7)
spisok_reviewer[0].rate_hw(spisok_studentov[1], 'Python', 4)

print (spisok_reviewer[1])
print (spisok_lectorov[1])
print (spisok_studentov[1])
print (avarge_grades(spisok_studentov, 'Python'))
print (avarge_grades(spisok_lectorov, 'Java'))

print (spisok_studentov[0] == spisok_studentov[1])