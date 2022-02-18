class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mas_asph (self, massa, sm):
        return (self._length * self._width * massa * sm)/1000

my_road = Road(5000,20)
print(my_road.mas_asph(25,5))
