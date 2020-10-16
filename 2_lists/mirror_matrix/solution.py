#Реализуйте функцию mirror_matrix, которая принимает двумерный список (матрицу) и изменяет его (по месту) таким образом, что правая половина матрицы становится зеркальной копией левой половины, симметричной относительно вертикальной оси матрицы. Если ширина матрицы — нечётная, то "средний" столбец не должен быть затронут.

#Пример
#>>> from solution import mirror_matrix
#>>> l = [
#...     [1, 2, 3],
#...     [4, 5, 6],
#... ]
#...
#>>> mirror_matrix(l)
#>>> l == [
#...     [1, 2, 1],
#...     [4, 5, 4],
#... ]
#...
#True
#>>> l = [
#...     [11, 12, 13, 14, 15, 16],
#...     [21, 22, 23, 24, 25, 26],
#...     [31, 32, 33, 34, 35, 36],
#...     [41, 42, 43, 44, 45, 46],
#...     [51, 52, 53, 54, 55, 56],
#...     [61, 62, 63, 64, 65, 66],
#... ]
#...
#>>> mirror_matrix(l)
#>>> l == [
#...     [11, 12, 13, 13, 12, 11],
#...     [21, 22, 23, 23, 22, 21],
#...     [31, 32, 33, 33, 32, 31],
#...     [41, 42, 43, 43, 42, 41],
#...     [51, 52, 53, 53, 52, 51],
#...     [61, 62, 63, 63, 62, 61],
#... ]
#...
#True
#>>>

def mirror_matrix(matrix):
    if matrix:
        half_len = len(matrix[0]) // 2
        for line in matrix:
            line[half_len:] = line[-half_len - 1::-1]

#def mirror_matrix(matrix):
#    if len(matrix) > 1:
#        for v in matrix:
#            chunk = len(v) // 2
#            odd = chunk + 1 if len(v) % 2 == 1 else chunk
#            v[odd:] = reversed(v[0:chunk])

#def mirrow_list(row):
#    for i in range(len(row) // 2):
#        row[-1 - i] = row[i]
#    return row
#def mirror_matrix(matrix):
#    for idx, row in enumerate(matrix):
#        matrix[idx] = mirrow_list(row)