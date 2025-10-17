from app.logic import average_rating, avg_by_stat, sorting
from pathlib import Path

tests = Path(__file__).parent / "data"


def test_sorting():
    assert sorting([('a', '1.0'), ('b', '2.0')]) == [('b', 2.0), ('a', 1.0)]


def test_sorting_type():
    types = []
    types.append(sorting('1'))
    types.append(sorting(1))
    types.append(sorting(['a', 'b']))
    types.append(sorting([['a', 'b'], ['a', 'b']]))
    assert all(isinstance(obj, str) for obj in types)


def test_data():
    assert average_rating(f'{tests}/products.csv') == 'Объект должен быть str(num)'