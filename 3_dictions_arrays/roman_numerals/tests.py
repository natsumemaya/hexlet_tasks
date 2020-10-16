from solution import to_arabic, to_roman

def test_to_roman():
    assert to_roman(0) == ''
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'
    assert to_roman(6) == 'VI'
    assert to_roman(27) == 'XXVII'
    assert to_roman(48) == 'XLVIII'
    assert to_roman(59) == 'LIX'
    assert to_roman(93) == 'XCIII'
    assert to_roman(141) == 'CXLI'
    assert to_roman(163) == 'CLXIII'
    assert to_roman(402) == 'CDII'
    assert to_roman(575) == 'DLXXV'
    assert to_roman(911) == 'CMXI'
    assert to_roman(1024) == 'MXXIV'
    assert to_roman(2020) == 'MMXX'
    assert to_roman(3000) == 'MMM'
    print('test_to_roman is Ok!')

def test_to_arabic():
    assert to_arabic('') == 0
    assert to_arabic('I') == 1
    assert to_arabic('II') == 2
    assert to_arabic('IV') == 4
    assert to_arabic('V') == 5
    assert to_arabic('VI') == 6
    assert to_arabic('XXVII') == 27
    assert to_arabic('XLVIII') == 48
    assert to_arabic('LIX') == 59
    assert to_arabic('XCIII') == 93
    assert to_arabic('CXLI') == 141
    assert to_arabic('CLXIII') == 163
    assert to_arabic('CDII') == 402
    assert to_arabic('DLXXV') == 575
    assert to_arabic('CMXI') == 911
    assert to_arabic('MXXIV') == 1024
    assert to_arabic('MMXX') == 2020
    assert to_arabic('MMM') == 3000
    assert to_arabic('IIII') is False
    assert to_arabic('VX') is False
    print('test_to_arabic is Ok!')

test_to_roman()
test_to_arabic()