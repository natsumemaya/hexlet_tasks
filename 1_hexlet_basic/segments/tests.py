from solution import is_degenerated, is_horizontal, is_inclined, is_vertical

VERTICAL = (15, 5), (15, -5)
HORIZONTAL = (5, 15), (-5, 15)
DEGENERATED = (42, 100), (42, 100)
INCLINED = (0, 0), (1, 1)


def test_is_vertical():
    print('Is verical test:')
    print(VERTICAL, is_vertical(VERTICAL))
    print(HORIZONTAL, not is_vertical(HORIZONTAL))
    print(DEGENERATED, not is_vertical(DEGENERATED))
    print(INCLINED, not is_vertical(INCLINED))


def test_is_horizontal():
    print('Is horizontal test:')
    print(VERTICAL, not is_horizontal(VERTICAL))
    print(HORIZONTAL, is_horizontal(HORIZONTAL))
    print(DEGENERATED, not is_horizontal(DEGENERATED))
    print(INCLINED, not is_horizontal(INCLINED))


def test_is_degenerated():
    print('Is degenerated test:')
    print(VERTICAL, not is_degenerated(VERTICAL))
    print(HORIZONTAL, not is_degenerated(HORIZONTAL))
    print(DEGENERATED, is_degenerated(DEGENERATED))
    print(INCLINED, not is_degenerated(INCLINED))


def test_is_inclined():
    print('Is inclined test:')
    print(VERTICAL, not is_inclined(VERTICAL))
    print(HORIZONTAL, not is_inclined(HORIZONTAL))
    print(DEGENERATED, not is_inclined(DEGENERATED))
    print(INCLINED, is_inclined(INCLINED))

test_is_vertical()
test_is_horizontal()
test_is_degenerated()
test_is_inclined()