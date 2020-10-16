from solution import chunked


def test_chunked_list():
    a = chunked(2, ['a', 'b', 'c', 'd']) == [['a', 'b'], ['c', 'd']]
    b = chunked(3, ['e', 'f', 'h', 'i']) == [['e', 'f', 'h'], ['i']]
    c = chunked(4, ['g', 'k', 'l', 'm']) == [['g', 'k', 'l', 'm']]
    d = chunked(4, []) == []
    e = chunked(2, ['n']) == [['n']]
    tests = [ a, b, c , d, e]
    for test in tests:
        if test:
            next
        else:
            raise Exception('test_chunked_list is Failed!')
    print('test_chunked_list is Ok!')


def test_chunked_tuple():
    a = chunked(2, ('A', 'B', 'C', 'D')) == [('A', 'B'), ('C', 'D')]
    b = chunked(3, ('E', 'F', 'H', 'I')) == [('E', 'F', 'H'), ('I',)]
    c = chunked(4, ('G', 'K', 'L', 'M')) == [('G', 'K', 'L', 'M')]
    d = chunked(4, []) == []
    e = chunked(2, ('N',)) == [('N',)]
    tests = [ a, b, c , d, e]
    for test in tests:
        if test:
            next
        else:
            raise Exception('test_chunked_tuple is Failed!')
    print('test_chunked_tuple is Ok!')


def test_chunked_str():
    a = chunked(2, 'abcd') == ['ab', 'cd']
    b = chunked(3, 'efhi') == ['efh', 'i']
    c = chunked(4, 'gklm') == ['gklm']
    d = chunked(4, '') == []
    e = chunked(2, 'x') == ['x']
    tests = [ a, b, c , d, e]
    for test in tests:
        if test:
            next
        else:
            raise Exception('test_chunked_str is Failed!')
    print('test_chunked_str is Ok!')

test_chunked_list()
test_chunked_tuple()
test_chunked_str()