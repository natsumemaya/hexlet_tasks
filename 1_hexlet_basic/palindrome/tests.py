from solution import is_palindrome

words = [('rotor', True), ('abba', True), ('r', True), ('', True), ('motor', False), ('bulb', False), ('blablab', False)]

for word in words:
    wrd, bolean = word
    answer = is_palindrome(wrd) == bolean
    if answer:
        print(repr(wrd), 'is', bolean)
    else:
        raise Exception(f"Sorry, your answer for {repr(wrd)}, not correct")