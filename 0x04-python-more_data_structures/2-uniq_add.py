#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = []
    [res.append(x) for x in my_list if x not in res]
    return sum(res)
