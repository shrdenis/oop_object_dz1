class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(total_grades) / len(total_grades)

    def __str__(self):
        avg_grade = self.average_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade:.1f}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершенные курсы: {finished_courses}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = [grade for grades in self.grades.values() for grade in grades]
        return sum(total_grades) / len(total_grades)

    def __str__(self):
        avg_grade = self.average_grade()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {avg_grade:.1f}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Функции для подсчета средней оценки
def average_student_grade(students, course):
    total_grades = []
    for student in students:
        if course in student.grades:
            total_grades.extend(student.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0

def average_lecturer_grade(lecturers, course):
    total_grades = []
    for lecturer in lecturers:
        if course in lecturer.grades:
            total_grades.extend(lecturer.grades[course])
    return sum(total_grades) / len(total_grades) if total_grades else 0


students = [
    Student('Ruoy', 'Eman', 'your_gender'),
    Student('John', 'Doe', 'male')
]

students[0].courses_in_progress += ['Python']
students[0].finished_courses += ['Введение в программирование']

students[1].courses_in_progress += ['Python']
students[1].finished_courses += ['Введение в программирование']

reviewers = [
    Reviewer('Some', 'Buddy'),
    Reviewer('Another', 'Reviewer')
]

reviewers[0].courses_attached += ['Python']
reviewers[1].courses_attached += ['Python']

reviewers[0].rate_hw(students[0], 'Python', 10)
reviewers[0].rate_hw(students[0], 'Python', 9)
reviewers[0].rate_hw(students[0], 'Python', 10)

reviewers[1].rate_hw(students[1], 'Python', 8)
reviewers[1].rate_hw(students[1], 'Python', 7)
reviewers[1].rate_hw(students[1], 'Python', 9)

lecturers = [
    Lecturer('Cool', 'Lecturer'),
    Lecturer('Another', 'Lecturer')
]

lecturers[0].courses_attached += ['Python']
lecturers[1].courses_attached += ['Python']

students[0].rate_lecturer(lecturers[0], 'Python', 10)
students[0].rate_lecturer(lecturers[0], 'Python', 8)

students[1].rate_lecturer(lecturers[1], 'Python', 9)
students[1].rate_lecturer(lecturers[1], 'Python', 7)

# Вывод данных
print(students[0])
print(students[1])
print(reviewers[0])
print(reviewers[1])
print(lecturers[0])
print(lecturers[1])

# Подсчет средней оценки
print(f'Средняя оценка за домашние задания по всем студентам в рамках курса Python: {average_student_grade(students, "Python"):.1f}')
print(f'Средняя оценка за лекции всех лекторов в рамках курса Python: {average_lecturer_grade(lecturers, "Python"):.1f}')
