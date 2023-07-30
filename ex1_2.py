# Задание №1
# � Вспомните какие модули вы уже проходили на курсе.
# � Создайте файл, в котором вы импортируете встроенные
# в модуль функции под псевдонимами. (3-7 строк импорта).

from random import randint as rndint
import math as mt
import numpy as np
from guess_num import guess_num

a = rndint(0, 5)

guess_num(1, 100, 5)
