first = input()
second = input()
first = first.split()
first = list(map(int, first))
second = second.split()
second = list(map(int, second))

first_counter = 1
second_counter = 1
result = []
while True:
    if first[first_counter + 1] < second[second_counter + 1]:
        result.append(second[second_counter])
        result.append(second[second_counter + 1])
        second_counter = second_counter + 2
    elif first[first_counter + 1] == second[second_counter + 1]:
        result.append(first[first_counter] + second[second_counter])
        result.append(first[first_counter + 1])
        first_counter = first_counter + 2
        second_counter = second_counter + 2
    elif first[first_counter + 1] > second[second_counter + 1]:
        result.append(first[first_counter])
        result.append(first[first_counter + 1])
        first_counter = first_counter + 2

    if first_counter == first[0] and second_counter == second[0]:
        break
print(result)
