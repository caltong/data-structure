def get_input():
    input_str = input()
    input_str = input_str.split(' ')
    return input_str


def get_root(heap, x):
    if heap[x] < 0:
        return x
    else:
        return get_root(heap, heap[x])


def get_root_with_path_compression(heap, x):
    root = get_root(heap, x)
    if heap[root] > 0:
        heap[root] = root
    return root


def union(heap, root1, root2):
    # 按秩归并 比规模
    if heap[root2] < heap[root1]:
        heap[root2] += heap[root1]
        heap[root1] = root2
    else:
        heap[root1] += heap[root2]
        heap[root2] = root1


N = int(get_input()[0])
heap = [-1] * N
while True:
    input_str = get_input()
    if input_str[0] == 'I':
        root1 = get_root_with_path_compression(heap, int(input_str[1]) - 1)
        root2 = get_root_with_path_compression(heap, int(input_str[2]) - 1)
        union(heap, root1, root2)
    if input_str[0] == 'C':
        root1 = get_root_with_path_compression(heap, int(input_str[1]) - 1)
        root2 = get_root_with_path_compression(heap, int(input_str[2]) - 1)
        if root1 == root2:
            print('yes')
        else:
            print('no')
    if input_str[0] == 'S':
        components = 0
        for i in heap:
            if i < 0:
                components += 1
        if components == 1:
            print('The network is connected.')
        else:
            print('There are {} components.'.format(components))
        break
