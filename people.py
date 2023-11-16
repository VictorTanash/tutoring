class Person:
    def __init__(self, name: str):
        self.name = name

    def get_name(self):
        return self.name


class Teacher(Person):
    competences = []

    def add_competence(self, competence: str):
        self.competences.append(competence)

    def get_competences(self):
        return self.competences


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
    def __init__(self, name: str, parent: Client) -> object:
        super().__init__(name)
        self.name = name
        self.parent = parent.get_name()


class Administrator(Person):
    pass
