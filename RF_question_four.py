# # -*- coding: utf-8 -*-
def flip(some_list):
    if some_list == reversed(some_list):
        return some_list
    else:
        return flip(some_list[-1])
print(flip(1, 2, 3))