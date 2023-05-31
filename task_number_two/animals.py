class Animals:
    def __init__(self, name, color, voice):
        self.name = name
        self.color = color
        self.voice = voice

    def says_something(self):
        return f"It says {self.voice}."


class Cow(Animals):
    def __init__(self, name, color, voice):
        super().__init__(name, color, voice)


class Cat(Animals):
    def __init__(self, name, color, voice):
        super().__init__(name, color, voice)


class Dog(Animals):
    def __init__(self, name, color, voice):
        super().__init__(name, color, voice)


cow = Cow("Cow", "White", "Mu-mu")
cat = Cat("Cat", "Black", "Meow")
dog = Dog("Dog", "Brown", "Woof")

print(f"{cow.name} is {cow.color}. {cow.says_something()}")
print(f"{cat.name} is {cat.color}. {cat.says_something()}")
print(f"{dog.name} is {dog.color}. {dog.says_something()}")
