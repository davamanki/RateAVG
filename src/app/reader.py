import csv
from pathlib import Path

# Валидируем файл
def check_csv(file_path):
    if not isinstance(file_path, str):
        return "Ошибка: Ожидается путь к файлу: str"
    if len(file_path) < 5 or file_path[-4:] != ".csv":
        return "Ошибка: Вид файла не поддерживается."
    if not Path(file_path).exists():
        return "Ошибка: Файл не найден."
    return 'OK'


def csv_dict_to_list(args)-> list | str:
    if isinstance(args, str):
        args = [args]
    if args is None:
        return 'Объект должен быть str.'
    for arg in args:
        if "Ошибка" in check_csv(arg):
            print(arg)
            return check_csv(arg)

    rows = [] # Создаём список для заполнения данными

    for arg in args: # Проходимся по файлам с путями
        with open(arg, 'r') as file:
            reader = csv.DictReader(file) # Открываем .csv файл в виде словаря

            for row in reader: # Заполняем список данными (словари)
                rows.append(row)


    return rows
