"""
Problem: Find the largest palindrome made from the product of two three digit numbers.
"""
def is_palindrome(x):
    return str(x) == str(x)[::-1]

palindromes = []
for x in range(999)[:50:-1]:
    for y in range(999)[:50:-1]:
        if is_palindrome(x * y):
            palindromes.append(x * y)

print(max(palindromes))