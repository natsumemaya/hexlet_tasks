from solution import rotate_left, rotate_right

TRIPLE = (42, 'a', None)

print('TRIPLE', TRIPLE)

def test_rotate_left():
    print('rotate_left:', ('a', None, 42))
    print(rotate_left(TRIPLE) == ('a', None, 42))
    if rotate_left(rotate_left(rotate_left(TRIPLE))) == TRIPLE:
        print('test Ok!')
    else:
        raise Exception('Rotation for 3 times != TRIPLE')

def test_rotate_right():
    print('rotate_right:',(None, 42, 'a'))
    print(rotate_right(TRIPLE) == (None, 42, 'a'))
    if rotate_right(rotate_right(rotate_right(TRIPLE))) == TRIPLE:
           print('test Ok!')
    else:
        raise Exception('Rotation for 3 times != TRIPLE')

test_rotate_left()
test_rotate_right()