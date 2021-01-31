class Stationery:
    title = "Pencil"

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):
    def draw(self):
        print('Запуск отрисовки маркером')


my_stationery = Stationery()
my_stationery.draw()
my_pen = Pen()
my_pen.draw()
my_pencil = Pencil()
my_pencil.draw()
my_handle = Handle()
my_handle.draw()
