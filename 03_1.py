def build_one_tree():
    tree_height = int(input())
    tree = []
    for i in range(tree_height):
        str_data = input().split()
        node = [str_data[0]]
        for item in str_data[1:]:
            if item is not '-':
                node.append(int(item))
            else:
                node.append(None)
        tree.append(node)
    root = list(range(tree_height))
    for node in tree:
        for child in node[1:]:
            if child is not None:
                root.remove(child)
    if len(root) != 0:
        root = root[0]
    else:
        root = None
    return tree, root


# 把tree存在list中
tree1, tree1_root = build_one_tree()
tree2, tree2_root = build_one_tree()


# print(tree1_root, tree1)
# print(tree2_root, tree2)


class BinaryTreeNode:
    def __init__(self, element, left, right):
        self.element = element
        self.left = left
        self.right = right

    def get_element(self):
        return self.element

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right


# 把list每个元素转换成BinaryTreeNode类
for i in range(len(tree1)):
    tree1[i] = BinaryTreeNode(tree1[i][0], tree1[i][1], tree1[i][2])
for i in range(len(tree2)):
    tree2[i] = BinaryTreeNode(tree2[i][0], tree2[i][1], tree2[i][2])
# print(tree1_root, tree1)
# print(tree2_root, tree2)

if len(tree1) != 0:
    root1 = tree1[tree1_root]
else:
    root1 = None
if len(tree2) != 0:
    root2 = tree2[tree2_root]
else:
    root2 = None

# 把每一个BinaryTreeNode链接起来
for node in tree1:
    if node.left is not None:
        node.left = tree1[node.left]
    if node.right is not None:
        node.right = tree1[node.right]
for node in tree2:
    if node.left is not None:
        node.left = tree2[node.left]
    if node.right is not None:
        node.right = tree2[node.right]


def isomorphic(root1, root2):
    # 都为空
    if (root1 is None) and (root2 is None):
        return 1

    # 一个为空一个不为空
    if ((root1 is None) and (root2 is not None)) or ((root1 is not None) and (root2 is None)):
        return 0

    # 根节点不相同
    if root1.get_element() != root2.get_element():
        return 0

    # 都没有左子树 则判断右子树
    if (root1.get_left() is None) and (root2.get_left() is None):
        return isomorphic(root1.get_right(), root2.get_right())

    # 左子节点element相等 则判断左子树和右子树
    if ((root1.get_left() is not None) and (root2.get_left() is not None)) and (
            root1.get_left().get_element() == root2.get_left().get_element()):
        return isomorphic(root1.get_left(), root2.get_left()) and isomorphic(root1.get_right(), root2.get_right())

    # 判断左右互换
    else:

        return isomorphic(root1.get_left(), root2.get_right()) and isomorphic(root1.get_right(), root2.get_left())


if isomorphic(root1, root2):
    print('Yes')
else:
    print('No')
