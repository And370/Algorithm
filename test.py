# -*- coding: utf-8 -*-
# author:And370
# time:2020/8/15
import random
from Sort import *


def check(func,*args):
    to_sort = [random.randrange(1, 10000) for i in range(5)]
    return func(to_sort,*args) == sorted(to_sort)


if __name__ == "__main__":
    print(check(shell_insert_sort,"normal"))
