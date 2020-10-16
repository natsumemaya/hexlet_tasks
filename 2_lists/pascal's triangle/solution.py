#Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел. Строки треугольника симметричны относительно вертикальной оси.

#0:      1
#1:     1 1
#2:    1 2 1
#3:   1 3 3 1
#4:  1 4 6 4 1

#Напишите функцию triangle, которая возвращает указанную строку треугольника паскаля в виде массива.
#Пример:
#>>> triangle(0)
#[1]
#>>> triangle(4)
#[1, 4, 6, 4, 1]

from operator import add

def triangle(row_number):
    row = [1]
    for _ in range(row_number):
        row = list(map(  # [x,y,z]
            add,         # x y z 0
            row + [0],   # + + + +
            [0] + row,   # 0 x y z
        ))
    return row

#from operator import add
#def triangle(num):
#    res = [[1], [1, 1]]
#    if num < 2:
#        return res[num]
#    for i in range(2, num + 1):
#        s = [1] + list(map(add, res[i - 1], res[i - 1][1:])) + [1]
#        res.append(s)
#    return res[num]

#def triangle(coeff):
#    if coeff == 0:
#        return [1]
#    elif coeff == 1:
#        return [1, 1]
#    prev = triangle(coeff - 1)
#    result = [1] * (coeff + 1)
#    for index in range(1, len(result) - 1):
#        result[index] = prev[index - 1] + prev[index]
#    return result

#def triangle(row):
#    coefficients = [1]
#    n = row
#    k = 1
#    for _ in range(row):
#        coefficients.append(coefficients[-1] * n // k)
#        n -= 1
#        k += 1
#    return coefficients