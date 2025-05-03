class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if (
            isinstance(student, Student)
            and course in self.courses_attached
            and course in student.courses_in_progress
        ):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lectour, course, grade):
        if (
            isinstance(lectour, Lecturer)
            and course in self.courses_in_progress
            and course in lectour.courses_attached
        ):
            if course in lectour.grades:
                lectour.grades[course] += [grade]
            else:
                lectour.grades[course] = [grade]
        else:
            return "Ошибка"


student = Student("Катя", "Семенова", "жен")
student.courses_in_progress += ["Python"]
student.courses_in_progress += ["SQL"]
student.courses_in_progress += ["Git"]

mentor = Mentor("Валентина", "Игнатьева")
mentor.courses_attached += ["Python"]
mentor.courses_attached += ["SQL"]
mentor.rate_hw(student, "Python", 7)
mentor.rate_hw(student, "Python", 10)
mentor.rate_hw(student, "SQL", 8)
print(student.grades)


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, *args):
        # При вызове этого метода вызываем исключение
        raise AttributeError("'Mentor' object has no attribute 'rate_hw'")


class Reviewer(Mentor): ...


# добавляем эксперта
reviewer = Reviewer("Семен", "Архипов")
reviewer.courses_attached += ["Python"]
reviewer.courses_attached += ["Git"]
print(f"{reviewer.name} {reviewer.surname} {reviewer.courses_attached}")

# проверяем что эксперт может выставлять оценки студенту
reviewer.rate_hw(student, "Git", 8)
reviewer.rate_hw(student, "Git", 9)
reviewer.rate_hw(student, "Python", 6)

# проверяем что новые оценки были успешно выставлены
print(
    f"{student.name} {student.surname} {student.courses_in_progress} {student.grades}"
)

# добавляем лектора
lecturer = Lecturer("Иван", "Федоров")
lecturer.courses_attached += ["Python"]

# проверяем, что студент может поставить оценку лектору
student.rate_hw(lecturer, 'Python', 10)
student.rate_hw(lecturer, 'Git', 10) # эта оценка не выставится, потому что лектор не читает лекций по Git
student.rate_hw(lecturer, 'Python', 7)
print(f"{lecturer.name} {lecturer.surname} {lecturer.courses_attached} {lecturer.grades}")

# проверяем что лектор не может выставлять оценки студенту
# возникнет ошибка
lecturer.rate_hw(student, "Python", 1)
print(f"{student.name} {student.surname} {student.courses_in_progress} {student.grades}")
