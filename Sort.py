# -*- coding: utf-8 -*-
# author:And370
# time:2020/8/15


def swap(to_exchange, i, j):
    to_exchange[i], to_exchange[j] = to_exchange[j], to_exchange[i]


# 1.1 冒泡排序，一开始理解不透彻，以是否发生交换为条件
def bubble_sort_1(to_sort: list):
    if len(to_sort) >= 2:
        changed = True
        while changed:
            changed = False
            for index in range(len(to_sort) - 1):
                if to_sort[index] > to_sort[index + 1]:
                    swap(to_sort, index, index + 1)
                    changed = True
    return to_sort


# 1.2 冒泡排序，以缩小比较范围为过程
def bubble_sort_2(to_sort: list):
    if len(to_sort) >= 2:
        for index in range(len(to_sort)):
            for index in range(len(to_sort) - 1):
                if to_sort[index] > to_sort[index + 1]:
                    swap(to_sort, index, index + 1)
    return to_sort


# 2.1 直接插入排序
def insert_sort(to_sort: list):
    if len(to_sort) >= 2:
        # 默认首位为左侧有序列首位
        # 遍历列表
        for index in range(1, len(to_sort)):
            # 取无序区首位自有序区末位起逐步比较元素
            # 若持续小于则持续发生交换,否则停止
            while to_sort[index] < to_sort[index - 1] and index >= 1:
                swap(to_sort, index, index - 1)
                index -= 1
    return to_sort


# 2.2 折半插入排序
# 在直接插入的基础上减少了对有序区的比较
def binary_insert_sort(to_sort: list):
    if len(to_sort) >= 2:
        # 默认首位为左侧有序列首位
        # 遍历列表
        for index in range(1, len(to_sort)):
            # TODO
            # 取无序区首位自有序区二分位起逐步比较元素
            # 若持续小于则持续发生交换,否则停止
            while to_sort[index] < to_sort[index - 1] and index >= 1:
                swap(to_sort, index, index - 1)
                index -= 1
    return to_sort


# 2.3 直接插入排序
# 为适配希尔排序直接调用,抽象起始点与间隔指定
# 默认参数即为直接插入排序
def insert_sort_by_indexes(to_sort: list, start=0, gap=1):
    if len(to_sort) >= 2:
        # 默认首位为左侧有序列首位
        # 遍历列表
        for index in range(start + gap, len(to_sort)):
            # 取无序区首位自有序区末位起逐步比较元素
            # 若持续小于则持续发生交换,否则停止
            while to_sort[index] < to_sort[index - gap] and index >= gap:
                swap(to_sort, index, index - gap)
                index -= gap
    return to_sort


# 2.4 希尔排序/缩小间隔插入排序
def shell_insert_sort(to_sort: list, mode: str = "normal"):
    if len(to_sort) >= 2:
        # 三种增量序列
        mode = mode.lower()
        if mode in ["normal", "hibbard", "sedgewick"]:
            if mode == "sedgewick":
                gaps = []
                # TODO
                # while
                gaps.reverse()
                # 完成一趟交换,缩小间隔,地板除2,直到完成gap=1的最后一趟直接插入排序
                for gap in gaps:
                    # gap为n时,则存在n组列表,列表起点为0~(n-1)
                    for start in range(gap):
                        # 执行插入排序
                        insert_sort_by_indexes(to_sort, start=start, gap=gap)
            if mode == "normal":
                gap = len(to_sort) // 2
            elif mode == "hibbard":
                gap = 1
                while gap * 2 < len(to_sort):
                    gap *= 2
                gap = gap - 1
            # 完成一趟交换,缩小间隔,地板除2,直到完成gap=1的最后一趟直接插入排序
            while gap:
                # gap为n时,则存在n组列表,列表起点为0~(n-1)
                for start in range(gap):
                    # 执行插入排序
                    insert_sort_by_indexes(to_sort, start=start, gap=gap)
                gap //= 2

        else:
            raise Exception("""Mode is not in ["normal", "hibbard", "sedgewick"].""")
    return to_sort


def sedgewick_array(n):
    i = 0
    j = 0
    while n:
        a = 9 * (4 ** i) - 9 * (2 ** i) + 1
        b = 4 ** j - 3 * (2 ** j ) + 1
        if a == 1:
            yield a
            i += 1
        elif a > b:
            i += 1
            yield a
        else:
            j += 1
            yield b
        n -= 1


# 3.选择排序
def selection_sort(to_sort: list):
    if len(to_sort) >= 2:
        for i in range(len(to_sort[:-1])):
            # 默认首位为左侧有序列首位
            min_index = i
            # 取右侧无序列最小值
            for j in range(i + 1, len(to_sort)):
                min_value = to_sort[min_index]
                if to_sort[j] < min_value:
                    min_index = j
            # print(to_sort[min_index], to_sort[i])
            # 交换最小值与无序列首位,归入有序列末位
            swap(to_sort, i, min_index)
    return to_sort


# 4.归并排序
def merge_sort(to_sort: list):
    if len(to_sort) >= 2:
        list1, list2 = partition(to_sort)
        return concat_sort(merge_sort(list1), merge_sort(list2))
    return to_sort


def partition(to_part: list):
    index = int(len(to_part) / 2)
    return to_part[index:], to_part[:index]


def concat_sort(list1: list, list2: list):
    i, j = 0, 0
    len_1, len_2 = len(list1), len(list2)
    result = []
    while i < len_1 and j < len_2:
        if list1[i] <= list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    result += list1[i:]
    result += list2[j:]
    return result
