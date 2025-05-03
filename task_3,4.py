from copy import deepcopy


class Grades:

    def __init__(self):
        self.grades = {}

    def avg(self):
        summ = 0
        count = 0
        for _, g in self.grades.items():
            summ += sum(g)
            count += len(g)
        return summ / count if count > 0 else 0

    def __eq__(self, other):
        return self.avg() == other.avg()

    def __gt__(self, other):
        return self.avg() > other.avg()

    def __ge__(self, other):
        return self.avg() >= other.avg()

    @classmethod
    def avg_by_course(cls, lst: list["Grades"], course: str):
        summ = 0
        count = 0
        for c in lst:
            summ += sum(c.grades.get(course, []))
            count += len(c.grades.get(course, []))
        return summ / count if count > 0 else 0


class Student(Grades):

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        Grades.__init__(self)

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

    def __str__(self):
        return (
            f"Имя: {self.name}\nФамилия: {self.surname}\n"
            + f"Средняя оценка за домашние задания: {self.avg()}\n"
            + f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
            + f"Завершенные курсы: {', '.join(self.finished_courses)}"
        )


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

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor, Grades):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        Grades.__init__(self)

    def rate_hw(self, *args):
        # При вызове этого метода вызываем исключение
        raise AttributeError("'Lecturer' object has no attribute 'rate_hw'")

    def __str__(self):
        return super().__str__() + f"\nСредняя оценка за лекции: {self.avg()}"


class Reviewer(Mentor): ...


print()

# добавляем экспертов
print("# Добавляем экспертов")
reviewer_1 = Reviewer("Семен", "Архипов")
reviewer_1.courses_attached += ["Python"]
reviewer_1.courses_attached += ["Git"]
print(reviewer_1)
print()
reviewer_2 = Reviewer("Валентина", "Игнатьева")
reviewer_2.courses_attached += ["Python"]
reviewer_2.courses_attached += ["SQL"]
reviewer_2.courses_attached += ["Введение в программирование"]
print(reviewer_2)
print()

# добавляем студениов и оценки
print("# Добавляем студениов и оценки")
student_1 = Student("Катя", "Семенова", "жен")
student_1.courses_in_progress += ["Python"]
student_1.courses_in_progress += ["SQL"]
student_1.courses_in_progress += ["Git"]
student_1.finished_courses += ["Введение в программирование"]

reviewer_1.rate_hw(student_1, "Python", 9)
reviewer_1.rate_hw(student_1, "Git", 10)
reviewer_1.rate_hw(student_1, "Git", 8)
reviewer_2.rate_hw(student_1, "Python", 7)
reviewer_2.rate_hw(student_1, "Python", 8)
reviewer_2.rate_hw(student_1, "SQL", 7)

print(student_1)
print()

student_2 = Student("Александр", "Петров", "муж")
student_2.courses_in_progress += ["Python"]
student_2.courses_in_progress += ["SQL"]
student_2.courses_in_progress += ["Введение в программирование"]
student_2.finished_courses += ["Git"]
reviewer_1.rate_hw(student_2, "Python", 10)
reviewer_2.rate_hw(student_2, "Python", 7)
reviewer_2.rate_hw(student_2, "Введение в программирование", 7)

print(student_2)
print()

print()

# добавляем лекторов и оценки
print("# Добавляем лекторов и оценки")
lecturer_1 = Lecturer("Иван", "Федоров")
lecturer_1.courses_attached += ["Python"]

# проверяем, что студент может поставить оценку лектору
student_1.rate_hw(lecturer_1, "Python", 10)
student_2.rate_hw(
    lecturer_1, "Git", 10
)  # эта оценка не выставится, потому что лектор не читает лекций по Git
student_1.rate_hw(lecturer_1, "Python", 7)
# print(f"{lecturer_1.name} {lecturer_1.surname} {lecturer_1.courses_attached} {lecturer_1.grades}")
print(lecturer_1)
print()

# проверяем что лектор не может выставлять оценки студенту
# возникнет ошибка
# lecturer.rate_hw(student, "Python", 1)
# print(f"{student.name} {student.surname} {student.courses_in_progress} {student.grades}")

lecturer_2 = Lecturer("Валерия", "Романова")
lecturer_2.courses_attached += ["Python"]
lecturer_2.courses_attached += ["SQL"]
lecturer_2.courses_attached += ["Введение в программирование"]

# проверяем, что студент может поставить оценку лектору
student_2.rate_hw(lecturer_2, "Python", 5)
student_1.rate_hw(lecturer_2, "SQL", 10)
student_2.rate_hw(lecturer_2, "Введение в программирование", 9)
# print(f"{lecturer_2.name} {lecturer_2.surname} {lecturer_2.courses_attached} {lecturer_2.grades}")

print(lecturer_2)
print()

s_1, s_2, s_3 = student_1, student_2, deepcopy(student_2)
print(f"сравнения Students {s_2.avg()} и {s_1.avg()}")
print("< ", s_2 < s_1)
print("<=", s_2 <= s_1)
print("==", s_2 == s_1)
print("!=", s_2 != s_1)
print(">=", s_2 >= s_1)
print("> ", s_2 > s_1)
print()

print(f"сравнения Students {s_2.avg()} и {s_3.avg()}")
print("< ", s_2 < s_3)
print("<=", s_2 <= s_3)
print("==", s_2 == s_3)
print("!=", s_2 != s_3)
print(">=", s_2 >= s_3)
print("> ", s_2 > s_3)
print()

print(f"сравнения Students {s_1.avg()} и {s_2.avg()}")
print("< ", s_1 < s_2)
print("<=", s_1 <= s_2)
print("==", s_1 == s_2)
print("!=", s_1 != s_2)
print(">=", s_1 >= s_2)
print("> ", s_1 > s_2)
print()

l_1, l_2, l_3 = lecturer_1, lecturer_2, deepcopy(lecturer_2)
print(f"сравнения лекторов {l_2.avg()} и {l_1.avg()}")
print("< ", l_2 < l_1)
print("<=", l_2 <= l_1)
print("==", l_2 == l_1)
print("!=", l_2 != l_1)
print(">=", l_2 >= l_1)
print("> ", l_2 > l_1)
print()

print(f"сравнения лекторов {l_2.avg()} и {l_3.avg()}")
print("< ", l_2 < l_3)
print("<=", l_2 <= l_3)
print("==", l_2 == l_3)
print("!=", l_2 != l_3)
print(">=", l_2 >= l_3)
print("> ", l_2 > l_3)
print()

print(f"сравнения лекторов {l_1.avg()} и {l_2.avg()}")
print("< ", l_1 < lecturer_2)
print("<=", l_1 <= l_2)
print("==", l_1 == l_2)
print("!=", l_1 != l_2)
print(">=", l_1 >= l_2)
print("> ", l_1 > l_2)
print()

s = [student_1, student_2]
print("Средние оценки студентов по курсам")
print("Python", Grades.avg_by_course(s, "Python"))
print("SQL", Grades.avg_by_course(s, "SQL"))
print("Git", Grades.avg_by_course(s, "Git"))
print(
    "Введение в программирование",
    Grades.avg_by_course(s, "Введение в программирование"),
)
print()
lr = [lecturer_1, lecturer_2]
print("Средние оценки лекторов по курсам")
print("Python (для одного лектора)", Grades.avg_by_course([lecturer_1], "Python"))
print("Python", Grades.avg_by_course(lr, "Python"))
print("SQL", Grades.avg_by_course(lr, "SQL"))
print("Git", Grades.avg_by_course(lr, "Git"))
print(
    "Введение в программирование",
    Grades.avg_by_course(lr, "Введение в программирование"),
)
