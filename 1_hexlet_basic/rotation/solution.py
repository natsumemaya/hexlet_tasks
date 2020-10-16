#В этом испытании вы будете работать с "тройками" — кортежами из трёх элементов. Вам предстоит реализовать две функции, которые "вращают" тройку влево и вправо. Как это выглядит, вы можете понять из пары примеров:

#>>> triple = ('A', 'B', 'C')
#>>> rotate_left(triple)
#('B', 'C', 'A')
#>>> rotate_right(triple)
#('C', 'A', 'B')


def rotate_right(triple):
    (a, b, c) = triple
    return (c, a, b)

def rotate_left(triple):
    (a, b, c) = triple
    return (b, c, a)