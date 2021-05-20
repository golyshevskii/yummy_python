# topic - OOP
# title - Tomato
# content:
# Есть Помидор со следующими характеристиками:
# 1. Индекс
# 2. Стадия зрелости(стадии: Отсутствует, Цветение, Зеленый, Красный)
#
# Помидор может:
# 1. Расти (переходить на следующую стадию созревания)
# 2. Предоставлять информацию о своей зрелости
#
# Есть Куст с помидорами, который:
# 1. Содержит список томатов, которые на нем растут
#
# И может:
# 1. Расти вместе с томатами
# 2. Предоставлять информацию о зрелости всех томатов
# 3. Предоставлять урожай
#
# И также есть Садовник, который имеет:
# 1. Имя
# 2. Растение, за которым он ухаживает
#
# И может:
# 1. Ухаживать за растением
# 2. Собирать с него урожай

# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических protected свойства:
#    1) _index - передается параметром и
#    2) _state - принимает первое значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания)
#
# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра количество томатов и на его основе
#    будет создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства
#    tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая
#
# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
#    1) name - передается параметром, является публичным и
#    2) _plant - принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все - садовник собирает урожай.
#    Если нет - метод печатает предупреждение.
#
# Тесты:
# 1. Создайте объекты классов TomatoBush и Gardener
# 2. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 3. Попробуйте собрать урожай
# 4. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 5. Соберите урожай


class Tomato:
    states = {0: 'nothing',
              1: 'flower',
              2: 'green_tomato',
              3: 'red_tomato'}

    def __init__(self, index):
        self.__index = index
        self.__state = 0
        self.i = 0

    def grow(self):
        self.i += 1
        self.__state = Tomato.states[self.i]

    def is_ripe(self) -> bool:
        return self.__state == Tomato.states[3]


class TomatoBush:
    def __init__(self, amount):
        self.amount = amount
        self.tomatoes = [Tomato(i) for i in range(self.amount)]

    def grow_all(self):
        for tomato in self.tomatoes:
            try:
                tomato.grow()
            except KeyError:
                continue

    def all_are_ripe(self) -> bool:
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        if TomatoBush.all_are_ripe(self):
            self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        self.name = name
        self.__plant = plant

    def work(self):
        self.__plant.grow_all()

    def harvest(self):
        if self.__plant.all_are_ripe():
            self.__plant.grow_all()
            print('good job!')
        else:
            print('not all tomatoes are ripe...')


tomatobush = TomatoBush(5)
gardener = Gardener('Kek', tomatobush)
gardener.harvest()
for _ in range(3):
    gardener.work()
gardener.harvest()
