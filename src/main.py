import argparse
from app.logic import average_rating
from tabulate import tabulate
parser = argparse.ArgumentParser()
parser.add_argument(
    "--files",
    nargs="+",                # 1 или множество значений
    required=True,            # *
    help="Пути к CSV-файлам."
)

REPORTS = {
    "average-rating": average_rating,
} # Добавляем словарь с выбором функций

parser.add_argument(
    "--name",              # 1 или множество значений
    type=str,
    help="Имя отчёта (необязательно)."
)

parser.add_argument("--report", required=True, choices=list(REPORTS.keys())) # Добавляем аргумент и добавляем словарь с выборами в choices
args = parser.parse_args()
paths = args.files  # список строковых путей
name = args.name
func = REPORTS[args.report] # Приравнием к функции из отчётов
sorted_rating, name = REPORTS[args.report](paths, name)
table = tabulate(sorted_rating, headers=['brand', 'rating'], tablefmt="github", floatfmt='.2f')
print(table)
if name:
    print(f'Название отчёта: {name}')
