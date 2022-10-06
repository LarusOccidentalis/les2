#1. Создать класс TrafficLight (светофор).
#определить у него один атрибут color (цвет) и метод running (запуск);атрибут реализовать как приватный;
#в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
#продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
#переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
#проверить работу примера, создав экземпляр и вызвав описанный метод.
#Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

#Сделать один атрибут и метод (ф-цию), без дочерних
from time import sleep
class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']
    def running (self):
        i = 0
        while i < 15:
            if i == 0:
                sleep(7)
                i += 1
                print("Загорелся красный сингал светофора")
                continue
            elif i == 1:
                sleep(5)
                i += 1
                print("Загорелся желтый сингал светофора")
                continue
            elif i == 2:
                sleep(10)
                i += 1
                print("Загорелся зеленый сингал светофора")
                continue
            else:
                break
TrafficLight = TrafficLight()
TrafficLight.running()

#2. Реализовать класс Road (дорога).
#определить атрибуты: length (длина), width (ширина);
#значения атрибутов должны передаваться при создании экземпляра класса;
#атрибуты сделать защищёнными;
#определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
#использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см*число см толщины полотна;
#проверить работу метода.
#Например: 20 м*5000 м*25 кг*5 см = 12500 т.
class Road:
    __length = None
    __width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def intake(self):
        self.weigth = 25
        self.tickness = 0.05
        intake = self.length * self.width * self.weigth * self.tickness / 1000
        print(f'Need {intake} ton for the building')

road_to_village = Road(20, 5000)
road_to_village.intake()







#3. Реализовать базовый класс Worker (работник).
#определить атрибуты: name, surname, position (должность), income (доход);
#последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
#создать класс Position (должность) на базе класса Worker;
#в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
#проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    name = None
    surname = None
    position = None
    profit = None
    bonus = None

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.profit = profit
        self.bonus = bonus


class Position(Worker):
    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        return self.name + self.surname

    def get_full_profit(self):
        self.__income = {'profit': self.profit, 'bonus': self.bonus}
        return self.__income


manager = Position('Д', 'Гал', 'ПЦР-разраб', 100, 10000)
print(manager.get_full_name(), manager.get_full_profit())

#4. Реализуйте базовый класс Car.
#у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать,
#что машина поехала, остановилась, повернула (куда);
#опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.
class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "The car went"
    def stop(self):
        return "The car has stopped"
    def turn(self, direction):
        return "The car turned to " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

ford = TownCar('Ford', 60, 'black')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('City'), ford.stop())
sport = SportCar('Ford', 180, 'red')
work1 = WorkCar('Ford', 90, 'white', True)
work2 = WorkCar('Audi', 90, 'white', False)
police = PoliceCar('Ford', 180, 'red')

#5. Реализовать класс Stationery (канцелярская принадлежность).
#определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
#создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
#в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
#создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    title = 'Title'
    def draw(self):
        print('Вы рисуете')
class Pen(Stationery):
    def draw(self):
        print('Вы рисуете ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Вы рисуете карандашом')
class Handle(Stationery):
    def draw(self):
        print('Вы рисуете маркером, вам нравится')

my_pen = Pen()
my_pencil = Pencil()
my_handle = Handle()
my_pen.draw()
my_pencil.draw()
my_handle.draw()