import pairs

EMPTY = ''

def test_pair1():
    pair = pairs.cons('hi', 'hexlet')
    assert pairs.car(pair) == 'hi'
    assert pairs.cdr(pair) == 'hexlet'
    print('test_pair1 is Ok!')

def test_pair2():
    pair = pairs.cons('Hello!', EMPTY)
    assert pairs.car(pair) == 'Hello!'
    assert pairs.cdr(pair) == EMPTY
    print('test_pair2 is Ok!')

def test_pair3():
    pair = pairs.cons(EMPTY, 'XXI')
    assert pairs.car(pair) == EMPTY
    assert pairs.cdr(pair) == 'XXI'
    print('test_pair3 is Ok!')

test_pair1()
test_pair2()
test_pair3()