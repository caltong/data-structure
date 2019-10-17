# 获取输入
def get_input_line():
    line = input().split()
    line = list(map(int, line))
    return line


# 获取第一行信息
first_line = get_input_line()
first_item_address = first_line[0]
length = first_line[1]
reverse_key = first_line[2]

# 用字典存储信息
d = {}
for i in range(length):
    line = get_input_line()
    d[line[0]] = line[1:]
# print(d)

# 顺序字典
p = first_item_address
data_dict = {}
while p != -1:
    data_dict[p] = d[p]
    p = d[p][1]
    # print(p)
# print('data_dict: ', data_dict, '\n' + 'reverse_key: ', reverse_key)

# 根据要求逆序字典keys
tmp = []
reverse_keys = []
counter = 0
for key in data_dict.keys():
    tmp.append(key)
    counter = counter + 1
    if counter == reverse_key:
        tmp.reverse()
        reverse_keys = reverse_keys + tmp
        tmp = []
        counter = 0
reverse_keys = reverse_keys + tmp

# 上移一位获取next
next_address = list(map(str, reverse_keys[1:])) + ['-1']
for i in range(len(next_address) - 1):
    next_address[i] = next_address[i].zfill(5)

# 拼接key data next
counter = 0
reverse_data_dict = {}
for key in reverse_keys:
    reverse_data_dict[key] = [data_dict[key][0], next_address[counter]]
    counter = counter + 1

# 输出
for key in reverse_data_dict.keys():
    print(str(key).zfill(5), reverse_data_dict[key][0], reverse_data_dict[key][1])
