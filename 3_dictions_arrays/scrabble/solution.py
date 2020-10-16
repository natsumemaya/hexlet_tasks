# Реализуйте функцию-предикат scrabble, которая принимает на вход два параметра: набор символов (строку) и слово, и проверяет, можно ли из переданного набора составить это слово. В результате вызова функция возвращает True или False.

# При проверке учитывается количество символов, которые нужны для составления слова, и не учитывается их регистр.

# Для решения используйте встроенный инструмент — Counter.

# Пример
# >>> scrabble('rkqodlw', 'world')
# True
# >>> scrabble('avj', 'java')
# False
# >>> scrabble('avjafff', 'java')
# True
# >>> scrabble('', 'hexlet')
# False
# >>> scrabble('scriptingjava', 'JavaScript')
# True

from collections import Counter

def scrabble(string, word):
    letters = Counter(string.lower())
    for letter, count in Counter(word.lower()).items():
        if letters[letter] < count:
            return False
    return True

# def scrabble(string, word):
#     string_chars_counts = Counter(string.lower())
#     word_chars_counts = Counter(word.lower())
#     string_chars_counts.subtract(word_chars_counts)
#     return all(count >= 0 for count in string_chars_counts.values())

# from collections import Counter

# def scrabble(string, word):
#     counter_string = Counter(string.lower())
#     counter_word = Counter(word.lower())
#     diff = counter_word - counter_string
#     if len(diff) == 0:
#         return True
#     return False