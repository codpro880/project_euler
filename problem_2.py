""" 
Problem: By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""

def fib():
    yield 1
    yield 2
    first = 1
    second = 2
    while True:
        yield first + second
        first, second = second, first + second

def sum_even_fib_less_than_4mil():
    fib_gen = fib()
    cur_fib = next(fib_gen)
    result = 0
    while cur_fib < 4000000:
        if cur_fib % 2 == 0:
            result += cur_fib
        cur_fib = next(fib_gen)
    return result

print(sum_even_fib_less_than_4mil())