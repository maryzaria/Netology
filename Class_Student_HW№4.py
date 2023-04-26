from functools import total_ordering


@total_ordering  # декоратор, чтобы не определять каждый из магических методов сравнения
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def mean_student_grade(self):
        # случай, когда у студента есть оценки за ДЗ
        try:
            mean_grade = 0
            for values in self.grades.values():
                mean_grade += (sum(values) / len(values))
            return mean_grade / len(self.grades)
        # случай, когда у студента нет ни одной оценки (len(self.grades) == 0)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за домашние задания: {self.mean_student_grade()}\n" \
               f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n" \
               f"Завершенные курсы: {', '.join(self.finished_courses)}"

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and (course in self.courses_in_progress or course in self.finished_courses) \
                and 0 <= grade <= 10:
            lecturer.lect_grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'

    def __eq__(self, other):
        return self.mean_student_grade() == other.mean_student_grade()

    def __gt__(self, other):
        return self.mean_student_grade() > other.mean_student_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


@total_ordering
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_grades = {}

    def mean_lect_grade(self):
        try:
            mean_grade = 0
            for values in self.lect_grades.values():
                mean_grade += (sum(values) / len(values))
            return mean_grade / len(self.lect_grades)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f"Имя: {self.name}\n" \
               f"Фамилия: {self.surname}\n" \
               f"Средняя оценка за лекции: {self.mean_lect_grade()}"

    def __eq__(self, other):
        return self.mean_lect_grade() == other.mean_lect_grade()

    def __gt__(self, other):
        return self.mean_lect_grade() > other.mean_lect_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f"Имя: {self.name} \nФамилия: {self.surname}"

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) \
                and course in self.courses_attached \
                and course in student.courses_in_progress:
            # student.grades[course] = student.grades.get(course, []).append(grade)
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


def mean_stud_grade_for_course(group: list[Student], course: str) -> float:
    sum_grade, count = 0, 0
    for student in group:
        if course in student.grades:
            sum_grade += sum(student.grades[course]) / len(student.grades[course])
        else:
            count += 1
    return sum_grade / len(group) if count != len(group) else 'никто из студентов не изучает данный курс'


def mean_lect_grade_for_course(lst: list[Lecturer], course: str) -> float:
    sum_grade, count = 0, 0
    for lecturer in lst:
        if course in lecturer.lect_grades:
            sum_grade += sum(lecturer.lect_grades[course]) / len(lecturer.lect_grades[course])
        else:
            count += 1
    return sum_grade / len(lst) if count != len(lst) else 'никто из лекторов не читает данный курс'


if __name__ == '__main__':
    student1 = Student('Ruoy', 'Eman', 'your_gender')
    student1.courses_in_progress += ['Python', 'Git']
    student1.add_courses('C++')

    student2 = Student('Mary', 'Zar', 'female')
    student2.courses_in_progress += ['Python', 'Git', 'OOP']
    student2.add_courses('C++')

    reviewer1 = Reviewer('First', "Reviewer")
    reviewer1.courses_attached += ['Python', 'C++']
    reviewer1.rate_hw(student1, 'Python', 7)
    reviewer1.rate_hw(student1, 'Python', 4)
    reviewer1.rate_hw(student2, 'Python', 10)
    reviewer1.rate_hw(student2, 'Python', 9)

    reviewer2 = Reviewer('Second', "Reviewer")
    reviewer2.courses_attached += ['Git']
    reviewer2.rate_hw(student1, 'Git', 10)
    reviewer2.rate_hw(student1, 'Git', 9)
    reviewer2.rate_hw(student2, 'Git', 10)
    reviewer2.rate_hw(student2, 'Git', 8)
    print(f"Оценки {student1.name}: {student1.grades}")
    print(f"Оценки {student2.name}: {student2.grades}")
    if student1 > student2:
        print(f"{student1.name} учится лучше {student2.name}")
    else:
        print(f"{student2.name} учится лучше {student1.name}")

    print(f"Средняя оценка за курс Git: {mean_stud_grade_for_course([student1, student2], 'Git')}")
    # print(mean_stud_grade_for_course([student1, student2], 'Python'))
    print(f"Средняя оценка за курс C++: {mean_stud_grade_for_course([student1, student2], 'C++')}")

    cool_lecturer = Lecturer('Ivan', 'Ivanovich')
    cool_lecturer.courses_attached += ['Python']

    bad_lecturer = Lecturer('Petr', 'Petrovich')
    bad_lecturer.courses_attached += ['C++', 'Python']

    student1.courses_in_progress += ['C++']
    student1.rate_lectures(cool_lecturer, 'Python', 9)
    student1.rate_lectures(cool_lecturer, 'Python', 10)
    print(f"Оценки лектора {cool_lecturer.name}: {cool_lecturer.lect_grades}")

    student1.rate_lectures(bad_lecturer, 'C++', 5)
    student1.rate_lectures(bad_lecturer, 'Python', 3)
    print(f"Средняя оценка лекторов за курс Python: {mean_lect_grade_for_course([cool_lecturer, bad_lecturer], 'Python')}")
    print()
    print(cool_lecturer)
    print()
    print(student1)
