# Матрицу можно представить в виде двумерного списка. Например, список [[1, 2, 3, 4], [5, 6, 7, 8]] — это отображение матрицы:

# 1 2 3 4
# 5 6 7 8
# src/solution.py
# Реализуйте функцию snail_path(), которая принимает на вход матрицу и возвращает список элементов матрицы по порядку следования от левого верхнего элемента по часовой стрелке к внутреннему. Движение по матрице напоминает улитку:

# Примеры:
# >>> from solution import snail_path
# >>> snail_path([[1, 2], [3, 4]])
# [1, 2, 4, 3]
# >>> snail_path([[1, 2, 3], [8, 9, 4], [7, 6, 5]])
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# >>> snail_path([['b', 'c', 'a'], ['3', True, 11], [None, 'foo', 0]])
# ['b', 'c', 'a', 11, 0, 'foo', None, '3', True]
# >>>

def rotate(matrix):
    """
    Rotate the matrix counter-clockwise.

    >>> rotate([[1]])
    [(1,)]
    >>> rotate([[1, 2, 3]])
    [(3,), (2,), (1,)]
    >>> rotate([[1, 2], [3, 4]])
    [(2, 4), (1, 3)]
    """
    return list(reversed(list(zip(*matrix))))


def snail_path(matrix):
    path = []

    def trace(submatrix):
        if not submatrix:
            return
        path.extend(submatrix[0])
        trace(rotate(submatrix[1:]))
    trace(matrix)
    return path

# def snail_path(seq):
#     if not seq:
#         return seq

#     result = []
#     while seq:
#         result.extend(seq.pop(0))
#         if not seq:
#             break
#         seq = list(map(list, zip(*seq)))[::-1]
#     return result

# def snail_path(matrix):
#     result = []
#     while matrix:
#         result.extend(matrix.pop(0))
#         matrix = list(zip(*matrix))[::-1]
#     return result