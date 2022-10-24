import re


class Student:
    def __init__(self, name, surname, record_book_number, grades):
        self.name = name
        self.surname = surname
        self.record_book_number = record_book_number
        self.grades = grades

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalpha():
            raise Exception(f'Name of the student can only consist of cyrillic/latin letters')
        if len(value) < 2:
            raise Exception(f'Name of the student can\'t contain only 1 letter')
        if not value[0].isupper() or not value[1:].islower():
            raise Exception(f'Name of the student must start with a capital letter '
                            f'and the rest of the letters should be in lowercase')
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not value.isalpha():
            raise Exception(f'Surname of the student can only consist of cyrillic/latin letters')
        if len(value) < 2:
            raise Exception(f'Surname of the student can\'t contain only 1 letter')
        if not value[0].isupper() or not value[1:].islower():
            raise Exception(f'Surname of the student must start with a capital letter '
                            f'and the rest of the letters should be in lowercase')
        self.__surname = value

    @property
    def record_book_number(self):
        return self.__record_book_number

    @record_book_number.setter
    def record_book_number(self, value):
        if not re.fullmatch(r'[А-Я][А-Я]-\d{4}', value):
            raise Exception(f'The value u added can\'t be a record book number')
        self.__record_book_number = value

    @property
    def grades(self):
        return self.__grades

    @grades.setter
    def grades(self, value):
        if not isinstance(value, list):
            raise Exception(f'The value u passed as grades isn\'t a list of grades')
        if not len(value) == 6:
            raise Exception(f'List, that contains grades, must have 6 grades')
        if not all(isinstance(grade, int) and 0 <= grade <= 100 for grade in value):
            raise Exception(f'Each grade must be an integer number somewhere in between 0 and 100')
        self.__grades = value

    def get_average_score(self):
        return sum(self.grades)/len(self.grades)

    def __str__(self):
        return f'Name: {self.surname.ljust(15)} {self.name.ljust(15)}' \
               f'Record book num: {self.record_book_number}\t' \
               f'Grades: {", ".join(map(str, self.grades))}\n'


class Group:
    max_students = 20

    def __init__(self, *args):
        if not args:
            raise Exception(f'U are trying to form group without students')
        self.__students_list = []
        for stud in args:
            self.add_student(stud)

    def add_student(self, student_to_add):
        if not isinstance(student_to_add, Student):
            raise Exception(f'u are trying to add to group someone/something that is not a student')
        if len(self.__students_list) == Group.max_students:
            raise Exception(f'u can\'t add anymore students. there are already {Group.max_students} of them')
        for st in self.__students_list:
            if student_to_add.name == st.name and student_to_add.surname == st.surname:
                raise Exception(f'There can\'t be two students with the same name and surname in one group')
        self.__students_list.append(student_to_add)

    def del_student(self, student_to_del):
        if not isinstance(student_to_del, Student):
            raise Exception(f'u are trying to kick out of the group someone/something that is not a student')
        if len(self.__students_list) == 1:
            raise Exception(f'Group can\'t exist without students, there must remain at least 1 student')
        self.__students_list.remove(student_to_del)

    def get_top_5(self):
        top_5 = sorted(self.__students_list, key=lambda stud: stud.get_average_score(), reverse=True)[:5]
        return f'Top 5 students:\n{"".join(map(str, top_5))}'

    def __str__(self):
        return f'Group:\n{"".join(map(str, self.__students_list))}'


student1 = Student('Daniel', 'Dziuban', 'ТВ-1178', [98, 84, 78, 86, 87, 71])
student2 = Student('Varvara', 'Grebenetska', 'КА-0651', [93, 94, 90, 90, 85, 82])
student3 = Student('Vlad', 'Bilousov', 'ТР-9101', [96, 81, 88, 100, 98, 85])
student4 = Student('Yehor', 'Veprintsev', 'МА-1713', [83, 61, 72, 69, 75, 63])
student5 = Student('Sabina', 'Bleesec', 'СР-2541', [85, 89, 88, 79, 81, 77])
student6 = Student('Marina', 'Haidei', 'ПМ-4899', [83, 81, 79, 92, 73, 77])
student7 = Student('Daria', 'Sadokha', 'ДЕ-7274', [73, 71, 69, 72, 73, 76])
student8 = Student('Denis', 'Pidenko', 'ПР-5532', [63, 61, 69, 82, 73, 66])

my_group = Group(student1, student2, student3, student4, student5, student6, student7)
my_group.add_student(student8)
my_group.del_student(student7)

print(my_group.get_top_5())
print(my_group.__str__())
