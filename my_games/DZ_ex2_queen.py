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
            if list_position[i][0] == list_position[j][0] or list_position[i][1] == list_position[j][1] or abs(int(list_position[i][0]) - int(list_position[j][0])) == abs(int(list_position[i][1]) - int(list_position[j][1])):
                flag = True
    if flag:
        result = False
    else:
        result = True

    return result



print(queens('1 1 2 6 3 8 4 3 5 7 6 4 7 2 8 5'))
print(queens('1 3 2 5 3 2 4 8 5 1 6 7 7 4 8 6'))

