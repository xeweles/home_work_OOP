def _find_avg(dict_grades):
    '''нахождение средней оценки'''
    sum_ = 0
    len_ = 0
    for grades_list in dict_grades:
        for grade in grades_list:
            sum_ += grade
            len_ += 1
    avg_grade = float(round((sum_ / len_), 1))
    return avg_grade

# списки студентов и лекторов
lst_students = []
lst_lekturer = []

class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = [ ]
        self.courses_in_progress = [ ]
        self.grades = {}
        self.avg_grades = 0
        lst_students.append(self)

    def update_avg(self):
        self.avg_grades += _find_avg(self.grades.values())
        return self.avg_grades

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за домашние задания: {self.update_avg()}'
                f'\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}'
                f'\nЗавершённые курсы: {", ".join(self.finished_courses)}')

    def __eq__(self, other):
        return self.avg_grades == other.avg_grades

    def __lt__(self, other):
        return self.avg_grades < other.avg_grades

    def __le__(self, other):
        return self.avg_grades <= other.avg_grades

    def rate_lekt(self, lektor, course, grade):
        '''оценивание лектора'''
        if grade > 0 and grade < 11:
            if isinstance(lektor, Lekturer) and course in self.courses_in_progress and course in lektor.courses_attached:
                if course in lektor.grades:
                    lektor.grades[course] += [grade]
                else:
                    lektor.grades[course] = [grade]
            else:
                print('###ошибка###')
        else:
            print('оценка должна быть от 1 до 10')

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lekturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = 0
        lst_lekturer.append(self)

    def update_avg(self):
        self.avg_grade += _find_avg(self.grades.values())
        return self.avg_grade

    def __str__(self):
        return (f'Имя: {self.name}'
                f'\nФамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.update_avg()}')

    def __eq__(self, other):
        return self.avg_grade == other.avg_grade

    def __lt__(self, other):
        return self.avg_grade < other.avg_grade

    def __le__(self, other):
        return self.avg_grade <= other.avg_grade

class Reviewer(Mentor):

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        '''оценивание студента'''
        if grade > 0 and grade < 11:
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return '###Ошибка###'
        else:
            print('Оценка должна быть от 1 до 10')

def all_grades_students(lst_st, course):
    '''нахождение средней оценки за дз по всем студентам в рамках конкретного курса'''
    sum_ = 0
    len_ = 0
    for student in lst_st:
        for i in student.grades.keys():
            if i == course:
                for j in student.grades[i]:
                    sum_ += j
                    len_ += 1
    return f'Средняя оценка всех студентов в рамках курса {course}: {round((sum_ / len_), 1)}'

def all_grades_lekturer(lst_lekt, course):
    '''нахождение средней оценки за дз по всем лекторам в рамках конкретного курса'''
    sum_ = 0
    len_ = 0
    for lekt in lst_lekt:
        for i in lekt.grades.keys():
            if i == course:
                for j in lekt.grades[i]:
                    sum_ += j
                    len_ += 1
    return f'Средняя оценка всех лекторов в рамках курса {course}: {round((sum_ / len_), 1)}'


# Создание экземпляров
student1 = Student('Имя первого студента', 'Фамилия первого студента', 'Пол первого студента')
lekt1 = Lekturer('Имя первого лектора', 'Фамилия первого лектора')
reviewer1 = Reviewer('Имя первого ревьювера', 'Фамилия первого ревьювера')

student2 = Student('Имя второго студента', 'Фамилия второго студента', 'Пол второго студента')
lekt2 = Lekturer('Имя второго лектора', 'Фамилия второго лектора')
reviewer2 = Reviewer('Имя второго ревьювера', 'Фамилия второго ревьюера')


student1.finished_courses += ['java']
student2.finished_courses += ['git', 'c#']

student1.courses_in_progress += ['python', 'git']
student2.courses_in_progress += ['c++', 'JavaScript', 'python']

reviewer1.courses_attached += ['python', 'JavaScript']
reviewer2.courses_attached += ['git', 'c++', 'c#']

lekt1.courses_attached += ['c++', 'git']
lekt2.courses_attached += ['python', 'JavaScript', 'git']

student1.rate_lekt(lekt1, 'java', 7)
student1.rate_lekt(lekt1, 'git', 3)
student1.rate_lekt(lekt1, 'git', 8)
student2.rate_lekt(lekt2, 'JavaScript', 6)
student2.rate_lekt(lekt1, 'c++', 4)
student2.rate_lekt(lekt2, 'git', 4)

reviewer1.rate_hw(student1, 'python', 8)
reviewer1.rate_hw(student2, 'JavaScript', 3)
reviewer1.rate_hw(student2, 'python', 7)
reviewer1.rate_hw(student2, 'python', 2)
reviewer2.rate_hw(student1, 'git', 6)
reviewer2.rate_hw(student2, 'c++', 9)

print('STUDENTS')
print(student1)
print(student2)

print('LEKTURERS')
print(lekt1)
print(lekt2)

print('REVIEWERS')
print(reviewer1)
print(reviewer2)

print(all_grades_students(lst_students, 'python'))
print(all_grades_lekturer(lst_lekturer, 'git'))

print(student1 > student2)
print(lekt1 >= lekt2)

