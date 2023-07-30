# Задание №2
# � Создайте модуль с функцией внутри. Функция принимает на вход три целых числа:
# нижнюю и верхнюю границу и количество попыток.
# � Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за
# заданное число попыток.
# � Функция выводит подсказки “больше” и “меньше”. Если число угадано, возвращается истина, а если
# попытки исчерпаны - ложь.

from random import randint

def guess_num (lower_limil, upper_limit, count):
    """
    Угадайка

    :param lower_limil:
    :param upper_limit:
    :param count:
    :return:
    """

    num = randint(lower_limil, upper_limit)
    while count > 0:
        print('Попытка № ', count)
        count -= 1

        attempt = float(input('Угадайте число между ' + str(lower_limil) + ' и ' + str(upper_limit) + ': '))
        if attempt < num:
            print('Больше')
        elif attempt > num:
            print('Меньше')
        else:
            break
    else:
        print('Исчерпаны все попытки. Сожалею.')
        quit()
    print('Вы угадали! Поздравляем!')

if __name__ == '__main__':
    pass