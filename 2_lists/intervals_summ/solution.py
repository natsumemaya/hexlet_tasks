# Реализуйте функцию sum_of_intervals, которая принимает на вход список интервалов и возвращает сумму всех длин интервалов. В данной задаче используются только интервалы целых чисел от 1 до ∞ , которые представлены в виде списков. Первое значение интервала всегда будет меньше, чем второе значение. Например, длина интервала [1, 5] равна 4, а длина интервала [5, 5] равна 0. Пересекающиеся интервалы должны учитываться только один раз.

# Примеры
# >>> from solution import sum_of_intervals
# >>> sum_of_intervals([
# ... [1, 1],
# ... ])
# 0
# >>> sum_of_intervals([
# ... [1, 2],
# ... [50, 100],
# ... [60, 70],
# ... ])
# 51
# >>> sum_of_intervals([
# ... [1, 2],
# ... [5, 10],
# ... ])
# 6
# >>>

def sum_of_intervals(intervals):
    values = []
    for start, end in intervals:
        for i in range(start, end):
            if i not in values:
                values.append(i)
    return len(values)

# def sum_of_intervals(intervals):
#     b = []
#     for elem in intervals:
#         interval = [x for x in range(elem[0], elem[-1])]
#         for step in interval:
#             b.append(step)
#     return len(set(b))