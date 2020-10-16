from solution import multiply


def test_multiply():
    assert multiply(
        [[2]],
        [[3]],
    ) == [[6]]

    a = [
        [1],
        [2],
    ]
    b = [
        [10, 20],
    ]
    assert multiply(a, b) == [
        [10, 20],
        [20, 40],
    ]

    a = [
        [1, 2, 1],
        [0, 1, 0],
        [2, 3, 4],
    ]
    b = [
        [2, 5],
        [6, 7],
        [1, 8],
    ]
    assert multiply(a, b) == [
        [15, 27],
        [6, 7],
        [26, 63],
    ]
    print('test_multiply is Ok!')

test_multiply()
