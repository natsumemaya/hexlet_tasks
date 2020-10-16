#Реализуйте функцию length_of_last_word, которая возвращает длину последнего слова переданной на вход строки. Словом считается любая последовательность не содержащая пробелы, символы перевода строки \n и табуляции \t.

#Примеры
#>>>length_of_last_word('')
#0
#>>>length_of_last_word('man in Black')
#5
#>>>length_of_last_word('hello, world!     ')
#6
#>>>length_of_last_word('hello\t\nworld')
#5

def length_of_last_word(string):
    words = string.split()
    if not words:
        return 0
    last_word = words[-1]
    return len(last_word)