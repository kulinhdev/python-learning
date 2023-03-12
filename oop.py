class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative.")
        self._age = age


person1 = Person("Alice", 30)
print(person1.name)
person1.name = "Bob"
print(person1.name)
print(person1.age)
person1.age = 35
print(person1.age)
