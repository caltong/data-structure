class HuffmanTree():
    def __init__(self, element, weight, left, right):
        self.element = element
        self.weight = weight
        self.left = left
        self.right = right


N = int(input())
input_list = input().split(' ')

for i in range(N):
    