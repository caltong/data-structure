# 获取输入
def get_input_line():
    get_line = input().split()
    get_line = list(map(int, get_line))
    return get_line


first_line = get_input_line()
M = first_line[0]
N = first_line[1]
K = first_line[2]

data_list = []
for i in range(K):
    line = get_input_line()
    data_list.append(line)

print(M, N, K)
print(data_list)


def judge(data_line):
    data = list(range(1, N + 1))
    data.reverse()
    stack = []
    tmp_max = 0
    for index in range(len(data_line)):
        if data_line[index] > tmp_max:
            for j in range(data_line[index] - tmp_max):
                stack.append(data.pop())
                if len(stack) > M:
                    return 'NO'
            tmp_max = data_line[index]
            stack.pop()
        elif data_line[index] < tmp_max:
            if stack.pop() != data_line[index]:
                return 'NO'
    return 'YES'


for i in range(K):
    print(judge(data_list[i]))
