list_len = input()
list_len = int(list_len)
list_data = input()
list_data = list_data.split(' ')
list_data = list(map(int, list_data))

max_sum = 0
this_sum = 0
this_list = []
for i in range(list_len):
    this_sum = this_sum + list_data[i]
    if this_sum > max_sum:
        max_sum = this_sum
    elif this_sum < 0:
        this_sum = 0

print(max_sum, first, last)
