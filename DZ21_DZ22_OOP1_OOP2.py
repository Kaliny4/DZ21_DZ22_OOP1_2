"""
DZ_21
Создать родительский класс auto, у которого есть атрибуты:
brand, age, cоlor, mark и weight.
А так же методы: move, birthday и stop.
Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
Атрибуты brand, age и mark являются обязательными при объявлении объекта.
"""
"""
DZ_22
Создать 2 класса truck и car, которые являются наследниками класса auto 
из предыдущего домашнего задания.
Класс truck имеет дополнительный обязательный атрибут max_load.
Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention», 
его реализацию сделать при помощи оператора super.
А так же дополнительный метод load. При его вызове происходит пауза 1 сек., 
затем выдаётся сообщение «load» и снова пауза 1 сек.
Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
метода move, после появления надписи «move» должна появиться надпись
«max speed is <max_speed>». Вместо <max_speed> должно выводится значение 
обязательного атрибума max_speed.
Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.
"""

import time
#DZ_21
class Auto(object):
#атрибути класу
    brand = None
    age = 0
    cоlor = None
    mark = None
    weight = 0

#атрибути обєкту які призначаються через функцію-конструктор,
# де три з них позиційні і обовязкові і два за замовчуванням (необовязкові)
    def __init__(self, brand, age, mark, cоlor='white', weight=0):
        self.brand = brand
        self.age = age
        self.color = cоlor
        self.mark = mark
        self. weight = weight

#методи обєкту
    def birthday(self):
        print('age before birthday: ', self.age)
        self.age += 1
        print('age after birthday: ', self.age)

    def move(self):
        print('Move')

    def stop(self):
        print('Stop')


auto1 = Auto('brand_test', 10, 'mark_test')  #задаєм тільки три обовязкові аргументи
auto1.birthday()
auto1.move()
auto1.stop()
print('*' * 100)

#DZ_22
# наслідування


class Truck(Auto):
    max_load = 0

    def __init__(self, brand, age, mark, max_load, cоlor=None, weight=0):
        super().__init__(brand, age, mark, cоlor, weight)
        self.max_load = max_load

    def move(self):
        print('Attention')
        super().move()

    def load(self):
        time.sleep(1)
        print('Load')
        time.sleep(1)


truck1 = Truck('Renault', 9, '3s', 4000)
truck2 = Truck('Peugeot', 15, '5m', 8000)
print('truck1 - Brand, Age, Mark, Max_load, Color, Weight -'
      , truck1.brand
      , truck1.age
      , truck1.mark
      , truck1.max_load
      , truck1.color
      , truck1.weight)
print('*' * 100)
print('truck2 - Brand, Age, Mark, Max_load, Color, Weight -'
      , truck2.brand
      , truck2.age
      , truck2.mark
      , truck2.max_load
      , truck2.color
      , truck2.weight)
print('*' * 100)
print('methods truck1:')
truck1.birthday()
truck1.move()
truck1.load()
truck1.stop()
print('*' * 100)
print('methods truck2:')
truck2.birthday()
truck2.move()
truck2.load()
truck2.stop()
print('*' * 100)


class Car(Auto):
    max_speed = 0

    def __init__(self, brand, age, mark, max_speed, cоlor=None, weight=0):
        super().__init__(brand, age, mark, cоlor, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print('max speed is', self.max_speed)


car1 = Car('Citroen', 2, 'H', 200, cоlor='white', weight=2000)
car2 = Car('Bugatti', 5, 'W', 400, cоlor='red', weight=1500)
print('car1 - Brand, Age, Mark, Max_speed, Color, Weight -'
      , car1.brand
      , car1.age
      , car1.mark
      , car1.max_speed
      , car1.color
      , car1.weight)
print('*' * 100)
print('car2 - Brand, Age, Mark, Max_speed, Color, Weight -'
      , car2.brand
      , car2.age
      , car2.mark
      , car2.max_speed
      , car2.color
      , car2.weight)
print('*' * 100)
print('methods car1:')
car1.birthday()
car1.move()
car1.stop()
print('*' * 100)
print('methods car2:')
car2.birthday()
car2.move()
car2.stop()
