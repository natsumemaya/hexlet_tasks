from solution import rpn_calc


def test_rpn_calc():
    assert rpn_calc([1, 2, '+', 4, '*', 3, '+']) == 15
    assert rpn_calc([7, 2, 3, '*', '-']) == 1
    assert rpn_calc([1, 2, '+', 2, '*']) == 6
    print('test_rpn_calc is Ok!')

test_rpn_calc()