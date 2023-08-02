import random

# print(random_queens())

def arrangements(count):
    def random_queens():

        # Разбиваем строку в список, содержащий позиции ферзей
        global list_position
        list_position = []
        for _ in range(0, 8):
            innerlist = []
            innerlist.append(random.randint(1, 8))
            innerlist.append(random.randint(1, 8))
            list_position.append(innerlist)
        # print(list_position)

        # Проверяем бьют ли ферзи друг друга

        flag = False
        for i in range(len(list_position) - 1):
            for j in range(i + 1, len(list_position)):
                if list_position[i][0] == list_position[j][0] or list_position[i][1] == list_position[j][1] or abs(
                        int(list_position[i][0]) - int(list_position[j][0])) == abs(
                        int(list_position[i][1]) - int(list_position[j][1])):
                    flag = True
        if flag:
            result = False
        else:
            result = True
        return result

    while count > 0:
        # print(random_queens())
        if random_queens():
            print(list_position)
            count -= 1

print(arrangements(4))