_month_dict = {31: [1, 3, 5, 7, 8, 10, 12], 30: [4, 6, 9, 11]}


def chek_date(inp_year):
    day, month, year = map(int, inp_year.split('.'))
    if 0 < year <= 9999 and 0 < month < 13 and 0 < day < 32:
        if month != 2:
            if day in _month_dict:
                return month in _month_dict[day]
            else:
                return True
        else:
            if _chek_year(year):
                return day < 29
            else:
                return day < 30


def _chek_year(year):
    if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
        print('Обычный год')
        return True
    else:
        print('Високосный год')
        return False


if __name__=='__main__':
    print(chek_date(input('Введите дату в формате DD.MM.YYYY: ')))