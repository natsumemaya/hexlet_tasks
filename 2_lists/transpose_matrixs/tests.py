from solution import transposed

SAMPLES = (
    # single cell
    ([[42]], [[42]]),

    # column
    ([
        [1],
        [2],
        [3],
    ], [
        [1, 2, 3],
    ]),

    # row
    ([
        [4, 5, 6],
    ], [
        [4],
        [5],
        [6],
    ]),

    # square matrix
    ([
        [10, 20],
        [30, 40],
    ], [
        [10, 30],
        [20, 40],
    ]),

    # rectangle matrix
    ([
        ['d', 'o'],
        ['r', 'e'],
        ['m', 'i'],
    ], [
        ['d', 'r', 'm'],
        ['o', 'e', 'i'],
    ]),
)


def test_transposed():
    for matrix, result in SAMPLES:
        assert transposed(matrix) == result
    print('test_transposed ok!')


def test_transposed_reversibility():
    for matrix, _ in SAMPLES:
        assert transposed(transposed(matrix)) == matrix
    print('test_transposed_reversibility ok!')

test_transposed()
test_transposed_reversibility()