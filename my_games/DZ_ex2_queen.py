def queens(my_str):

# Разбиваем строку в список, содержащий позиции ферзей
    _ = my_str.split()
    list_position = []
    for x in range(0, 16, 2):
        innerlist = []
        innerlist.append(_[x])
        innerlist.append(_[x+1])
        list_position.append(innerlist)
    print(list_position)

# Проверяем бьют ли ферзи друг друга
    flag = False
    for i in range(len(list_position)-1):
        for j in range(i+1, len(list_position)):
            if list_position[i][0] == list_position[j][0] or list_position[i][1] == list_position[j][1] or abs(list_position[i][0] - list_position[j][0]) == abs(list_position[i][1] - list_position[j][1]):
                flag = True
    if flag:
        result = 'бьёт'
    else:
        result = 'не бьёт'

    return result









queens('1 2 7 3 4 5 7 9 2 3 4 5 6 8 2 1')
