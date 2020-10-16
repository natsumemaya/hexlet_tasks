from solution import fizz_buzz

def test_fizz_buzz():
    print((1,0), fizz_buzz(1, 0) == '')
    print((7,7), fizz_buzz(7, 7) == '7')
    print((1,5), fizz_buzz(1, 5) == '1 2 Fizz 4 Buzz')
    print((11,20), fizz_buzz(11, 20) == '11 Fizz 13 14 FizzBuzz 16 17 Fizz 19 Buzz')

test_fizz_buzz()