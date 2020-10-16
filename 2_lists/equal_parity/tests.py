from solution import same_parity_filter

a = same_parity_filter([5, 0, 1, -3, 10]) == [5, 1, -3]
b = same_parity_filter([2, 0, 1, -3, 10, -2]) == [2, 0, 10, -2]
c = same_parity_filter([-1, 0, 1, -3, 10, -2]) == [-1, 1, -3]
d = same_parity_filter([10, -1.5, 1.3, -3, 25, -2]) == [10, -2]
e = same_parity_filter([]) == []

tests = [ a, b, c , d, e]

def test_same_parity_filter():
    for test in tests:
        if test:
            next
        else:
            raise Exception('test_same_parity_filter Failed!')
    print('test_same_parity_filter is Ok!')

test_same_parity_filter()
    