class User:
    def __init__(self, name, age):
        if not (isinstance(name, str) and name.isalpha() and name):
            raise ValueError("Некорректное имя")
        if not (isinstance(age, int) and 0 <= age <= 110):
            raise ValueError("Некорректный возраст")
        self._name = name
        self._age = age

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if not (isinstance(new_name, str) and new_name.isalpha() and new_name):
            raise ValueError("Некорректное имя")
        self._name = new_name

    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if not (isinstance(new_age, int) and 0 <= new_age <= 110):
            raise ValueError("Некорректный возраст")
        self._age = new_age
user = User('Гвидо', 67) 
 
print(user.get_name()) 
print(user.get_age()) 