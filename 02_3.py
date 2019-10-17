# 获取输入
def get_input_line():
    line = input().split()
    line = list(map(int, line))
    return line


# 获取第一行信息
first_line = get_input_line()
first_item_address = first_line[0]
length = first_line[1]
K = first_line[2]

# 用字典存储信息
d = {}
for i in range(length):
    line = get_input_line()
    d[line[0]] = line[1:]
# print(d)
# 顺序
p = first_item_address
data_dict = {}
while p != -1:
    data_dict[p] = d[p]
    p = d[p][1]
    # print(p)
# print('data_dict: ', data_dict, '\n' + 'K: ', K)

# 根据要求逆序字典keys
tmp = []
reverse_keys = []
counter = 0
for key in data_dict.keys():
    tmp.append(key)
    counter = counter + 1
    if counter == K:
        tmp.reverse()
        reverse_keys = reverse_keys + tmp
        tmp = []
        counter = 0
reverse_keys = reverse_keys + tmp

# 输出
counter = 1
for key in reverse_keys[:-1]:
    print(str(key).zfill(5), data_dict[key][0], str(reverse_keys[counter]).zfill(5))
    counter = counter + 1
print(str(reverse_keys[-1]).zfill(5), data_dict[reverse_keys[-1]][0], '-1')
