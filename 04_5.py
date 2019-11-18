class AVLTree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None


def get_height(tree):
    # 通过遍历所有节点 获取树高
    if tree is None:
        return 0
    else:
        return max(get_height(tree.left), get_height(tree.right)) + 1


def single_left_rotation(tree0):
    # tree0 为旋转前的树, tree1 旋转后的树
    tree1 = tree0.left
    tree0.left = tree1.right
    tree1.right = tree0
    return tree1


def single_right_rotation(tree0):
    tree1 = tree0.right
    tree0.right = tree1.left
    tree1.left = tree0
    return tree1


def double_left_right_rotation(tree):
    tree.left = single_right_rotation(tree.left)
    return single_left_rotation(tree)


def double_right_left_rotation(tree):
    tree.right = single_left_rotation(tree.right)
    return single_right_rotation(tree)


def insert_avl_tree(tree, element):
    # 如果子树为空 则插入该位置
    if tree is None:
        tree = AVLTree(element)
    elif element < tree.root:
        tree.left = insert_avl_tree(tree.left, element)
        # 判断单左旋还是左右旋转
        if get_height(tree.left) - get_height(tree.right) == 2:
            if element < tree.left.root:
                tree = single_left_rotation(tree)
            else:
                tree = double_left_right_rotation(tree)
    elif element > tree.root:
        # 判断单右旋还是右左旋
        tree.right = insert_avl_tree(tree.right, element)
        if get_height(tree.left) - get_height(tree.right) == -2:
            if element > tree.right.root:
                tree = single_right_rotation(tree)
            else:
                tree = double_right_left_rotation(tree)
    return tree


N = int(input())
input_str = input()
input_str = input_str.split(' ')
input_list = list(map(int, input_str))
tree = AVLTree(input_list[0])  # 建立第一个树
for i in input_list[1:]:  # 遍历插入后面的树
    tree = insert_avl_tree(tree, i)
print(tree.root)
