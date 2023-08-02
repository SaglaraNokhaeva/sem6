def queens(my_str):

# Разбиваем строку в список, содержащий позиции ферзей
    _ = my_str.split()
    newlist = []
    for x in range(0, 16, 2):
        innerlist = []
        innerlist.append(_[x])
        innerlist.append(_[x+1])
        newlist.append(innerlist)
    print(newlist)





queens('1 2 7 3 4 5 7 9 2 3 4 5 6 8 2 1')
