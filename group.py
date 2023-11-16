from people import Student, Teacher


class Group:
    students = []
    price = 0
    study = ''
    teacher = None
    administrator = None

    def __init__(self, group_number: int, study: str):
        self.group_number = group_number
        self.study = study

    def add_student(self, student: Student):
        self.students.append(student)

    def get_group_attendees(self):
        names = []
        for student in self.students:
            names.append(student.get_name())
        return names

    def set_price(self, new_price: int):
        self.price = new_price

    def get_price(self):
        return self.price

    def set_teacher(self, teacher: Teacher):
        self.teacher = teacher

    def set_administrator(self, administrator):
        self.administrator = administrator
