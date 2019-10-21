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
    root = root[0]
    return tree, root


tree1, tree1_root = build_one_tree()
tree2, tree2_root = build_one_tree()
print(tree1_root, tree1)
print(tree2_root, tree2)


def isomorphism():
    if (tree1_root == 0) and (tree2_root == 0):
        return 'YES'
    if ((tree1_root == 0) and (tree2_root != 0)) or ((tree1_root != 0) and (tree2_root == 0)):
        return "NO"
