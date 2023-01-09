from classes import CourseFactory

if __name__ == "__main__":
    teacher1 = CourseFactory.create_teacher('Sidorov Vasiliy', 11)
    teacher2 = CourseFactory.create_teacher('Ivanov Ivan', 1)
    course1 = CourseFactory.create_course('Python', 1, 1, 1, 'oop')
    course2 = CourseFactory.create_course('Java', 2, 1, 2, 'oop')
    course3 = CourseFactory.create_course('C basics', 3, 1, 1, 'oop')
    print(course1)
    print(teacher1)
    print(teacher2)
