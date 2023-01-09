from abc import ABC, abstractmethod


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def courses(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourse(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @property
    @abstractmethod
    def program(self):
        pass

    @program.setter
    @abstractmethod
    def program(self, value):
        pass

    @property
    @abstractmethod
    def teacher(self):
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value):
        pass


class ILocalCourse(ABC):
    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ABC):
    @abstractmethod
    def __str__(self):
        pass


class ICourseFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_course(name, course_id, course_type_id, id_teacher, program):
        pass

    @staticmethod
    @abstractmethod
    def create_teacher(name, teachers_id):
        pass
