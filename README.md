# DZ21_DZ22_OOP1_2
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
