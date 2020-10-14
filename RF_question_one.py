# # -*- coding: utf-8 -*-
def fib(n):
    if n == 0:
        return n
    else:
        fib(n-1)
        print('{} * {} = {}'.format(n, (n+1), n*(n+1)))
fib(10)