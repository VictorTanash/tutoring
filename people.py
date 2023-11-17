class Person:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


class Teacher(Person):
    competences = []
    group_ids = []

    def add_competence(self, competence: str):
        self.competences.append(competence)

    def get_competences(self):
        return self.competences

    def add_group(self, group_id: int):
        # need to implement checking for correct id
        self.group_ids.append(group_id)

    def close_group(self, group_id):
        # need to implement checking if id exists in teacher's groups
        self.group_ids.remove(group_id)


class Client(Person):
    discount = 0

    def __init__(self, name: str, discount=0):
        super().__init__(name)
        self.name = name
        self.discount = discount

    def set_discount(self, new_discount):
        self.discount = new_discount

    def get_discount(self):
        return self.discount


class Student(Person):
    def __init__(self, name: str, parent: Client):
        super().__init__(name)
        self.name = name
        self.parent = parent.get_name()


class Administrator(Person):
    monthly_salary = 0

    def set_monthly_salary(self, new_salary: int):
        self.monthly_salary = new_salary

    def get_monthly_salary(self):
        return self.monthly_salary
