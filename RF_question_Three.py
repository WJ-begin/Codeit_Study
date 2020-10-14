# # -*- coding: utf-8 -*-
def sum_digits(n):
    # base case
    if n < 10:
        return n

    # recursive case
    return n % 10 + sum_digits(n // 10)
print(sum_digits(12102))