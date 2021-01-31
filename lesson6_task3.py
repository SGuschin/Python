class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        if float(self._income["wage"]) <= 0:
            raise Exception('Зарплата должна быть больше 0 !')


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        print(full_name + ' - ' + self.position)

    def get_total_income(self):
        total_income = sum(self._income.values())
        print(total_income)


income = {"wage": 25000, "bonus": 5000}

worker1 = Position('Ivan', 'Usovich', 'sale_manager', income)
worker1.get_full_name()
worker1.get_total_income()

try:
    income = {"wage": -45000, "bonus": 5000}
    worker2 = Position('Petr', 'Usmanov', 'sale_manager', income)
    worker2.get_full_name()
    worker2.get_total_income()
except Exception as ex:
    print(ex)
