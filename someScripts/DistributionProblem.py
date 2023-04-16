"""
РЕШЕНИЕ ТРАНСПОРТНОЙ ЗАДАЧИ. ВАРИАНТ 16
=======================================

Автор: Подстречный Александр Владимирович, группа 2Э2
Проверил: Бутузова Лариса Леонидовна
"""

# Импорт функций и объектов из библиотеки PuLP
from pulp import *

# Инициализация констант с английскими буквами
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

def show(matrix: list, replace_none_to: str = "_"):
    """
    Функция для вывода матрицы в консоль
    """
    for row in matrix:
        print('\t'.join([str(elem).replace("None", replace_none_to) for elem in row]))


# Задаем первоначальные значения в виде списков
matrix = [
    [1, 2, 3, 1],
    [2, 3, 4, 6],
    [3, 4, 7, 12]
]
stocks = [100, 200, 300]
needs = [100, 100, 300, 300]


# Закрываем задачу, если необходимо
diff_for_close = sum(stocks) - sum(needs)
if diff_for_close < 0:
    print(f"Задача закрыта. Добавлен фиктивный поставщик со значением {abs(diff_for_close)} - строка:")
    matrix.append([0] * len(matrix[0]))
    stocks.append(abs(diff_for_close))
elif diff_for_close > 0:
    print(f"Задача закрыта. Добавлен фиктивный потребитель со значением {abs(diff_for_close)} - столбец:")
    needs.append(abs(diff_for_close))
    for i, row in enumerate(matrix):
        matrix[i].append(0)
else:
    print("Стоимости доставок:")
show(matrix)
print("Запасы:")
print(*stocks, sep="\n")
print("Потребности:")
print(*needs)


# Создает список всех узлов снабжения
Warehouses = [ascii_uppercase[i] for i in range(len(matrix))]

# Создает словарь для количества единиц поставки для каждого узла поставки
supply = {Warehouses[i]: stocks[i] for i in range(len(matrix))}

# Создает список всех узлов спроса
Customers = [str(i) for i in range(len(matrix[0]))]

# Создает словарь для количества единиц спроса для каждого узла спроса
demand = {Customers[i]: needs[i] for i in range(len(matrix[0]))}

# Создает список затрат для каждого транспортного пути
costs = [*matrix]

# Данные о стоимости формируются в словарь
costs = makeDict([Warehouses, Customers], costs, 0)

# Создает переменную 'prob' для содержания данных о проблеме
prob = LpProblem("Distribution Problem", LpMinimize)

# Создает список кортежей, содержащий все возможные маршруты для транспорта
Routes = [(w, b) for w in Warehouses for b in Customers]

# Создается словарь под названием 'Vars', содержащий переменные, на которые ссылаются (маршруты)
vars = LpVariable.dicts("Route", (Warehouses, Customers), 0, None, LpInteger)

# Объективная функция сначала добавляется к 'prob'
prob += (
    lpSum([vars[w][b] * costs[w][b] for (w, b) in Routes]),
    "Sum_of_Transporting_Costs",
)

# Максимальные ограничения на поставки добавляются к prob для каждого узла поставки (склада)
for w in Warehouses:
    prob += (
        lpSum([vars[w][b] for b in Customers]) <= supply[w],
        f"Sum_of_Products_out_of_Warehouse_{w}",
    )

# Минимальные ограничения спроса добавляются к prob для каждого узла спроса (бар)
for b in Customers:
    prob += (
        lpSum([vars[w][b] for w in Warehouses]) >= demand[b],
        f"Sum_of_Products_into_Customer{b}",
    )

# Данные о проблеме записываются в файл .lp
prob.writeLP("DistributionProblem.lp")

# Задача решается с помощью выбранного в PuLP решателя
prob.solve()

# Статус решения выводится на экран
print("Status:", LpStatus[prob.status])

# Каждая из переменных выводится с разрешенным оптимальным значением
_index = 0
for v in prob.variables():
    if _index >= len(matrix[0]):
        print(end="\n")
        _index = 0
    print(int(v.varValue), end="\t")
    _index += 1

# Оптимизированное значение объективной функции выводится на экран
print("\n\nTotal Cost of Transportation = ", value(prob.objective))

"""
Result - Optimal solution found

Objective value:                2300.00000000
Enumerated nodes:               0
Total iterations:               0
Time (CPU seconds):             0.01
Time (Wallclock seconds):       0.01

Option for printingOptions changed from normal to all
Total time (CPU seconds):       0.02   (Wallclock seconds):       0.02

Status: Optimal
0       0       0       100
0       0       200     0
100     100     100     0
0       0       0       200

Total Cost of Transportation =  2300.0
"""