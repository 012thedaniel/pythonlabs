from abstract_classes import ICourse, ILocalCourse, IOffsiteCourse, ITeacher, ICourseFactory
from sql import select_info_from_database, insert_delete_update_info_in_database


def check_str(value, variable):
    if not isinstance(value, str):
        raise TypeError(f'the value u pass as a {variable} must be a string')
    if len(value) < 2:
        raise ValueError(f'the value u pass a {variable} must contain at least 2 characters')
    if not value:
        raise ValueError(f'the value u pass a {variable} can\'t be empty')


def check_id(value, variable):
    if not isinstance(value, int):
        raise TypeError(f'the value u pass as a {variable} must be an integer')
    if value < 0:
        raise ValueError(f'the value u pass as a {variable} can\'t be less than zero')


def check_teacher(value):
    if not select_info_from_database(f'SELECT * FROM `teacher` WHERE `teacher\'s id` = %s', value):
        raise ValueError(f'there is no such teacher, that u are trying to set to this course')


class Teacher(ITeacher):
    def __init__(self, teachers_id):
        self.__teachers_id = teachers_id

    @property
    def name(self):
        return select_info_from_database(f'SELECT `teacher\'s full name` FROM `teacher` WHERE `teacher\'s id` = %s;',
                                         self.__teachers_id)[0][0]

    @name.setter
    def name(self, value):
        check_str(value, 'teacher\'s full name')
        insert_delete_update_info_in_database(f'UPDATE `teacher` SET `teacher\'s full name` = %s '
                                              f'WHERE `teacher\'s id` = %s;', (value, self.__teachers_id))

    @property
    def courses(self):
        return select_info_from_database(f'SELECT `course\'s name`, `program` FROM `course` '
                                         f'WHERE `teacher\'s id` = %s;', self.__teachers_id)

    def __str__(self):
        text = f'teacher: {self.name}\ncourses:\n'
        if not self.courses:
            return text + f'\tnot found\n'
        courses = iter(self.courses)
        for course in courses:
            text += f'\tname: {course[0]}, program: {course[1]}\n'
        return text + f'\n'


class Course(ICourse):
    def __init__(self, course_id):
        self.__course_id = course_id

    @property
    def name(self):
        return select_info_from_database(f'SELECT `course\'s name` FROM `course` WHERE `course\'s id` = %s;',
                                         self.__course_id)[0][0]

    @name.setter
    def name(self, value):
        check_str(value, 'course\'s name')
        insert_delete_update_info_in_database(f'UPDATE `course` SET `course\'s name` = %s '
                                              f'WHERE `course\'s id` = %s;', (value, self.__course_id))

    @property
    def program(self):
        return select_info_from_database(f'SELECT `program` FROM `course` WHERE `course\'s id` = %s;',
                                         self.__course_id)[0][0]

    @program.setter
    def program(self, value):
        check_str(value, 'program')
        insert_delete_update_info_in_database(f'UPDATE `course` SET `program` = %s '
                                              f'WHERE `course\'s id` = %s;', (value, self.__course_id))

    @property
    def teacher(self):
        return select_info_from_database(f'SELECT teacher.`teacher\'s full name` FROM `course` JOIN `teacher` ON '
                                         f'course.`teacher\'s id` = teacher.`teacher\'s id` WHERE '
                                         f'course.`course\'s id` = %s', self.__course_id)[0][0]

    @teacher.setter
    def teacher(self, value):
        check_id(value, f'teacher\'s id')
        check_teacher(value)
        insert_delete_update_info_in_database(f'UPDATE `course` SET `teacher\'s id` = %s WHERE `course\'s id` = %s;',
                                              (value, self.__course_id))


class LocalCourse(Course, ILocalCourse):
    def __init__(self, course_id):
        super().__init__(course_id)

    def __str__(self):
        return f'course: {self.name}\n' \
               f'program: {self.program}\n' \
               f'teacher: {self.teacher}\n'


class OffsiteCourse(Course, IOffsiteCourse):
    def __init__(self, course_id):
        super().__init__(course_id)

    def __str__(self):
        return f'course: {self.name}\n' \
               f'program: {self.program}\n' \
               f'teacher: {self.teacher}\n'


class CourseFactory(ICourseFactory):
    @staticmethod
    def create_teacher(name, teachers_id):
        check_id(teachers_id, f'teacher\'s id')
        result = select_info_from_database(f'SELECT `teacher\'s full name` FROM `teacher` '
                                           f'WHERE `teacher\'s id` = %s;', teachers_id)
        if not result:
            check_str(name, 'teacher\'s full name')
            insert_delete_update_info_in_database(f'INSERT INTO `teacher` (`teacher\'s full name`, `teacher\'s id`) '
                                                  f'VALUES (%s, %s);', (name, teachers_id))
        else:
            if result[0][0] != name:
                raise ValueError(f'the teacher with such an id already exists, but the name u passed to this function'
                                 f'differs from the one that was found in database by the id u passed')
        return Teacher(teachers_id)

    @staticmethod
    def create_course(name, course_id, course_type_id, id_teacher, program):
        check_id(course_id, f'course\'s id')
        result = select_info_from_database(f'SELECT `course\'s name`, `course\'s type id`, `teacher\'s id`, `program` '
                                           f'FROM `course` WHERE `course\'s id` = %s', course_id)
        if not result:
            check_str(name, f'course\'s name')
            if course_type_id not in (1, 2):
                raise ValueError(f'variable \'course_id\' can take only two parameters(1, 2). '
                                 f'other parameters aren\'t allowed')
            check_id(id_teacher, f'id_teacher')
            if not select_info_from_database(f'SELECT * FROM `teacher` WHERE `teacher\'s id` = %s', id_teacher):
                raise ValueError(f'there is no such teacher, that u are trying to set to the course')
            check_str(name, f'program')
            insert_delete_update_info_in_database(f'INSERT INTO `course` (`course\'s name`, `course\'s type id`, '
                                                  f'`teacher\'s id`, `program`, `course\'s id`) VALUES '
                                                  f'(%s, %s, %s, %s, %s);',
                                                  (name, course_type_id, id_teacher, program, course_id))
        else:
            if result[0][0] != name or result[0][1] != course_type_id or \
                    result[0][2] != id_teacher or result[0][3] != program:
                raise ValueError(f'the course with such an id already exists, but the values of variables '
                                 f'that u passed differ from ones, that are stored in db')
        course_type_dict = {1: LocalCourse,
                            2: OffsiteCourse}
        return course_type_dict[course_type_id](course_id)
