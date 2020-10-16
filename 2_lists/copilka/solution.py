# Реализуйте функцию visualize, которая подсчитывает сколько монет каждого номинала есть в копилке и показывает результат в виде графика. Каждый столбец графика — стопка монет опредлённого номинала.

# Для простоты условимся, что монеты в копилке всегда есть, и их количество не ограничено, а номинал может быть любым.

# Функция принимает на вход список или кортеж с числами и возвращает график в виде строки. Необязательный аргумент bar_char определяет символ, с помощью которого рисуется график. Значение по умолчанию — знак рубля (₽).

# Для решения используйте встроенный инструмент — Counter.

# Примеры
# from solution import visualize
# >>> print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3)))
# 5             
# ₽₽ 4  4       
# ₽₽ ₽₽ ₽₽    3 
# ₽₽ ₽₽ ₽₽    ₽₽
# ₽₽ ₽₽ ₽₽ 1  ₽₽
# ₽₽ ₽₽ ₽₽ ₽₽ ₽₽
# --------------
# 1  2  3  10 20
# >>>
# >>> print(visualize((10,1,1,1,1,1,20,20,20,2,2,2,2,3,3,3,3), bar_char='$'))
# 5             
# $$ 4  4       
# $$ $$ $$    3 
# $$ $$ $$    $$
# $$ $$ $$ 1  $$
# $$ $$ $$ $$ $$
# --------------
# 1  2  3  10 20

from collections import Counter


def visualize(coins, bar_char='₽'):  # noqa: WPS210
    """Visualize money in a money box."""
    # BEGIN
    counts = Counter(coins)
    nominals = sorted(counts.keys())
    highest_stack = max(counts.values())

    rows = []
    delimiter = ''

    for level in range(highest_stack, -1, -1):
        row = ''
        for _, bar in sorted(counts.items()):
            if bar > level:
                row += '{} '.format(bar_char * 2)
            elif bar == level and bar != 0:
                row += '{:<2d} '.format(bar)
                delimiter += '---'
            else:
                row += '   '
        rows.append(row[:-1])

    rows.append(delimiter[:-1])
    row = ''
    for nominal in nominals:
        row += '{:<2d} '.format(nominal)
    rows.append(row[:-1])

    return '\n'.join(rows)

# from collections import Counter

# def visualize(coins, bar_char='₽'):  # noqa: WPS210
#     """Visualize money in a money box."""
#     # BEGIN (write your solution here)
#     res = []
#     count_coins = Counter(coins)
#     keys = sorted(count_coins.keys())
#     max_count = max(count_coins.values())

#     footer = ' '.join(list(map(lambda x: str(x).ljust(2), keys)))
#     line = '-' * (len(keys) * 2 + len(keys) - 1)
#     res.append(footer)
#     res.append(line)

#     matrix = []
#     for key in keys:
#         elem = count_coins.get(key)
#         t = [bar_char * 2 for _ in range(elem)]
#         t.extend([str(elem).ljust(2)])
#         t.extend(['  ' for _ in range(max_count - elem)])
#         matrix.append(t)

#     for i in list(map(list, zip(*matrix))):
#         res.append(' '.join(i))

#     return '\n'.join(res[::-1])


