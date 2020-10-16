# Анаграммы — это слова, которые состоят из одинаковых букв. Например:

# спаниель — апельсин
# карат — карта — катар
# топор — ропот — отпор
# src/solution.py
# Реализуйте функцию filter_anagrams, которая находит все слова-анаграммы. Функция принимает исходное слово и последовательность (iterable) слов для проверки, а возвращает последовательность анаграмм.

# Я использовал в абзаце "слова" только для краткости. Строго говоря, ваша функция должна уметь находить анаграммы любых последовательностей, в том числе списков и кортежей. То есть решение должно быть максимально общим.

# Примеры
# >>> list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
# ['aabb', 'bbaa']
# >>> list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
# ['carer', 'racer']
# >>> list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer']))
# []
# >>> list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]]))
# [[2, 1], [1, 2]]

def normalized(string):
    return list(sorted(string))


def filter_anagrams(word, words):
    norm = normalized(word)
    return filter(lambda item: normalized(item) == norm, words)

# def filter_anagrams(iterable_source, collection):
#     def iterables_equal(iterable_checking):
#         first = list(iterable_source)
#         second = list(iterable_checking)
#         first.sort()
#         second.sort()
#         return first == second

#     return list(filter(iterables_equal, collection))

# def filter_anagrams(key, items):
#     result = items.copy()                   
#     for word in items:                     
#         word_list = []
#         word_list.extend(word)
#         if len(word) == len(key):
#             for letter in key:                  
#                 if letter in word_list:             
#                     word_list.remove(letter)
#                 else:
#                     result.remove(word)
#                     break
#         else: 
#             result.remove(word)
#     return result