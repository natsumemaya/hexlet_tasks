from solution import enlarge


def test_enlarge():
    assert enlarge([]) == []
    assert enlarge(['']) == ['', '']
    assert enlarge(['A',]) == ['AA', 'AA',]
    assert enlarge([' *','# ',]) == ['  **', '  **', '##  ', '##  ',]
    print('test_enlarge is Ok!')

test_enlarge()