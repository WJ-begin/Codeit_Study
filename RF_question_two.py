# # -*- coding: utf-8 -*-
def triangle_number(n):
    if n == 0:
        return n
    else:
        triangle_number(n-1)
        print('{}'.format(n*(n+1)//2))
triangle_number(11)