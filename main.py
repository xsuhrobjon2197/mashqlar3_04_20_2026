#7-m
class Animal:
    def __init__(self, title, genre):
        self.title = title
        self.ganre = genre

    def make_sound(self):
        print(f"{self.title} {self.ganre}")

s1 = Animal("Mushuk", "Miyovlaydi")
s1.make_sound()

#8-m
class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

    def info(self):
        print(f"Film: {self.title}, Janr: {self.genre}")


s1 = Movie("Avatar", "Fantasty")
s1.info()

#9-m
class Laptop:
    def __init__(self, model, ram):
        self.model = model
        self.ram = ram

    def show_specs(self):
        print(f"{self.model} {self.ram} Ram")


s1 = Laptop("HP", "166GB")
s1.show_specs()
