"""
sample:
import random
mbh = MinBinaryHeap()
datas = {random.randrange(1,100) for i in range(30)}
for data in datas:
    mbh.add(data)
mbh.root
mbh.root.left
mbh.root.left.left
mbh.root.left.left.right
mbh.left(5)

or

mbh.root.element
mbh.root.left.element
mbh.root.left.left.element
mbh.root.left.left.right.element
mbh.left(5)

"""


class BinaryHeap(object):
    """
    最小/大堆定义：
    必须是完全二叉树
    任一结点的值是其子树所有结点的最大值或最小值
    """

    def __init__(self, root=None, mode="min"):
        self.elements = [root]
        self.root = self.elements[0]
        self.mode = True if mode == "min" else False

    def __repr__(self):
        return """BaseBinaryHeap("%s")""" % self.root

    def __getitem__(self, directions):
        if isinstance(directions, int):
            return self.elements[directions]
        elif isinstance(directions, list):
            index = 0
            for direction in directions:
                if direction == "left":
                    index = index * 2 + 1
                elif direction == "right":
                    index = index * 2 + 2
                elif direction == "parent":
                    index = (index - 1) // 2
                if not (index < len(self.elements) and index >= 0):
                    raise Exception("node index out of range")
            return self.elements[index]
        else:
            raise Exception("%s is not expected." % type(directions))

    def add(self, element):
        if self.elements[0] is None:
            self.elements[0] = element
        else:
            self.elements.append(element)
        self._sort()

    def swap(self, index_a, index_b):
        self.elements[index_a], self.elements[index_b] = self.elements[index_b], self.elements[index_a]

    def _sort(self):
        index = len(self.elements) - 1
        parent_index = self.parent_index(index)
        while True:
            # TODO
            # if self.elements[parent_index] == self.elements[index]:
            #     raise ValueError("Element %s is repeated." % self.elements[index])
            if self.elements[parent_index] > self.elements[index] and self.mode:
                self.swap(parent_index, index)
                index = parent_index
                parent_index = self.parent_index(index)
            else:
                break

    def delete(self):
        # TODO
        pass

    def index_check(self):
        # TODO
        # if (index - 1) // 2 >= 0 and (index - 1) // 2 < len(self.elements)
        pass

    def left_index(self, index):
        return index * 2 + 1

    def right_index(self, index):
        return index * 2 + 2

    def parent_index(self, index):
        return (index - 1) // 2


def func_test(funcs, node=None):
    """
    测试函数
    :param funcs:
    :param node:
    :return:
    """
    for func in funcs:
        print(func.__name__, ":", func(node))


if __name__ == "__main__":
    # 基础二叉堆
    mbh = BinaryHeap()
    for i in range(15, 0, -1):
        # 逐层顺序插入
        mbh.add(i)
    print(mbh.elements)
    print(mbh.left_index(3))
