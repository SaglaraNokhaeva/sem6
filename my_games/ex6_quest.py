from random import choice

_answers_count = {}


def quest(question, answers, try_count):
    count = try_count
    while try_count > 0:
        print('Осталось попыток: ', try_count, question),
        try_count -= 1
        answer = input("Введите ваш ответ: ")
        if answer in answers:
            _answers_count[question] = count - try_count
            print(f'Бинго, вы угадали!!! № попытки: {count - try_count}')
            break
        else:
            print('Ответ неверен.')
    else:
        print('Исчерпаны все попытки. Сожалею.')
        quit()


def more_quests(iters):
    quests = {'Сколько ног у муравья?': ['4', '5', '6'],
              'Какого цвета огнетушитель?': ['Красный', 'Синий'],
              'Сколько лет тебе было в детстве?': [str(i) for i in range(19)],
              'Идут два крокодила, один зелёный, другой направо. Зачем мне холодильник, если я не курю?': ['Да',
                                                                                                           'Гладиолус']}
    for i in range(iters):
        temp = choice(list(quests.keys()))
        quest(temp, quests[temp], 3)


def how_many_answers():
    print(*(f'Загадка {key[:15]} ... была отгадана за {value} попыток' for key, value in _answers_count.items()),
          sep='\n')
