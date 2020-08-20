# -*- coding: utf-8 -*-
# author:And370
# time:2020/8/15
import random
from Sort import *


def check(func,*args):
    to_sort = [random.randrange(1, 1000) for i in range(500)]
    return func(to_sort,*args) == sorted(to_sort)


if __name__ == "__main__":
    # print(check(quick_sort))
    to_sort = [random.randrange(1, 100) for i in range(10)]
    # print(to_sort)
    print(quick_sort(to_sort))
