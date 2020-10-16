from solution import is_power_of_three


def test_is_power_of_three_positive():
    print('is_power_of_three positive:')
    print(1, is_power_of_three(1))
    print(9, is_power_of_three(9))
    print(81, is_power_of_three(81))


def test_is_power_of_three_negative():
    print('is_power_of_three negative:')
    print(0, not is_power_of_three(0))
    print(2, not is_power_of_three(2))
    print(10, not is_power_of_three(10))
    print(18, not is_power_of_three(18), "Делится на 3, но не степень тройки!")

test_is_power_of_three_positive()
test_is_power_of_three_negative()