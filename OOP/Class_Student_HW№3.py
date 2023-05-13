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

    def _mean_student_grade(self):
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
               f"Средняя оценка за домашние задания: {self._mean_student_grade()}\n" \
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
        try:
            return self._mean_student_grade() == other._mean_student_grade()
        except AttributeError:
            return 'кто-то не является студентом'

    def __gt__(self, other):
        try:
            return self._mean_student_grade() > other._mean_student_grade()
        except AttributeError:
            return 'кто-то не является студентом'


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

    def _mean_lect_grade(self):
        try:
            mean_grade = 0
            for values in self.lect_grades.values():
                mean_grade += (sum(values) / len(values))
            return mean_grade / len(self.lect_grades)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        return f"Имя: {self.name} \n" \
               f"Фамилия: {self.surname} \n" \
               f"Средняя оценка за лекции: {self._mean_lect_grade()}"

    def __eq__(self, other):
        try:
            return self._mean_lect_grade() == other._mean_lect_grade()
        except AttributeError:
            return 'кто-то не является лектором'

    def __gt__(self, other):
        try:
            return self._mean_lect_grade() > other._mean_lect_grade()
        except AttributeError:
            return 'кто-то не является лектором'


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


if __name__ == '__main__':
    student1 = Student('Ruoy', 'Eman', 'your_gender')
    student1.courses_in_progress += ['Python']

    student2 = Student('Mary', 'Zar', 'female')
    student2.courses_in_progress += ['Python']

    rew = Reviewer('New', "Reviewer")
    rew.courses_attached += ['Python']
    rew.rate_hw(student1, 'Python', 8)
    rew.rate_hw(student2, 'Python', 10)
    print(student1 <= student2)
    print(student1)




