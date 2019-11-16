list_len = input()
list_len = int(list_len)
list_data = input()
list_data = list_data.split(' ')
list_data = list(map(int, list_data))

max_sum = 0
this_sum = 0
left = 0
temp_left = 0
right = list_len - 1
for i in range(list_len):
    this_sum = this_sum + list_data[i]
    if this_sum > max_sum:
        max_sum = this_sum
        left = temp_left
        right = i
    elif this_sum < 0:
        this_sum = 0
        temp_left = i + 1
    elif this_sum == 0 and max_sum == 0:
        left = temp_left
        right = i

print(max_sum, list_data[left], list_data[right])
