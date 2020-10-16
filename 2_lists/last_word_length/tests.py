from solution import length_of_last_word

def test_length_of_last_word():
    strings = ['', ' \t\n', 'hi', '  cat', 'man in black', 'hello, world!', 'hello, wOrLd!    ', 'hello\t\nworld']
    answers = [0, 0, 2, 3, 5, 6, 6, 5]
    results = []
    for string in strings:
        results.append(length_of_last_word(string))
    for i in range(len(answers)):
        if answers[i] == results[i]:
            next
        else:
            raise Exception(f'test_same_parity_filter Failed! For {repr(strings[i])} has answer > {results[i]}')
    print('test_length_of_last_word is Ok!')

test_length_of_last_word()
    
