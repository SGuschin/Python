import time


class TrafficLight:
    def __init__(self):
        self.__color = ['Red', 'Yellow', 'Green']

    def running(self, timing):
        for index, i in enumerate(timing):
            print(self.__color[index])
            time.sleep(i)


light = TrafficLight()
light.running([7, 2, 1])
