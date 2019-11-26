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

huffman_code = []


def generate_huffman_code(tree, code=None):
    if code is None:
        code = []
    if tree.element is None:
        return generate_huffman_code(tree.left, code + [0]), generate_huffman_code(tree.right, code + [1])
    elif tree.element is not None:
        return huffman_code.append((tree.element, code))


generate_huffman_code(elements[0])


def cal_weights_sum(huffman_code):
    sum = 0
    for i in huffman_code:
        weight = weights[i[0]]
        length = len(i[1])
        sum += weight * length
    return sum


standard = cal_weights_sum(huffman_code)


def is_prefix_code(huffman_code):
    huffman_code.sort(key=lambda a: len(a[1]))
    for i in range(len(huffman_code)):
        for j in huffman_code[i + 1:]:
            if huffman_code[i][1] == j[1][:len(huffman_code[i][1])]:
                return False
    return True


M = int(input())
for i in range(M):
    student_huffman_code = []
    for i in range(N):
        input_str = input().split(' ')
        key = input_str[0]
        code = input_str[1]
        student_huffman_code.append((key, code))
    if (cal_weights_sum(student_huffman_code) == standard) and (is_prefix_code(student_huffman_code)):
        print('Yes')
    else:
        print('No')
