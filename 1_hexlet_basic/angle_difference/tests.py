from solution import diff


def test_diff_modularity():
    print("(720, 0)", diff(720, 0) == 0)
    print("(-720, 0)", diff(-720, 0) == 0)


def test_diff_in_same_quadrant():
    print("(60, 30)", diff(60, 30) == 30)
    print("(125, 120)", diff(125, 120) == 5)
    print("(125, 120)", diff(200, 199) == 1)
    print("(300, 340)", diff(300, 340) == 40)


def test_diff_commutativity():
    print("(0, 90)", diff(0, 90) == diff(90, 0))
    print("(15, -15)", diff(15, -15) == diff(-15, 15))
    print("(45, 315)", diff(45, 315) == diff(315, 45))


def test_diff_difficult_cases():
    print("(0, 0)", diff(0, 0) == 0)
    print("(0, 180)", diff(0, 180) == 180)
    print("(30, 270)", diff(30, 270) == 120)
    print("(30, 240)", diff(30, 240) == 150)
    print("(240, 30)", diff(240, 30) == 150)

test_diff_modularity()
test_diff_in_same_quadrant()
test_diff_commutativity()
test_diff_difficult_cases()