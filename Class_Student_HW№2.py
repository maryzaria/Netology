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

    def rate_lectures(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached \
                and self.courses_in_progress and 0 <= grade <= 10:
            lecturer.lect_grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lect_grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student)\
                and course in self.courses_attached\
                and course in student.courses_in_progress:
            # student.grades[course] = student.grades.get(course, []).append(grade)
            student.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'


if __name__ == '__main__':
    some_student = Student('Ruoy', 'Eman', 'your_gender')
    some_student.courses_in_progress += ['Python']

    cool_lecturer = Lecturer('Some', 'Buddy')
    cool_lecturer.courses_attached += ['Python']

    some_student.rate_lectures(cool_lecturer, 'Python', 9)
    some_student.rate_lectures(cool_lecturer, 'Python', 10)

    print(cool_lecturer.lect_grades)
