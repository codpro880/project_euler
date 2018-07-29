"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6
routes to the bottom right corner. How many such routes are there through a 20×20 grid?
"""

"""
This one is certainly hard to explain by text, but the solution hinges on the fact that we only have to
compute how many ways there are to get to the center diagonal, and then noticing that we need to add the
'in between points' to get to the next iterations solution (hence pascal's triangle)
"""

def main():
    pascal_triangle_20th_row = compute_pascal_triangle(20)
    print(sum([x**2 for x in pascal_triangle_20th_row]))

def compute_pascal_triangle(n):
    for r in range(n + 1):
        yield nCr(n, r)

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1

def nCr(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

assert nCr(5,1) == 5
assert nCr(5,2) == 10
assert nCr(5,3) == 10
assert nCr(5,4) == 5

main()