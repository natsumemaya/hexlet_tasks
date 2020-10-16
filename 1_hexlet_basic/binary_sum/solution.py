#Реализуйте функцию binary_sum, которая принимает на вход два двоичных числа (в виде строк) и возвращает их сумму. Результат (вычисленная сумма) также должен быть бинарным числом в виде строки.
#Посмотрите примеры работы функции:
#binary_sum('10', '1')      # 11
#binary_sum('1101', '101')  # 10010
#Подсказки
#bin
#int

#def binary_sum(number_a, number_b):
#    binary_a = int(number_a, base=2)
#    binary_b = int(number_b, base=2)
#    return bin(binary_a + binary_b).replace('0b', '')

def binary_sum(first_number, second_number):
    (a, b) = (int(first_number, 2), int(second_number, 2))
    s = a + b
    return format(s, 'b')