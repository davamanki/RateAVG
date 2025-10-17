from pathlib import Path
from app.reader import csv_dict_to_list

tests = Path(__file__).parent / "data"


def test_csv_str():
    assert csv_dict_to_list([12345])=="Ошибка: Ожидается путь к файлу: str"

def test_is_csv():
    assert csv_dict_to_list(['not_file'])=="Ошибка: Вид файла не поддерживается."

def test_csv_exists():
    assert csv_dict_to_list(["not_file.csv"])=="Ошибка: Файл не найден."

def test_rows():
    paths = [f'{tests}/products1.csv', f'{tests}/products2.csv']
    data = csv_dict_to_list(paths)
    assert ({'name': 'iphone 15 pro', 'brand': 'apple', 'price': '999', 'rating': '4.9'} in data
            and {'name': 'iphone 13 mini', 'brand': 'apple', 'price': '599', 'rating': '4.5'} in data)



def test_none():
    assert csv_dict_to_list(None)=='Объект должен быть str.'