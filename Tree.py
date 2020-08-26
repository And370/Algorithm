# 不考虑重复节点

class Node(object):
    """
    节点.
    """

    def __init__(self, element):
        self.element = element
        self.left: Node = None
        self.right: Node = None

    def __repr__(self):
        return """Node("%s")""" % self.element

    def __str__(self):
        return str(self.element)


class BaseBinaryTree(object):
    """
    基础二叉树.
    """

    def __init__(self, node: Node = None):
        self.root = node

    def __repr__(self):
        return """BaseTree("%s")""" % self.root

    def __str__(self):
        return str(self.root)

    def insert(self, element):
        """
        根左右顺序添加.
        """
        node = Node(element)
        # 根节点优先添加
        if not self.root:
            self.root = node
            return
        else:
            # 此处建立队列
            queue = [self.root]
            while queue:
                current_node = queue.pop(0)
                # 对当前节点进行空值判断,添加顺序先左后右
                if not current_node.left:
                    current_node.left = node
                    return
                elif not current_node.right:
                    current_node.right = node
                    return
                # 都不为空则下探，FIFO
                else:
                    queue.append(current_node.left)
                    queue.append(current_node.right)


class BinarySortTree(BaseBinaryTree):
    """
    二叉排序树/二叉搜索树.
    """

    def insert(self, element):
        """
        排序插入.
        """
        node = Node(element)
        if not self.root:
            self.root = node
            return
        else:
            # 此处建立队列
            current_node = self.root
            while True:
                # 元素与当前节点判断大小
                if element < current_node.element:
                    # 若左节点存在,加入比较队列,否则插入
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = node
                        return
                elif element > current_node.element:
                    if current_node.right:
                        current_node = current_node.left
                    else:
                        current_node.left = node
                        return
                # 重复值报错
                else:
                    raise ValueError("Element is repeated.")


def max_depth(node=None):
    """
    :param node:
    :return: 最大树深
    """
    if not node:
        return 0
    max_depth_left = max_depth(node.left)
    max_depth_right = max_depth(node.right)
    return max(max_depth_left, max_depth_right) + 1


def min_depth(node=None):
    """
    :param node:
    :return: 最小树深
    """
    if not node:
        return 0
    min_depth_left = min_depth(node.left)
    min_depth_right = min_depth(node.right)
    return min(min_depth_left, min_depth_right) + 1


def nodes_count(node=None):
    """
    节点数量计算
    :param node:
    :return: 节点数量
    """
    if not node:
        return 0
    return nodes_count(node.left) + nodes_count(node.right) + 1


def leaf_nodes_count(node=None):
    """
    叶子节点数量计算
    这里容易卡在都以node左右子节点的情况来判断是否叶子节点，导致递归被短路无法正确进行
    可以将return 0的条件建立在叶子节点不存在的"子节点"上
    :param node:
    :return: 叶子节点数量
    """
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return leaf_nodes_count(node.left) + leaf_nodes_count(node.right)


def nodes_count_k_level(node=None, k=0):
    """
    第k层的节点数量
    这里递归从根节点逐渐将二叉树分解为子树,取其k-1层
    当k=1时,即将第k层的节点定义为单节点子树
    逐层累加返回
    :param node:
    :param k: 第k层
    :return: 第k层的节点数量
    """
    if k < 1 or not node:
        return 0
    if k == 1:
        return 1
    return nodes_count_k_level(node.left, k - 1) + nodes_count_k_level(node.right, k - 1)


def pre_order_traversal(node=None):
    """
    前序遍历
    TODO
    :param node:
    :return:
    """
    pass


def is_balanced(node=None):
    """
    平衡二叉树判断
    TODO
    :param node:
    :return:
    """
    pass


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
    bbt = BaseBinaryTree()
    for i in range(10):
        bbt.insert(i)

    funcs = [max_depth, min_depth, nodes_count, leaf_nodes_count, is_balanced]
    func_test(funcs, bbt.root)

    print(nodes_count_k_level.__name__, ":", nodes_count_k_level(bbt.root, 3))

    bst = BinarySortTree()
    for i in range(10):
        bst.insert(i)
