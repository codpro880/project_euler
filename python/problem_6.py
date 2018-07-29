"""
Problem: Find the difference between the sum of the squares of the first one hundred natural numbers
and the square of the sum.
"""

def main():
    sum_of_squares = sum_of_squares_up_to(100)
    square_of_sum = square_of_sum_up_to(100)
    print(square_of_sum - sum_of_squares)

def sum_of_squares_up_to(n):
    sum = 0
    for i in range(n + 1):
        sum += i**2
    return sum

def square_of_sum_up_to(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum ** 2

main()