from app import reader

def avg_by_stat(data: list[dict], stat_key: str) -> list:
    count = {}
    brands = {}

    for row in data: # Проходимся по всем строкам
        if row['brand'] not in brands: #Добавляем брэнд, если его нет
            brands[row['brand']] = 0
            count[row['brand']] = 0


        brands[row['brand']] += float(row[stat_key]) # Прибавляем рейтинг устройства к брэнду
        count[row['brand']] += 1

    for key in brands: # Приводим значение рейтинга. Суммарный -> Средний и округляем
        brands[key] = round(brands[key] / count[key], 2)


    brands = dict(sorted(brands.items()))
    brands = [[k, str(v)] for k, v in brands.items()]

    return brands


def no_letter(num):
    if not isinstance(num, str):
        return 'Ожидалась строка.'
    symbols = '0123456789.'
    if not any(obj in symbols for obj in num):
        return 'Объект должен быть str(num)'
    if '.' in num and num.count('.') == 1 and num[0]!='.' and num[-1]!='.':
        return 'OK'
    else:
        return 'Объект должен быть str(num)'


def average_rating(arg, name=None):
    csv_dicts = reader.csv_dict_to_list(arg)
    for obj in csv_dicts:
        if no_letter(obj['rating'])!='OK':
            return no_letter(obj['rating'])
    sorted_rating = avg_by_stat(csv_dicts, 'rating') # Сортируем брэнды по рейтингу
    sorted_rating = sorting(sorted_rating)
    return sorted_rating, name


def sorting(objs) -> list | str : #Сортируем по 1) убыванию рейтинга 2) алфавиту
    if not isinstance(objs, list) or not all(isinstance(obj, tuple) or isinstance(obj, list) for obj in objs):
        return "Неверный тип данных. Ожидался список. list(tuple(str, num | str(num)))"
    for obj in objs:
        if not no_letter(obj[1])=='OK':
            return no_letter(obj[1])

    objs = [(-float(obj[1]), obj[0]) for obj in objs] # Генерируем список кортежей с числами на первом месте для сортировки
    objs = sorted(objs) # Сортируем
    objs = [(obj[1], -obj[0]) for obj in objs] # Генерируем словарь


    return objs


