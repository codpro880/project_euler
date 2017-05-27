"""
Problem: What is the largest prime factor of the number 600851475143 ?
"""


def main():
    print(find_largest_prime_factor_for_odd_number(600851475143))


def find_largest_prime_factor_for_odd_number(n):
    """
    Proof/explaination of algo: Every integer can be written as n = p1^x1 * p2^x2 * ... * pn^xn, where pk is the kth prime.
    So, WLOG, assuming n % p1 == 0, we can divide out all instances of p1 and get
    divisor = p2^x2 * ... * pn^xn. We test for whether our current divisor is divisible by the next possible_factor.
    If possible_factor is not prime, it will not divide divisor, since all of the prime factors composing divisor
    have already been divided out.
    """
    possible_factor = 3
    divisor = n
    while divisor > 1:
        while divisor % possible_factor == 0:
            divisor /= possible_factor
            max_prime_factor = possible_factor
        possible_factor += 2

    return max_prime_factor


# Quick test
assert find_largest_prime_factor_for_odd_number(31) == 31
assert find_largest_prime_factor_for_odd_number(33) == 11
# This test is really the inspiration for the solution.
assert find_largest_prime_factor_for_odd_number(13*13*13*17) == 17

main()
