import customtkinter

# створення класу
class Animal:
    # конструктор класу __init__, який не дозволить створити обєкт з пустими полями
    # self - ссилка на щойно створений обєкт, вона надає конкретному ексземпляру доступ до атрибутів та методів класу
    # він є обовязковим і має передувати усім іншим параметрам
    def __init__(self, species, voice, count_legs):
        # конструктор приймає значення виду, голосу тварини та квлькість ніг
        # тут відбувається збереження через змінні, які потім звязуються з створеним обєктом
        self.species = species
        self.voice = voice
        self.count_legs = count_legs

class Rectangle:
    # з самого початку в конструкторі ми можемо задати значення параметрам
    def __init__(self, w = 0.5, h = 1):
        # конструктор приймає значення ширини та висоти
        self.width = w
        self.height = h
    # метод для вираховування периметру 
    def square(self):
        return self.width * self.height
# створення обєкта/екземпляра класу Rectangle зі зміненами параметрами 
rec = Rectangle(2,5)
# print(rec.square())

class MyAppCTk(customtkinter.CTk):
    def __init__(self, title, fg_color):
        super().__init__(fg_color = fg_color)
        self.title(title)
    
my_app = MyAppCTk(fg_color = "green", title = "App")