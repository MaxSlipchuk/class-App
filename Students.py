# Запрограмуй клас Student:
# 1) Створи конструктор класу. 
# Він повинен створювати студента з властивостями: ім'я, середній бал (передаються в конструктор) та курс, 
# що відвідується за вибором (за замовчуванням «-»).
# 2) Створи метод, який друкує інформацію про студента. Він повинен виводити дані як на картинці.
# 3) Створи метод, який встановлює курс на вибір. Назва курсу має запитуватися з клавіатури та зберігатися як властивість об'єкта.
# Створи екземпляр класу Student з ім'ям «Степанова Дар'я», середнім балом «4.8» та без курсу на вибір. 
# Надрукуй інформацію про об'єкт. Потім встанови курс на вибір «Астрономія» та надрукуй оновлену інформацію.

class Student():
    #конструктор
    def __init__(self, name, score, curriculum):
        self.name = name
        self.score = score
        self.curriculum = curriculum

    #друк інформації
    def student_information(self):
        print("Студент(-ка)", self.name)
        print("Має середній бал:", self.score)
        print("Відвідує курс на вибір:", self.curriculum)

    #встановити курс на вибір
    def curriculum_choise(self):
        self.curriculum = input("Введіть назву курсу: ")

student = Student("Степанова Дар'я", '4.8', '-')

#друк інформації про студента
student.student_information()

#встановити курс на вибір "Астрономія"
student.curriculum_choise()

#друк інформації про студента
student.student_information()
