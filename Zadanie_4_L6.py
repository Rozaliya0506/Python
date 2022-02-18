class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go!')

    def stop(self):
        print('Stop!')

    def turn(self, direction):
        print(f'Car turn on {direction}!')

    def show_speed(self):
        print(f'Speed of car is = {self.speed}')

class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('Speed exceeded!')

class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('Speed exceeded!')


class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town = TownCar(45, 'red', 'Town')
sport = SportCar(150, 'black', 'Fred')
work = WorkCar(70, 'white', 'Job')
police = PoliceCar(100, 'sky', 'Police')

town.show_speed()
sport.show_speed()
work.show_speed()
police.show_speed()

sport.turn('right')
work.turn('left')
town.go()
police.stop()




