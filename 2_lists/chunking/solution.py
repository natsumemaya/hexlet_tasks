#Реализуйте функцию chunked, которая принимает на вход число и последовательность. Число которое задает размер чанка (куска). Функция должна вернуть список, состоящий из чанков указанной размерности. При этом список должен делиться на куски-списки, строка — на строки, кортеж — на кортежи!

#>>> chunked(2, ['a', 'b', 'c', 'd'])
#[['a', 'b'], ['c', 'd']]
#>>> chunked(3, ['a', 'b', 'c', 'd'])
#[['a', 'b', 'c'], ['d']]
#>>> chunked(3, 'foobar')
#['foo', 'bar']
#>>> chunked(10, (42,))
#[(42,)]

#def chunked(size, source):
#    result = []
#    index = 0
#    while index < len(source):
#        result.append(source[index:index + size])
#        index += size
#    return result

#def chunked(chunk, sequence):
#    chunks = []
#    for counter in range(0, len(sequence), chunk):
#        current_chunk = slice(counter, counter + chunk, 1)
#        chunks.append(sequence[current_chunk])
#    return chunks

def chunked(chunk, sequence):
    result = []
    while sequence:
        result.append(sequence[:chunk])
        sequence = sequence[chunk:]
    return result