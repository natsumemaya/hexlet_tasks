from solution import triangle

def test_triangle():
    rows = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    results = []
    for i in range(len(rows)):
        results.append(triangle(i))
    for i in range(len(rows)):
        if rows[i] == results[i]:
            next
        else:
            raise Exception(f'test_triangle is Failed! For {repr(rows[i])} has answer > {results[i]}')
    print('test_triangle is Ok!')

test_triangle()
