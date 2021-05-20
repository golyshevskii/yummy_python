# Есть Марсианин, характеристиками которого являются:
# 1. Имя
# 2. Возраст
# 3. Наличие кислорода
# 4. Наличие собственного звездного-корабля
#
# Марсианин может:
# 1. Предоставить информацию о себе
# 2. Заработать кислород
# 3. Купить звездный корабль
#
# Также же есть звездный корабль, к свойствам которого относятся:
# 1. Площадь
# 2. Стоимость
#
# Для звездного корабля можно:
# 1. Применить скидку на покупку
# Также есть  Типовы звездные корабли, обязательной площадью 30м2.
#
# Класс Martian
# 1. Создайте класс Martian.
# 2. Определите для него два статических поля: default_name и default_age.
# 3. Создайте метод __init__(), который помимо self принимает еще два параметра: name и age.
#    Для этих параметров задайте значения по умолчанию, используя свойства default_name и default_age.
#    В методе __init__() определите четыре свойства: Публичные - name и age. Приватные - oxygen и spaceship.
# 4. Реализуйте справочный метод info(), который будет выводить поля name, age, spaceship и oxygen.
# 5. Реализуйте справочный статический метод default_info(), который будет выводить статические
#    поля default_name и default_age.
# 6. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки spaceship:
#    уменьшать количество кислорода на счету и присваивать ссылку на только что купленный spaceship.
#    В качестве аргументов данный метод принимает объект звездного корабля и его цену.
# 7. Реализуйте метод earn_oxygen(), увеличивающий значение свойства oxygen.
# 8. Реализуйте метод buy_spaceship(), который будет проверять, что у марсианина достаточно денег для покупки,
#    и совершать сделку. Если кислорода слишком мало - нужно вывести предупреждение в консоль.
#    Параметры метода: ссылка на звездный корабль и размер скидки
#
# Класс Spaceship
# 1. Создайте класс Spaceship
# 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price.
# 3. Свои начальные значения они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и
#    возвращает цену с учетом данной скидки.
#
# Класс StandardSpaceShip
# 1. Создайте класс StandardSpaceShip, унаследовав его функционал от класса Spaceship
# 2. Внутри класса StandardSpaceShip переопределите метод __init__() так, чтобы он создавал объект с площадью 30м2
#
# Тесты
#
# 1. Вызовите справочный метод  default_info() для класса Human()
# 2. Создайте объект класса Human
# 3. Выведите справочную информацию о созданном объекте (вызовите метод info()).
# 4. Создайте объект класса SmallHouse
# 5. Попробуйте купить созданный дом, убедитесь в получении предупреждения.
# 6. Поправьте финансовое положение объекта - вызовите метод earn_money()
# 7. Снова попробуйте купить дом
# 8. Посмотрите, как изменилось состояние объекта класса Human


class Martian:
    default_name = 'Yami'
    default_age = 25

    def __init__(self, name, age):
        name = Martian.default_name
        age = Martian.default_age
        self.name = name
        self.age = age
        self.__oxygen = 0
        self.__spaceship = 0

    def info(self):
        print("""name: {0}
        age: {1}
        oxygen: {2}
        spaceship: {3}""".format(self.name, self.age, self.__spaceship, self.__oxygen))

    @staticmethod
    def default_info():
        print("""name: {0}
        age: {1}""".format(Martian.default_name, Martian.default_age))

    def __make_deal(self, spaceship, price):
        self.__oxygen -= price
        self.__spaceship = spaceship

    def earn_oxygen(self):
        self.__oxygen += 1000

    def buy_spaceship(self, spaceship, price, discount):
        if price - (price * discount) / 100 <= self.__oxygen:
            self.__make_deal(spaceship, price)
        else:
            print('not enough oxygen')


class Spaceship:
    def __init__(self, area, price):
        self.__area = area
        self.__price = price

    def final_price(self, discount: int) -> float:
        return self.__price - (self.__price * discount) / 100

class St
