def build_one_tree():
    tree_node_number = int(input())
    tree = []
    for i in range(tree_node_number):
        str_data = input().split()
        node = [i]
        for item in str_data:
            if item is not '-':
                node.append(int(item))
            else:
                node.append(None)
        tree.append(node)
    root = list(range(tree_node_number))
    for node in tree:
        for child in node[1:]:
            if child is not None:
                root.remove(child)
    if len(root) != 0:
        root = root[0]
    else:
        root = None
    return tree, root


tree, root = build_one_tree()
# print(root, tree)
queue = [tree[root]]
output = []
while len(queue) != 0:
    element = queue[0][0]
    left = queue[0][1]
    right = queue[0][2]
    queue.remove(queue[0])
    if (left is None) and (right is None):
        output.append(element)
    if left is not None:
        queue.append(tree[left])
    if right is not None:
        queue.append(tree[right])

for i in output[:-1]:
    print(i, end=' ')
print(output[-1])
