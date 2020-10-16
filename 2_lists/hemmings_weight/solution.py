#Вес Хэмминга это количество единиц в двоичном представлении числа.
#Реализуйте функцию hamming_weight, которая считает вес Хэмминга.
#Примеры
#>>> hamming_weight(0)
#0
#>>> hamming_weight(4)
#1
#>>> hamming_weight(101)
#4

def hamming_weight(number):
    weight = 0
    digits = bin(number)[2:]
    for num in digits:
        weight += int(num)
    return weight


# Alternative solutions
# def hamming_weight(x):
#     s = 0
#     while x:
#         x, r = divmod(x, 2)
#         s += r
#     return s

# def hamming_weight(number):
#     return bin(number).count('1')