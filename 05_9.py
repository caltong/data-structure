class HuffmanTree():
    def __init__(self, element, weight, left, right, height):
        self.element = element
        self.weight = weight
        self.left = left
        self.right = right
        self.height = height


N = int(input())
input_list = input().split(' ')

elements = []
weights = {}
for i in range(N):
    key = input_list.pop(0)
    value = int(input_list.pop(0))
    elements.append(HuffmanTree(element=key, weight=value, left=None, right=None, height=1))
    weights[key] = value
while True:
    if len(elements) == 1:
        break
    elements.sort(key=lambda huffman_tree: huffman_tree.weight)
    first = elements.pop(0)
    second = elements.pop(0)
    build_tree = HuffmanTree(element=None, weight=first.weight + second.weight, left=first, right=second,
                             height=max(first.height, second.height) + 1)
    elements.append(build_tree)


def cal_sum(tree):
    if tree.element is None:
        return cal_sum(tree.left) + cal_sum(tree.right)
    else:
        return 
