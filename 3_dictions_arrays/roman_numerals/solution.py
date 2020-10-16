# Для записи цифр римляне использовали буквы латинского алфафита: I, V, X, L, C, D, M. Например:
# * 1 обозначалась с помощью буквы I
# * 10 с помощью Х
# * 7 с помощью VII
# Число 2020 в римской записи — это MMXX (2000 = MM, 20 = XX).
# 'src/solution.py'
# Реализуйте функцию to_roman(), которая переводит арабские числа в римские. Функция принимает на вход целое число из диапазона от 1 до 3000, а возвращает строку с римским представлением этого числа.
# Реализуйте функцию to_arabic(), которая переводит число в римской записи в число, записанное арабскими цифрами. Если переданное римское число не корректно, то функция должна вернуть значение False.
# Примеры
# to_roman(1)
# >>> 'I'
# to_roman(59)
# >>> 'LIX'
# to_roman(3000)
# >>> 'MMM'
# to_arabic('I')
# >>> 1
# to_arabic('LIX')
# >>> 59
# to_arabic('MMM')
# >>> 3000
# to_arabic('IIII')
# >>> False
# to_arabic('VX')
# >>> False
# Подсказки
# * Подробнее о римской записи — https://ru.wikipedia.org/wiki/Римские_цифры


NUMERALS = {  # noqa: WPS407
    'M': 1000,
    'CM': 900,
    'D': 500,
    'CD': 400,
    'C': 100,
    'XC': 90,
    'L': 50,
    'XL': 40,
    'X': 10,
    'IX': 9,
    'V': 5,
    'IV': 4,
    'I': 1,
}

def descending(pair):
    return -pair[1]

def to_roman(number):
    result = ''
    for roman, arabic in sorted(NUMERALS.items(), key=descending):
        repetitions_count = number // arabic
        number -= arabic * repetitions_count
        result += roman * repetitions_count
    return result

def to_arabic(number):  # noqa: WPS210
    numbers = []
    for char in number:
        numbers.append(NUMERALS[char])
    # Сдвиг чисел с повтором последнего
    # Пример: [1,2,3,4] -> [2,3,4,4]
    shifted_numbers = numbers[1:] + numbers[-1:]
    result = 0
    for previous, current in zip(numbers, shifted_numbers):
        if previous >= current:
            result += previous
        else:
            result -= previous
    if to_roman(result) != number:
        return False
    return result


# NUMERALS = {  # noqa: WPS407
#     'M': 1000,
#     'D': 500,
#     'C': 100,
#     'L': 50,
#     'X': 10,
#     'V': 5,
#     'I': 1,
# }

# NUMERALS_WITH_SUBSTRACT = {
#         'CM': 900,
#         'CD': 400,
#         'XC': 90,
#         'XL': 40,
#         'IX': 9,
#         'IV': 4,
# }

# NUMERALS_ARABIC = {  # noqa: WPS407
#     1000: 'M',
#     900: 'CM',
#     500: 'D',
#     400: 'CD',
#     100: 'C',
#     90: 'XC',
#     50: 'L',
#     40: 'XL',
#     10: 'X',
#     9: 'IX',
#     5: 'V',
#     4: 'IV',
#     1: 'I',
# }


# def to_arabic(roman):
#     if roman == '':
#         return 0
#     roman_for_check = roman
#     arabic = 0
#     while roman:
#         if len(roman) >= 2 and roman[:2] in NUMERALS_WITH_SUBSTRACT:
#             arabic += NUMERALS_WITH_SUBSTRACT[roman[:2]]
#             roman = roman[2:]
#         elif roman[0] in NUMERALS:
#             arabic += NUMERALS[roman[0]]
#             roman = roman[1:]
#         else:
#             return None
#     if to_roman(arabic) == roman_for_check:
#         return arabic
#     else:
#         return False


# def to_roman(arabic):
#     roman = ''
#     while arabic:
#         digit, arabic = next_roman_digit(arabic)
#         roman = roman + digit
#     return roman

# def next_roman_digit(arabic):
#     for number in sorted(NUMERALS_ARABIC, reverse=True):
#         if arabic >= number:
#             arabic -= number
#             digit = NUMERALS_ARABIC[number]
#             return digit, arabic