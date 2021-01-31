class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is riding')

    def stop(self):
        print(f'{self.name} is stoping')

    def turn(self, turn):
        print(f'{self.name}  is turning on {turn}')

    def show_speed(self):
        print(f'{self.name} speed {self.speed}')



class TownCar(Car):
    def show_speed(self):
        print(f'{self.name} speed {self.speed}')
        if self.speed >= 40:
            print('Вы превысили ограничение скорость в 40 км/ч !')

class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f'{self.name} speed {self.speed}')
        if self.speed >= 60:
            print('Вы превысили ограничение скорость в 60 км/ч !')


class PoliceCar(Car):
    pass


a = Car(39, 'green', 'BMW', False)
a.show_speed()
a.go()
b = WorkCar(65, 'red', 'Volkswagen', False)
b.show_speed()
b.stop()
c = TownCar(90, 'green', 'Mercedes', True)
c.show_speed()
c.stop()
d = SportCar(30, 'green', 'Skoda', True)
d.show_speed()
d.go()
d.turn('right')
d.go()

