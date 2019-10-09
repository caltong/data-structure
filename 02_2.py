first = input()
second = input()
first = first.split()
first = list(map(int, first))
second = second.split()
second = list(map(int, second))

# todo
# for i in range(first[0]):
#     for j in range(second[0]):
#
for i in range(first[0]):
    for j in range(second[0]):
        temp_result = [first[2*i+1]*second[2*j+1],first[2*i+2]*second[2*j+2]]
        
first.append(0)
first.append(0)
second.append(0)
second.append(0)
first_counter = 1
second_counter = 1
result_add = []
while True:
    if first[first_counter + 1] < second[second_counter + 1]:
        result_add.append(second[second_counter])
        result_add.append(second[second_counter + 1])
        second_counter = second_counter + 2

    elif first[first_counter + 1] == second[second_counter + 1]:
        result_add.append(first[first_counter] + second[second_counter])
        result_add.append(first[first_counter + 1])
        first_counter = first_counter + 2
        second_counter = second_counter + 2

    elif first[first_counter + 1] > second[second_counter + 1]:
        result_add.append(first[first_counter])
        result_add.append(first[first_counter + 1])
        first_counter = first_counter + 2

    if first_counter >= 2 * first[0] and second_counter >= 2 * second[0]:
        break
print(result_add)
