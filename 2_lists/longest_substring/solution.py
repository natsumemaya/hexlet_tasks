# Реализуйте функцию find_longest_length, принимающую на вход строку и возвращающую длину максимальной последовательности из неповторяющихся символов. Подстрока может состоять из одного символа. Например в строке qweqrty, можно выделить следующие подстроки: qwe, weqrty. Самой длинной будет weqrty, а её длина — 6 символов.

# >>> find_longest_length('abcdeef')
# 5
# >>> find_longest_length('jabjcdel')
# 7

# def unique_sequence_length(string):
#     unique_sequence = set()
#     length = 0
#     for char in string:
#         if char in unique_sequence:
#             break
#         unique_sequence.add(char)
#         length += 1
#     return length


# def find_longest_length(string):
#     longest_length = 0
#     for i, _ in enumerate(string):
#         substring_length = unique_sequence_length(string[i:])
#         if longest_length < substring_length:
#             longest_length = substring_length
#     return longest_length

def find_longest_length(input_string):
    mass = list(input_string)
    sub_mass = []
    result = 0
    for i in range(len(mass)):
        for j in range(i, len(mass)):
            if mass[j] in sub_mass:
                break
            else:
                sub_mass.append(mass[j])
        if len(sub_mass) > result:
            result = len(sub_mass)
        sub_mass.clear()
    return result

# def find_longest_length(seq):
#     res, tmp = [], []

#     for i, _ in enumerate(seq):
#         for j in seq[i:]:
#             if j in tmp:
#                 if len(tmp) > len(res):
#                     res = tmp[:]
#                 tmp.clear()
#                 break
#             else:
#                 tmp.append(j)
#     if len(tmp) > len(res):
#         res = tmp[:]
#     return len(res)

#не работает :с
# def find_longest_length(sequence):
#     A = list(sequence) 
#     for counter in range(len(A)): 
#         result = []
#         start = 0
#         letter = A[counter] 
#         if letter not in result:
#             result.append(letter)
#         else: 
#             result.clear
#             new_start = counter
#             new_A = A[new_start:]
#             find_longest_length(new_A)
#         return len(result)

# find_longest_length('jabjcdel')