"""
Which starting number, under one million, produces the longest (collatz) chain?
"""


def main():
    collatz_under_1m = [(n, collatz_chain_len(n)) for n in range(1000001)]
    print(max(collatz_under_1m, key=lambda x: x[1]))


def collatz_chain_len(n):
    count = 1
    while n > 1:
        count += 1
        n = collatz(n)
    return count


def collatz(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

main()