# Реализуйте функцию find_index_of_nearest, которая принимает на вход список чисел и искомое число. Задача функции — найти в списке ближайшее число к искомому и вернуть его индекс.

# Если в списке содержится несколько чисел, одновременно являющихся ближайшими к искомому числу, то возвращается наименьший из индексов ближайших чисел.

# Примеры
# >>> find_index_of_nearest(2, []) is None
# True
# >>> find_index_of_nearest(0, [15, 10, 3, 4])
# 2
# >>> find_index_of_nearest(4, [7, 5, 3, 2])
# 1
# >>> find_index_of_nearest(4, [7, 5, 4, 4, 3])
# 2
def find_index_of_nearest(number, source):
    if source:
        diff = list(map(lambda x: abs(x - number), source))
        return diff.index(min(diff))

# def find_index_of_nearest(n, list_):
#     if list_:
#         min_ = []
#         for i in list_:
#             min_.append(abs(n - i))
#         return min_.index(min(min_))
#     return None


#_____________________
# from operator import sub
# from itertools import repeat

# def find_index_of_nearest(search, neighbours):
#     if neighbours:
#         n = list(map(abs, map(sub, neighbours, repeat(search))))
#         return n.index(min(n))



# МОЕ:

# def find_index_of_nearest(number, source):
#     if source:
#         diff = list(map(lambda x: abs(x - number), source))
#         return diff.index(min(diff))

# def find_index_of_nearest(x,sourse):
#   if not sourse: # на случай когда словарь пуст
#     return None
# # если значение есть в списке функция просто вернет его индекс return...
# # если заданного значения нет в списке
#   if x not in sourse:
#     # создадим новый словарь ключи(данный списк), а в значения к ним записываем разницу между ним и искомым значением
#     diff_source = {}
#     for item in sourse:   
#       diff = abs(item - x)
#       diff_source[item] = diff  
#     #print(diff_source)
#     # отсортируем значения в новом списке, чтобы узнать наименьшее
#     a = list(diff_source.values())
#     a.sort()
#     smallest = a[0]
#     #print(smallest, 'smallest')
#     # достаем ключ по совпадению с наименьшим значением из своего словаря и вернуть ответ по индексу уже из данного нам источника 
#     for k, v in diff_source.items():
#       if v == smallest:
#         return sourse.index(k)
      
#   return sourse.index(x)
