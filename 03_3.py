N = int(input())
pre_order = []
in_order = []

tmp = []
for i in range(N * 2):
    str_data = input().split()
    if str_data[0] == 'Push':
        pre_order.append(int(str_data[1]))
        tmp.append(int(str_data[1]))
    elif str_data[0] == 'Pop':
        in_order.append(tmp[-1])
        tmp.remove(tmp[-1])


# print(pre_order)
# print(in_order)


class TreeNode:
    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


def build_tree(pre_o, s1, e1, in_o, s2, e2):
    if s1 > e1:
        return None
    index = in_o.index(pre_o[s1])
    root = TreeNode(pre_o[s1])
    root.left = build_tree(pre_o, s1 + 1, s1 + index - s2, in_o, s2, index - 1)
    root.right = build_tree(pre_o, s1 + index - s2 + 1, e1, in_o, index + 1, e2)
    return root


root = build_tree(pre_order, 0, N - 1, in_order, 0, N - 1)

# print(root)
output = []


def print_post_order(tree):
    if tree.left is not None:
        print_post_order(tree.left)
    if tree.right is not None:
        print_post_order(tree.right)

    output.append(tree.element)


print_post_order(root)
for i in output[:-1]:
    print(i, end=' ')
print(output[-1], end='')
