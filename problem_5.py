"""
Problem: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 
"""

"""
This doesn't even require any programming. You just need to include the "highest power possible" for each prime factor
under 20. "highest power possible" means using the highest possible power without going over 20. For example, 2^4 is
under 20, but 2^5 is over. So use 2^4.

Answer: 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19

Proof: Every integer can be written as p1^x1 * p2^x2 * ... * pn^xn where pk is the kth prime and xn is some
coefficient greater than or equal to 0. So, if all pi's are less than 20, and we maximize xi s.t. pi^xi <= 20,
then we can represent each integer 1-20 with some subset of s. If we can't, then we are either missing some prime
(but we aren't, we have included 2, 3, 5, 7, 11, 13, 17, 19 and there are no more primes less than 20), OR we are
missing a coefficient on one of our primes (but we aren't, because we maximized xi subject to constraint pi^xi <= 20).
"""

print(2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19)