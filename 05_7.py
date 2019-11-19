from math import log


def get_parent_index(child_index):
    # if 父节点index = i
    #     left index = 2i
    #     right index = 2i + 1
    if child_index % 2 == 1:
        return int((child_index - 1) / 2)
    elif child_index % 2 == 0:
        return int(child_index / 2)


input_str = input()
input_str = input_str.split(' ')
input_list = list(map(int, input_str))
N = input_list[0]
M = input_list[1]
input_str = input()
input_str = input_str.split(' ')
input_list = list(map(int, input_str))
a = input_list
input_str = input()
input_str = input_str.split(' ')
input_list = list(map(int, input_str))
b = input_list

heap = [None]  # None代表头 以便index从1开始计算
for i in range(N):
    heap.append(a.pop(0))
    index = len(heap) - 1
    while index != 1:  # 当判断根节点的时候退出循环
        parent = get_parent_index(index)
        if heap[parent] > heap[index]:
            tmp = heap[parent]
            heap[parent] = heap[index]
            heap[index] = tmp
        index = get_parent_index(index)

for i in b:
    index = i
    while index:  # index为1时 下一次index为0 正好退出循环
        # if else 为了隔空格输出 并且结尾没有空格
        if index != 1:
            print(heap[index], end=' ')
        else:
            print(heap[index])
        index = get_parent_index(index)
