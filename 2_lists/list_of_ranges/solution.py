# Реализуйте функцию summary_ranges, которая находит в списке непрерывные возрастающие последовательности чисел и возвращает список с их перечислением.

# Примеры
# >>> summary_ranges([])
# []
# >>> summary_ranges([1])
# []
# >>> summary_ranges([1, 2, 3])
# ['1->3']
# >>> summary_ranges([0, 1, 2, 4, 5, 7])
# ['0->2', '4->5']
# >>> summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5])
# ['110->112', '-5->-4']

def summary_ranges(numbers):
    if not numbers:
        return []
    ranges = []
    current_sequence = [numbers[0]]
    sequences = [current_sequence]
    for x, y in zip(numbers, numbers[1:]):
        if (y - x) == 1:
            current_sequence.append(y)
        else:
            current_sequence = [y]
            sequences.append(current_sequence)

    # здесь [0, 1, 2, 7, 5, 6] уже преобразован
    # в [[0, 1, 2], [7], [5, 6]]

    for sequence in sequences:
        if len(sequence) > 1:
            first, last = sequence[0], sequence[-1]
            ranges.append('{}->{}'.format(first, last))

    return ranges

# def summary_ranges(numbers):
#     if not numbers:
#         return []
#     current_seq = [numbers[0]]
#     ranges = [current_seq]

#     for x, y in zip(numbers, numbers[1:]):
#         if y - x == 1:
#             current_seq.append(y)
#         else:
#             current_seq = [y]
#             ranges.append(current_seq)
#     return [
#         f'{seq[0]}->{seq[-1]}' for seq in ranges if len(seq) > 1  # noqa: WPS305
#     ]

# def summary_ranges(seq):
#     result = []
#     if len(seq) < 2:
#         return result

#     tmp = []
#     current = seq[0]
#     for i in seq[1:]:
#         if i - current == 1:
#             tmp.append(current)
#         elif tmp:
#             tmp.append(current)
#             result.append(tmp[:])
#             tmp.clear()
#         current = i

#     if i - current == 1:
#         tmp.append(current)
#     elif tmp:
#         tmp.append(current)
#         result.append(tmp[:])

#     return ['{}->{}'.format(i[0], i[-1]) for i in result]