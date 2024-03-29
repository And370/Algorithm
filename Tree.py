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
        return """Node(%s)""" % self.element

    def __str__(self):
        return str(self.element)

    def __bool__(self):
        return False if self.element is None else True


class HuffmanNode(Node):
    """
    哈夫曼节点.
    增加父节点指针与权重
    """

    def __init__(self, element, char):
        super(HuffmanNode, self).__init__(element)
        self.data = char
        self.parent = None

    def __repr__(self):
        return """HuffmanNode(%s)""" % self.element


class BaseBinaryTree(object):
    """
    基础无序二叉树.
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
                # 都不为空则下探,FIFO
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
            # 从根节点开始
            current_node = self.root
            while True:
                # 元素与当前节点判断大小
                if element < current_node.element:
                    # 若节点存在,则比较,否则插入
                    if current_node.left:
                        current_node = current_node.left
                    else:
                        current_node.left = node
                        return
                elif element > current_node.element:
                    if current_node.right:
                        current_node = current_node.right
                    else:
                        current_node.right = node
                        return
                # 重复值报错
                else:
                    raise ValueError("Element %s is repeated." % element)


class HuffmanTree(BaseBinaryTree):
    """
    哈夫曼树/最优二叉树
    带权路径和最小
    大值放近，小值放远
    * 此处设定左节点小于右节点权重

    WPL = sum(Wi * Li)
    求和(节点权重 * 路径)


    应用价值在于可以提高信息熵
    降低高频信息哈夫曼编码字符长度
    优化了整体的传输字节
    """

    def __init__(self):
        super(HuffmanTree, self).__init__()
        del self.insert

    def __repr__(self):
        return """HuffmanTree("%s")""" % self.root

    # TODO
    # def from_data(self, wights2char: dict):
    #     if not all(isinstance(value, (int, float)) for value in wights2char.keys()):
    #         raise TypeError("Wight should be number.")
    #     self.wight_map = wights2char
    #     wights =
    #     while wights:
    #         h_node = HuffmanNode(None, None)
    #         if len(wights) >= 2:
    #             min_1, min_2 = wights.pop(0), wights.pop(0)
    #             h_node.left = HuffmanNode(element=min_1, char=wights2char[min_1])
    #             h_node.right = HuffmanNode(element=min_2, char=wights2char[min_2])
    #         else:


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
    这里容易卡在都以node左右子节点的情况来判断是否叶子节点,导致递归被短路无法正确进行
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
    为了对节点进行"第一次到达即执行操作"的遍历.
    :param node:
    :return:
    """
    elements = []
    if node:
        elements.append(node.element)
        elements.extend(pre_order_traversal(node.left))
        elements.extend(pre_order_traversal(node.right))
    return elements


def in_order_traversal(node=None):
    """
    中序遍历
    可为二叉排序树进行排序输出.
    :param node:
    :return:
    """
    elements = []
    if node:
        elements.extend(in_order_traversal(node.left))
        elements.append(node.element)
        elements.extend(in_order_traversal(node.right))
    return elements


def post_order_traversal(node=None):
    """
    后序遍历
    后续遍历的特点是确保执行操作时,已经遍历执行过该节点的左右子节点,
    故适用于要进行破坏性操作的情况,比如删除所有节点.
    :param node:
    :return:
    """
    elements = []
    if node:
        elements.extend(post_order_traversal(node.left))
        elements.extend(post_order_traversal(node.right))
        elements.append(node.element)
    return elements


def layer_traversal(node=None):
    """
    层序遍历
    :param node:
    :return:
    """
    elements = []
    queue = [node]
    while queue:
        node = queue.pop(0)
        elements.append(node.element)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return elements


def layer_traversal_with_deep(node=None):
    """
    带树深的层序遍历
    :param node:
    :return:
    """
    if not node:
        return {}
    elements = {}
    queues = {1: [node]}
    layer = 1
    while queues.get(layer):
        for current_node in queues[layer]:
            # 注意不要重复覆盖式创建
            if not elements.get(layer):
                elements[layer] = []
            if not queues.get(layer + 1):
                queues[layer + 1] = []
            elements[layer].append(current_node.element)
            if current_node.left:
                queues[layer + 1].append(current_node.left)
                # print(queues)
            if current_node.right:
                queues[layer + 1].append(current_node.right)
                # print(queues)
        layer += 1
    return elements


def is_complete_tree(node=None):
    """
    完全二叉树定义:
    从左向右逐层排列紧密
    除最后一层节点未满

    :param node:
    :return:
    """
    bottom_torched = False
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        if not bottom_torched:
            # 当左空右实,必然False
            if not current_node.left and current_node.right:
                return False
            # 将后续节点加入队列
            elif current_node.left and current_node.right:
                queue.extend([current_node.left, current_node.right])
            # 左实右空,开始触底
            elif current_node.left and not current_node.right:
                bottom_torched = True
        else:
            # 触底节点不应该再出现子节点：解决高差定义
            if current_node.left or current_node.right:
                return False
    return True


def is_full_binary_tree(node=None):
    """
    满二叉树定义:
    除最后一层所有节点均有左右节点.
    :param node:
    :return:
    """
    # 逐层检查当前层与下一层
    current_layer = [node]
    next_layer = []
    bottom_torched = False
    result = True
    # 两种非完全二叉树的情况:
    # 1.非最后一层,存在空子节点
    # 2."最后一层"存在子节点
    while current_layer:
        for current_node in current_layer:
            # 非底部时
            if not bottom_torched:
                if current_node.left and current_node.right:
                    next_layer.extend([current_node.left, current_node.right])
                elif current_node.left is None and current_node.right is None:
                    bottom_torched = True
                else:
                    return False
            # 底部时
            elif current_node.left or current_node.right:
                return False
        current_layer, next_layer = next_layer, []
    return result


def is_full_binary_tree_2(node=None):
    """
    满二叉树定义:
    第K层有2**(k-1)个元素

    :param node:
    :return:
    """
    # 逐层检查当前层与下一层
    current_layer = [node]
    next_layer = []
    k = 0
    while current_layer:
        for current_node in current_layer:
            next_layer.extend([current_node.left, current_node.right])
        k += 1
        if set(next_layer) == {None}:
            return True
        elif None in next_layer:
            return False
        elif len(next_layer) != 2 ** k:
            return False
        current_layer, next_layer = next_layer, []
    return True


def is_binary_sort_tree(node=None):
    """
    二叉排序树定义为：
    节点的左子树中的值要严格小于该节点的值。
    节点的右子树中的值要严格大于该节点的值。
    左右子树也必须是二叉查找树。
    一个节点的树也是二叉查找树。
    :param node:
    :return:
    """
    result = True
    if not node:
        return result
    if node.left:
        result = result and node.left.element < node.element
    if node.right:
        result = result and node.right.element > node.element
    return result and is_binary_sort_tree(node.left) and is_binary_sort_tree(node.right)


def is_balanced_tree(node=None):
    """
    平衡二叉树定义:
    TODO
    :param node:
    :return:
    """


def is_same_tree(node_a, node_b):
    """
    判断两棵树是否相同
    :param node_a:
    :param node_b:
    :return:
    """
    result = True
    # 当节点A,B存在
    if node_a and node_b:
        # 且不相等时,不等
        if node_a.element != node_b.element:
            return False
    # 当节点A,B仅存在一者,不等
    elif node_a or node_b:
        return False
    return result and is_same_tree(node_a.left, node_b.left) and is_same_tree(node_a.right, node_b.right)


def binary_tree_visualization(node=None):
    """
    二叉树可视化
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
    # 基础二叉树
    bbt = BaseBinaryTree()
    for i in range(15):
        # 逐层顺序插入
        bbt.insert(i)

    funcs = [layer_traversal_with_deep,
             max_depth, min_depth, nodes_count, leaf_nodes_count,
             is_complete_tree, is_full_binary_tree, is_full_binary_tree_2,
             is_binary_sort_tree]
    func_test(funcs, bbt.root)

    print(nodes_count_k_level.__name__, ":", nodes_count_k_level(bbt.root, 3))

    print("-" * 50)
    # 二叉搜索树

    bst = BinarySortTree()
    # elements = set([random.randrange(1, 100) for i in range(8)])
    elements = [59, 23, 55, 56, 25, 27, 30, 63]
    print(elements)
    for i in elements:
        bst.insert(i)

    func_test(funcs, bst.root)
