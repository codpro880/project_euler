"""
Problem: What is the 10 001st prime number?
"""


def main():
    print(find_nth_prime(10001))

def find_nth_prime(n):
    primes = [2, 3]
    possible_prime = primes[-1] + 2
    while len(primes) < n:
        if _is_prime(possible_prime, primes):
            primes.append(possible_prime)
        possible_prime += 2

    return primes[-1]

def _is_prime(possible_prime, primes):
    for prime in primes:
        if possible_prime % prime == 0:
            return False

    return True

assert find_nth_prime(3) == 5
assert find_nth_prime(10) == 29  # 2, 3, 5, 7, 11, 13, 17, 19, 23, 29

main()