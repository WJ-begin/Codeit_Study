# # -*- coding: utf-8 -*-
def triangle_number(n):
    if n == 0:
        return n
    return n + triangle_number(n - 1)
print(triangle_number(11))