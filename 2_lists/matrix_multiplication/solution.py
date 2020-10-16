# Операция умножения двух матриц А и В представляет собой вычисление результирующей матрицы С, где каждый элемент C(ij) равен сумме произведений элементов в соответствующей строке первой матрицы A(ik) и элементов в столбце второй матрицы B(kj).

# Две матрицы можно перемножать только в том случае, если количество столбцов в первой матрице совпадает с количеством строк во второй матрице. Это значит, что первая матрица обязательно должна быть согласованной со второй матрицей. В результате операции умножения матрицы размера M×N на матрицу размером N×K является матрица размером M×K.

# src/solution.py
# Реализуйте функцию multiply, которая принимает две матрицы и возвращает новую матрицу — результат их произведения.

# Примеры
# >>> from solution import multiply
# >>> A = [[1, 2], [3, 2]]
# >>> B = [[3, 2], [1, 1]]
# >>> multiply(A, B)
# [[5, 4], [11, 8]]
# >>>
# >>> C = [
# ...   [2, 5],
# ...   [6, 7],
# ...   [1, 8],
# ... ]
# >>> D = [
# ...   [1, 2, 1],
# ...   [0, 1, 0],
# ... ]
# >>> multiply(C, D)
# [[2, 9, 2], [6, 19, 6], [1, 10, 1]]
# >>>
# Подсказки
# Описание алгоритма перемножения матриц.
# Демонстрация операции перемножения матриц.

def zero_matrix(rows, columns):
    matrix = []
    row = [0] * columns
    for _ in range(rows):
        matrix.append(row[:])
    return matrix


def multiply(a, b):  # noqa: WPS210
    rows_in_a = len(a)
    columns_in_b = len(b[0])
    c = zero_matrix(rows_in_a, columns_in_b)
    for row_a, row_c in zip(a, c):
        for x in range(columns_in_b):
            for y, row_b in enumerate(b):
                row_c[x] += row_a[y] * row_b[x]
    return c

# def multiply(m1,m2):
#     s=0     #сумма
#     t=[]    #временная матрица
#     m3=[] # конечная матрица
            
#     r1=len(m1) #количество строк в первой матрице
#     c1=len(m1[0]) #Количество столбцов в 1   
#     r2=c1           #и строк во 2ой матрице
#     c2=len(m2[0])  # количество столбцов во 2ой матрице
#     for z in range(0,r1):
#         for j in range(0,c2):
#             for i in range(0,c1):
#                   s=s+m1[z][i]*m2[i][j]
#             t.append(s)
#             s=0
#         m3.append(t)
#         t=[]           
#     return m3

# from operator import mul

# def multiply(x, y):
#     result = []
#     for i, vx in enumerate(x):
#         result.append([])
#         for vy in map(list, zip(*y)):
#             result[i].append(sum(map(mul, vx, vy)))
#     return result