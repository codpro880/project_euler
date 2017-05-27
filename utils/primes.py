import math

def find_nth_prime(n):
    return _generate_primes(n, len, -1)

def primes_less_than(n):
    return _generate_primes(n, lambda x: x[-1], slice(0,-1))

def _generate_primes(n, while_condition, slice_=None):
    primes = [2, 3]
    possible_prime = primes[-1] + 2
    while while_condition(primes) < n:
        if _is_prime(possible_prime, primes):
            primes.append(possible_prime)
        possible_prime += 2

    return primes[slice_]

def _is_prime(possible_prime, primes):
    for prime in primes:
        if math.sqrt(possible_prime) < prime:
            return True
        if possible_prime % prime == 0:
            return False

assert find_nth_prime(3) == 5
assert find_nth_prime(10) == 29

assert primes_less_than(10) == [2, 3, 5, 7]
assert primes_less_than(30) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

assert set(primes_less_than(100)) < set(primes_less_than(110))
