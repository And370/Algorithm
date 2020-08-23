# -*- coding: utf-8 -*-
# author:And370
# time:2020/8/15
import random
from Sort import *
from Markov import *

def check(func,*args):
    to_sort = [random.randrange(1, 10000) for i in range(5)]
    return func(to_sort,*args) == sorted(to_sort)


if __name__ == "__main__":
    for i in range(3, 7):
        print(i, MonteCarloTimes(times=100000, dimension=i))
