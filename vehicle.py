class Vehicle:
    vehicle_type = "none"


# Создаем родительский класс Car, который наследуется от класса Vehicle
class Car(Vehicle):
    # Устанавливаем свойство price
    price = 1000000

    # Функция для получения свойства
    def horse_powers(self):
        return 320


# Создаем класс Nissan, который наследуется от классов Car и Vehicle
class Nissan(Car, Vehicle):
    # Переопределяем свойство price
    price = 900000
    # Переопределяем свойство vehicle_type
    vehicle_type = 'Audi'


# Переопределяем функцию horse_powers
def horse_powers(self):
    return 280


# Создаем экземпляр класса Nissan
nissan = Nissan()
# Выводим на печать
print(nissan.vehicle_type)
print(nissan.price)
