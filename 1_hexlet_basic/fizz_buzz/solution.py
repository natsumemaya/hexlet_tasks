#Реализуйте функцию fizz_buzz, которая возвращает строку с числами (через пробел) в диапазоне от begin до end включительно. При этом:

#Если число делится без остатка на 3, то вместо него выводится слово Fizz
#Если число делится без остатка на 5, то вместо него выводится слово Buzz
#Если число делится без остатка и на 3, и на 5, то вместо числа выводится слово FizzBuzz
#В остальных случаях в строку добавляется само число
#Функция принимает два параметра (begin и end), определяющих начало и конец диапазона (включительно). Если диапазон пуст (в случае, когда begin > end), то функция возвращает пустую строку.

def fizz_buzz(start, stop):
    result = ''
    while start <= stop:
        if result:
            result += ' '
        if start % 15 == 0:
            result += 'FizzBuzz'
        elif start % 3 == 0:
            result += 'Fizz'
        elif start % 5 == 0:
            result += 'Buzz'
        else:
            result += str(start)
        start += 1
    return result