from solution import hamming_weight

def test_hamming():
    numbers = [0, 1, 5, 10, 101, 12345]
    answers = [0, 1, 2, 2, 4, 6]
    results = []
    for number in numbers: 
        results.append(hamming_weight(number))
    for i in range(len(answers)):
        if answers[i] == results[i]:
            next
        else:
            raise Exception(f'test_same_parity_filter Failed! For {numbers[i]} as {bin(numbers[i])[2:]} has answer > {results[i]}')
    print('test_hamming is Ok!')




    

test_hamming()