class Man:

    def __init__(self):
        self._age = 10

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if self._age < 18:
            self._age = value
            raise ValueError


a = Man()
a.age = 100
