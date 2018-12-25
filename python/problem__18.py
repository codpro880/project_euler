# Just copy/pasta-ed from project euler
problem_triangle_str = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

def sum_up_from_bottom(triangle_str):
    tri_arr = parse_triangle_into_array(triangle_str)
    while len(tri_arr) > 1:
        tri_arr = sum_bottom_row(tri_arr)
    return tri_arr[0]

def sum_bottom_row(tri_arr):
    bottom_row = tri_arr[-1]
    upper_row = tri_arr[-2]
    result_row = []
    for first, second, upper_row_item in zip(bottom_row, bottom_row[1:], upper_row):
        max_ = max(first, second)
        result_row.append(max_ + upper_row_item)

    tri_arr[-2] = result_row
    tri_arr = tri_arr[:-1]
    return tri_arr

def parse_triangle_into_array(triangle_str):
    rows_str = triangle_str.split("\n")
    triangle_arr = [[int(x) for x in row.split(' ') if x] for row in rows_str]
    if triangle_arr[-1]:
        return triangle_arr
    else:
        return triangle_arr[:-1]

if __name__ == "__main__":
    """ Some quick tests...TODO: move to test suite. """
    triangle_str = """3
7 4
2 4 6
8 5 9 3
"""
    tri_arr = parse_triangle_into_array(triangle_str)

    assert tri_arr[0] == [3]
    assert tri_arr[1] == [7, 4]
    assert tri_arr[2] == [2, 4, 6]
    assert tri_arr[3] == [8, 5, 9, 3]

    bottom_row_summed = sum_bottom_row(tri_arr)
    assert bottom_row_summed[-1] == [8 + 2, 9 + 4, 9 + 6]

    result = sum_up_from_bottom(triangle_str)
    assert result[0] == 23

    print(sum_up_from_bottom(problem_triangle_str))
