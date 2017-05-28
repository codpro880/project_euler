"""
What is the value of the first triangle number to have over five hundred divisors?
"""
import itertools
from utils import factoring


def main():
    print(first_triangle_number_with_500_divisors())

def first_triangle_number_with_500_divisors():
    for triangle_number in triangle_numbers():
        prime_factors = factoring.factor(triangle_number)
        if get_num_of_divisors(prime_factors) > 500:
            return triangle_number


def triangle_numbers():
    for n in itertools.count(start=1, step=1):
        yield n * (n+1) / 2

def get_num_of_divisors(prime_factors):
    prime_factors = condense_prime_factors_to_primes_and_powers(prime_factors)
    return multiply_powers_together(prime_factors)


def multiply_powers_together(prime_factors):
    result = 1
    for power in prime_factors.values():
        result *= (power + 1)
    return result


def condense_prime_factors_to_primes_and_powers(prime_factors):
    result = {}
    for prime_factor in prime_factors:
        if prime_factor in result.keys():
            result[prime_factor] += 1
        else:
            result[prime_factor] = 1
    return result

main()