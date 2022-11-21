class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        str_ = (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self._avg_grade_()}'
                f'\nКурсы в процессе изучения: {", ".join(str(x) for x in self.courses_in_progress)}'
                f'\nЗавершенные курсы: {", ".join(str(x) for x in self.finished_courses)}')
        return str_

    def __lt__(self, student):
        if isinstance(student, Student):
            return self._avg_grade_() < student._avg_grade_()
        else:
            return 'Ошибка'

    def __le__(self, student):
        if isinstance(student, Student):
            return self._avg_grade_() <= student._avg_grade_()
        else:
            return 'Ошибка'

    def __eq__(self, student):
        if isinstance(student, Student):
            return self._avg_grade_() == student._avg_grade_()
        else:
            return 'Ошибка'

    def _avg_grade_(self):
        all_grades = []
        for course in self.grades:
            for grade in self.grades[course]:
                all_grades.append(grade)
        avg_grade = sum(all_grades) / len(all_grades)
        return avg_grade

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer) and course in self.courses_in_progress
                and course in lecturer.courses_attached and isinstance(grade, int) and 0 < grade <= 10):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
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
        self.grades = {}

    def __str__(self):
        str_ = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_grade_()}'
        return str_
    
    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self._avg_grade_() < lecturer._avg_grade_()
        else:
            return 'Ошибка'

    def __le__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self._avg_grade_() <= lecturer._avg_grade_()
        else:
            return 'Ошибка'

    def __eq__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self._avg_grade_() == lecturer._avg_grade_()
        else:
            return 'Ошибка'
        
    def _avg_grade_(self):
        all_grades = []
        for course in self.grades:
            for grade in self.grades[course]:
                all_grades.append(grade)
        avg_grade = sum(all_grades) / len(all_grades)
        return avg_grade


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        str_ = f'Имя: {self.name}\nФамилия: {self.surname}'
        return str_

    def rate_hw(self, student, course, grade):
        if (isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress
                and isinstance(grade, int) and 0 < grade <= 10):
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def course_students_avg_grade(students, course):
    if not isinstance(students, list):
        return 'Ошибка'
    all_grades = []
    for student in students:
        if not isinstance(student, Student):
            return 'Ошибка'
        if course not in student.grades:
            return 'Ошибка'
        for grade in student.grades[course]:
            all_grades.append(grade)
    avg_grade = sum(all_grades) / len(all_grades)
    return f'Средняя оценка среди всех студентов по курсу {course} составляет {avg_grade}'


def course_lecturers_avg_grade(lecturers, course):
    if not isinstance(lecturers, list):
        return 'Ошибка'
    all_grades = []
    for lecturer in lecturers:
        if not isinstance(lecturer, Lecturer):
            return 'Ошибка'
        if course not in lecturer.grades:
            return 'Ошибка'
        for grade in lecturer.grades[course]:
            all_grades.append(grade)
    avg_grade = sum(all_grades) / len(all_grades)
    return f'Средняя оценка среди всех лекторов по курсу {course} составляет {avg_grade}'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'Java']
best_student.finished_courses += ['JavaScript']
worse_student = Student('Bad', 'Student', 'gender')
worse_student.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python', 'Java']

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
bad_lecturer = Lecturer('Other', 'Buddy')
bad_lecturer.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 8)
cool_mentor.rate_hw(worse_student, 'Python', 9)
cool_mentor.rate_hw(best_student, 'Java', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 1)
best_student.rate_lecturer(bad_lecturer, 'Python', 10)

print(best_student)
print(cool_lecturer)
print(cool_mentor)

print(cool_lecturer <= bad_lecturer)

print(course_students_avg_grade([best_student, worse_student], 'Python'))

print(course_lecturers_avg_grade([cool_lecturer, bad_lecturer], 'Python'))