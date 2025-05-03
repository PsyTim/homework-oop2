class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


# Ниже выполнение первого задания


class Lecturer(Mentor): ...


class Reviewer(Mentor): ...


# Проверяем как работает наследование для новых пустых классов
lecturer = Lecturer("Иван", "Федоров")
lecturer.courses_attached += ['Python']
print(f"{lecturer.name} {lecturer.surname} {lecturer.courses_attached}")

reviewer = Reviewer("Семен", "Архипов")
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']
print(f"{reviewer.name} {reviewer.surname} {reviewer.courses_attached}")

best_student.courses_in_progress += ['Git']
reviewer.rate_hw(best_student, 'Git', 8)
reviewer.rate_hw(best_student, 'Git', 9)
print(f"{best_student.name} {best_student.surname} {best_student.courses_in_progress} {best_student.grades}")
