

class Person:

    def __init__(self, name, surname, email, gender, likes=None):
        self.name = name
        self.surname = surname
        self.email = email
        self.gender = gender
        self.likes = likes

    def __str__(self):
        return "{} {}".format(self.name, self.surname)

    def to_long_str(self):
        return "name: {} | surname: {} | email: {} | likes: {}".format(self.name, self.surname, self.email, self.likes)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.name == other.name and self.surname == other.surname:
            return True
        return False