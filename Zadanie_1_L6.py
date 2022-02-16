from time import sleep

class TrafficLight:

    colors = ('red', 'yellow', 'green')
    time = (7, 2, 3)

    def __init__(self):
        self.__color = 'green'

    def running(self):
        while True:
            for el in self.colors:
                self.__color = el
                print(self.__color)
                sleep(self.time[self.colors.index(self.__color)])


traffic_light = TrafficLight()
traffic_light.running()
