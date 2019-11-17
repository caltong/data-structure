class BinarySearchTree:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right


def insert_binary_search_tree(tree, element):
    if tree.root is None:
        tree.root = element
        tree.left = BinarySearchTree(None, None, None)
        tree.right = BinarySearchTree(None, None, None)
    elif element < tree.root:
        return insert_binary_search_tree(tree.left, element)
    elif element > tree.root:
        return insert_binary_search_tree(tree.right, element)


def is_same_binary_search_tree(tree_a, tree_b):
    if (tree_a is None) and (tree_b is None):
        return True
    elif tree_a.root != tree_b.root:
        return False
    elif tree_a.root == tree_b.root:
        return (is_same_binary_search_tree(tree_a.left, tree_b.left) and
                is_same_binary_search_tree(tree_a.right, tree_b.right))


while True:
    input_str = input()
    input_str = input_str.split(' ')
    input_list = list(map(int, input_str))
    if input_list[0] == 0:
        break
    N = input_list[0]
    L = input_list[1]
    input_str = input()
    input_str = input_str.split(' ')
    input_list = list(map(int, input_str))
    tree0 = BinarySearchTree(None, None, None)
    for i in input_list:
        insert_binary_search_tree(tree0, i)
    for i in range(L):
        input_str = input()
        input_str = input_str.split(' ')
        input_list = list(map(int, input_str))
        tree1 = BinarySearchTree(None, None, None)
        for j in input_list:
            insert_binary_search_tree(tree1, j)
        if is_same_binary_search_tree(tree0, tree1):
            print('Yes')
        else:
            print('No')
