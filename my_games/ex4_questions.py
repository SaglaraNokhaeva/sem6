def quest(question, answers, try_count):
    count = try_count
    while try_count > 0:
        print('Осталось попыток: ', try_count, question),
        try_count -= 1
        answer = input("Введите ваш ответ: ")
        if answer in answers:
            print(f'Бинго, вы угадали!!! № попытки: {count - try_count}')
            break
        else:
            print('Ответ неверен.')
    else:
        print('Исчерпаны все попытки. Сожалею.')
        quit()