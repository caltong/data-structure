from math import log


def get_root(tree_list):
    if len(tree_list) == 1:
        return 0
    else:
        # n为节点数 k为层数
        n = len(tree_list)
        k = int(log(n + 1, 2)) + 1
        s1 = pow(2, k - 2) - 1
        s2 = min(n - pow(2, k - 1) + 1, pow(2, k - 2))
        return int(s1 + s2)


N = int(input())
input_str = input()
input_str = input_str.split(' ')
input_list = list(map(int, input_str))
input_list.sort()
result = []
tmp = [input_list]
while len(tmp) != 0:
    sub_list = []
    for i in tmp:
        root = get_root(i)
        result.append(i[root])
        if i[:root]:
            sub_list.append(i[:root])
        if i[root + 1:]:
            sub_list.append(i[root + 1:])
    tmp = sub_list

for i in result[:-1]:
    print(i, end=' ')
print(result[-1])
