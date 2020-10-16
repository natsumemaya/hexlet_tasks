#Реализуйте функцию is_power_of_three, которая определяет, является ли переданное число натуральной степенью тройки. Например, число 27 — это третья степень: 3 ** 3, а 81 — это четвёртая: 3 ** 4.

#Пример:

#>>> is_power_of_three(1)
#True
#>>> is_power_of_three(2)
#False
#>>> is_power_of_three(9)
#True

def is_power_of_three(number):
    counter = 1  # 3 ** 0
    while counter < number:
        counter *= 3
    return counter == number

#def is_power_of_three(x):
#    if x == 0:
#        return False
#    while x > 1:
#        if x % 3 != 0:
#            return False
#        x //= 3
#    return True