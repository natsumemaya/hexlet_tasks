from solution import scrabble


def test_scrabble():
    assert scrabble('begsdhhtsexoult', 'hexlet') is True
    assert scrabble('rkqodlw', 'world') is True
    assert scrabble('begsdhhtsexoult', 'hexlet') is True
    assert scrabble('katas', 'steak') is False
    assert scrabble('scriptjava', 'javascript') is True
    assert scrabble('scriptingjava', 'javascript') is True
    assert scrabble('scriptjavest', 'javascript') is False
    assert scrabble('', 'hexlet') is False
    assert scrabble('scriptingjava', 'JavaScript') is True
    print('test_scrabble is Ok!')

test_scrabble()