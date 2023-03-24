# клас батько або суперклас
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    # метод, який виводить інформацію по авто
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        print(long_name.title())
    # метод, який змінює пробіг
    def update_odometr(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    # метод, який добавляє до пробігу милі в залежності від того скільки машина проїхала
    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print('Error')
    # метод, який виводить пробіг
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")
# екземпляр класу Car
my_new_car = Car('audi', 'a4', 2016)

# створення субкласу ElectroCar, який унаслідує клас Car
class ElectroCar(Car):
    # метод __init__ отримує інформацію, яка необхідна для створення обєкту Car
    def __init__(self, make, model, year):
        #  super() - спеціальна функція, яка допомагає Phyton звязати суперклас з субкласом
        super().__init__(make, model, year)
        # створення атрибуту, який буде присутній тільки електрокарам
        self.battery_size = 70

        # метод, який показує інформацію по батареї
    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')
# створення екземпляру класа ElectroCar
my_tesla = ElectroCar('teska', 'Model S', 2016)
my_tesla.get_descriptive_name()
my_tesla.describe_battery()