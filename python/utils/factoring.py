def find_largest_prime_factor_for_odd_number(n):
    """
    Proof/explaination of algo: Every integer can be written as n = p1^x1 * p2^x2 * ... * pn^xn, where pk is the kth prime.
    So, WLOG, assuming n % p1 == 0, we can divide out all instances of p1 and get
    divisor = p2^x2 * ... * pn^xn. We test for whether our current divisor is divisible by the next possible_factor.
    If possible_factor is not prime, it will not divide divisor, since all of the prime factors composing divisor
    have already been divided out.
    """
    return factor(n)[-1]

def factor(n):
    prime_factors = [] # TODO: Clean up this function
    divisor = n
    possible_factor = 2
    while divisor % possible_factor == 0:
        divisor /= possible_factor
        prime_factors.append(possible_factor)
    possible_factor = 3
    while divisor > 1:
        while divisor % possible_factor == 0:
            divisor /= possible_factor
            prime_factors.append(possible_factor)
        possible_factor += 2

    return prime_factors


# Quick test
assert find_largest_prime_factor_for_odd_number(31) == 31
assert find_largest_prime_factor_for_odd_number(33) == 11
# This test is really the inspiration for the solution.
assert find_largest_prime_factor_for_odd_number(13 * 13 * 13 * 17) == 17

assert factor(31) == [31]
assert factor(22) == [2, 11]
assert factor(2**4 * 3**2 * 17 * 23) == [2, 2, 2, 2, 3, 3, 17, 23]