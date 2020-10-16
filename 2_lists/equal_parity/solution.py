#Реализуйте функцию same_parity_filter, которая принимает на вход список и возвращает новый список, состоящий из элементов, у которых такая же чётность, как и у первого элемента исходного списка.

#Примеры
#>>> same_parity_filter([])
#[]
#>>> same_parity_filter([2, 0, 1, -3, 10, -2])
#[2, 0, 10, -2]
#>>> same_parity_filter([-1, 0, 1, -3, 10, -2])
#[-1, 1, -3]

#def is_even(number):
#    return number % 2 == 0

#def same_parity_filter(numbers):
#    if not numbers:
#        return []
#    first_number_parity = is_even(numbers[0])
#    filtered_numbers = filter(
#        lambda number: is_even(number) == first_number_parity,
#        numbers,)
#    return list(filtered_numbers)

def same_parity_filter(list_example):
    filtered_list = []
    for item in list_example:
        if item % 2 is list_example[0] % 2:
            filtered_list.append(item)
    return filtered_list

#def even_or_odd(a):
#    if a % 2 == 0:
#        return True

#def same_parity_filter(lists):
#    a = []
#    for value in lists:
#        if even_or_odd(value) == even_or_odd(lists[0]):
#            a.append(value)
#    return a
