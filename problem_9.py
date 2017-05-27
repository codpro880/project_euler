"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math


def main():
    for possible_triple in generate_possible_triples():
        a, b, c = possible_triple
        if a + b + c == 1000 and is_pythagorean_triple(a, b, c):
            print(a * b * c)


def generate_possible_triples():
    """ Just make sure we satisfy a < b < c """
    for c in range(1001):
        for b in range(c):
            for a in range(b):
                yield a, b, c


def is_pythagorean_triple(a, b, c):
    return a**2 + b**2 == c**2 and is_perfect_square(a**2 + b**2)


def is_perfect_square(x):
    return math.sqrt(x) == int(math.sqrt(x))


main()