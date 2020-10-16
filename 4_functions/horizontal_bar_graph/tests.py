from solution import histo

BIG_SAMPLE = (  # noqa: WPS317
    30, 15, 21, 19, 15, 25, 17, 27, 16, 16,
    21, 17, 24, 16, 16, 18, 20, 25, 28, 26,
    21, 21, 20, 26, 28, 27, 16, 26, 22, 15,
    20, 30, 21, 21, 19, 18, 30, 22, 24, 24,
    19, 23, 27, 15, 24, 25, 21, 16, 21, 24,
    21, 29, 27, 19, 19, 25, 26, 27, 27, 22,
    16, 23, 24, 15, 24, 23, 22, 20, 22, 17,
    21, 29, 16, 27, 18, 19, 28, 17, 18, 21,
    30, 26, 28, 22, 29, 30, 28, 30, 17, 26,
    18, 17, 17, 26, 21, 27, 20, 29, 29, 30,
)

SMALL_SAMPLE = (  # noqa: WPS317
    21, 23, 23, 25, 24, 21, 25, 24, 22, 21,
)


def test_histo():
    assert histo([], min_value=10, max_value=15) == """
10|
11|
12|
13|
14|
15|
""".strip()

    assert histo([3, 3, 5, 6, 6], min_value=1, bar_char='%') == """
1|
2|
3|%% 2
4|
5|% 1
6|%% 2
""".strip()

    assert histo(BIG_SAMPLE) == """
15|##### 5
16|######## 8
17|####### 7
18|##### 5
19|###### 6
20|##### 5
21|############ 12
22|###### 6
23|### 3
24|####### 7
25|#### 4
26|####### 7
27|######## 8
28|##### 5
29|##### 5
30|####### 7
""".strip()

    assert histo(SMALL_SAMPLE, min_value=22, max_value=27) == """
22|# 1
23|## 2
24|## 2
25|## 2
26|
27|
""".strip()
    print('test_histo is Ok!')

test_histo()


# from collections import Counter

# def histo(samples, min_value=None, max_value=None, bar_char='#'):
#     """Draws a horizontal histogram."""
#     start_value = min_value or min(samples)
#     end_value = max_value or max(samples)
#     res = []
#     d = dict(Counter(samples))
#     for i in range(start_value, end_value + 1):
#         elem = d.get(i)
#         s = '{:d}|'.format(i)
#         if elem:
#             s += '{} {:d}'.format(bar_char * elem, elem)
#         res.append(s)
#     return '\n'.join(res)

# from collections import Counter

# def histo(samples, min_value=None, max_value=None, bar_char='#'):
#     """Draws a horizontal histogram."""  # noqa: DAR101, DAR201

#     min_value = min_value or min(samples)
#     max_value = max_value or max(samples)
#     c = Counter(samples)
#     axis = range(min_value, max_value + 1)
#     output = [
#         f'{x}|{bar_char * c[x]} {c[x]}'  # noqa: WPS305
#         if x in c else f'{x}|' for x in axis  # noqa: WPS305
#     ]
#     return '\n'.join(output)