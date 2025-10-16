class Person:
    def __init__(self, name, surname):
        self._name=name
        self._surname=surname
    @property
    def name(self):
        return self._name

    @property
    def fullname(self):
        return f"{self._name} {self._surname}"


    @name.setter
    def name(self, value):
        self._name=value

    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname (value, self):
        self._surname=value

    @fullname.setter  
    def fullname (value, self):
        name, surname=value.split('', 1)
        self._name=name
        self._surname=surname

person = Person('Меган', 'Фокс') 
 
print(person.name) 
print(person.surname) 
print(person.fullname)

