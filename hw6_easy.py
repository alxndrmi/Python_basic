# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)


class TownCar:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(self.name, 'is going')

    def stop(self):
        print(self.name, 'has stopped')

    def turn(self, direction):
        print(self.name, 'has turned', direction)


class SportCar:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(self.name, 'is going')

    def stop(self):
        print(self.name, 'has stopped')

    def turn(self, direction):
        print(self.name, 'has turned', direction)


class WorkCar:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(self.name, 'is going')

    def stop(self):
        print(self.name, 'has stopped')

    def turn(self, direction):
        print(self.name, 'has turned', direction)


class PoliceCar:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(self.name, 'is going')

    def stop(self):
        print(self.name, 'has stopped')

    def turn(self, direction):
        print(self.name, 'has turned', direction)


town_car1 = TownCar('Toyota Camry', 'black', '40', False)
town_car1.go()
town_car1.turn('right')
town_car1.stop()

police_car1 = PoliceCar('Vaz 2114', 'gray', '60', True)
police_car1.go()
police_car1.turn('left')
police_car1.turn('right')
police_car1.stop()

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

# отступ + отделяющая линия
print()
print('_' * 100)
print()


class Car:
    def __init__(self, name, color, speed, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(self.name, 'is going')

    def stop(self):
        print(self.name, 'has stopped')

    def turn(self, direction):
        print(self.name, 'has turned', direction)


class TownCar(Car):
    pass


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police):
        super().__init__(name, color, speed, is_police)
        print(self.name, 'police alarm lights and sound is on')


town_car2 = TownCar('Ford Focus', 'white', '80', False)
town_car2.go()
town_car2.turn('right')
town_car2.go()
town_car2.stop()

sport_car2 = SportCar('Aston Martin', 'red', '120', False)
sport_car2.go()
sport_car2.stop()

work_car2 = WorkCar('Gazel', 'blue', '40', False)
work_car2.go()
work_car2.turn('right')
work_car2.go()
work_car2.stop()
work_car2.go()
work_car2.turn('left')
work_car2.go()
work_car2.turn('right')
work_car2.go()
work_car2.turn('left')
work_car2.go()
work_car2.stop()

police_car2 = PoliceCar('Porsche Cayenne', 'gray', '60', True)
police_car2.go()
police_car2.turn('left')
police_car2.go()
police_car2.turn('right')
police_car2.go()
police_car2.stop()