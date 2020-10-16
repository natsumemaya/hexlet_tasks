from solution import int2ip, ip2int

ZEROES = '0.0.0.0'  # noqa: S104


def test_ip2int():
    assert ip2int(ZEROES) == 0
    assert ip2int('128.32.10.1') == 2149583361
    print("test_ip2int is Ok!")


def test_int2ip():
    assert int2ip(0) == ZEROES
    assert int2ip(2149583361) == '128.32.10.1'
    print('test_int2ip is Ok!')


def test_round_robin():
    assert int2ip(ip2int('192.168.1.32')) == '192.168.1.32'
    assert ip2int(int2ip(2149583361)) == 2149583361
    print('test_round_robin is Ok!')

test_ip2int()
test_int2ip()
test_round_robin()