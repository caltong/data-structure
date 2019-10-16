first = input()
second = input()
first = first.split()
first = list(map(int, first))
second = second.split()
second = list(map(int, second))


class Node:
    def __init__(self, coef, exp):
        self.coef = coef
        self.exp = exp
        self.next = None

    def get_data(self):
        return [self.coef, self.exp]


class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_node(self, node):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node

    def print_link(self):
        res = []
        current = self.head
        res.append(current.get_data())
        while current.next is not None:
            current = current.next
            res.append(current.get_data())
        return res


def add(l1, l2):
    p1 = l1.head
    p2 = l2.head
    add_res = []
    while (p1 is not None) and (p2 is not None):
        tmp_exp1 = p1.get_data()[1]
        tmp_exp2 = p2.get_data()[1]
        if tmp_exp1 < tmp_exp2:
            add_res.append([p2.get_data()[0], p2.get_data()[1]])
            p2 = p2.next
        elif tmp_exp1 == tmp_exp2:
            add_res.append([p1.get_data()[0] + p2.get_data()[0], p1.get_data()[1]])
            p1 = p1.next
            p2 = p2.next
        elif tmp_exp1 > tmp_exp2:
            add_res.append([p1.get_data()[0], p1.get_data()[1]])
            p1 = p1.next
    while p1 is not None:
        add_res.append([p1.get_data()[0], p1.get_data()[1]])
        p1 = p1.next
    while p2 is not None:
        add_res.append([p2.get_data()[0], p2.get_data()[1]])
        p2 = p2.next

    res = []
    for item in add_res:
        if item[0] != 0:
            res.append(item[0])
            res.append(item[1])
    if len(res) == 0:
        res = [0, 0]
    return res


def multiply(l1, l2):
    p1 = l1.head
    p2 = l2.head
    multiply_res = []
    while p1 is not None:
        tmp1 = p1.get_data()
        while p2 is not None:
            tmp2 = p2.get_data()
            multiply_res.append([tmp1[0] * tmp2[0], tmp1[1] + tmp2[1]])
            p2 = p2.next
        p2 = l2.head
        p1 = p1.next

    exps = []
    for i in multiply_res:
        if i[1] not in exps:
            exps.append(i[1])

    d = {}
    for i in multiply_res:
        if i[1] not in d.keys():
            d[i[1]] = 0
        d[i[1]] = d[i[1]] + i[0]

    res = []
    keys = sorted(d)
    keys.reverse()
    for key in keys:
        if d[key] != 0:
            res.append(d[key])
            res.append(key)

    if len(res) == 0:
        res = [0, 0]

    return res


def print_list(l):
    for i in l[:-1]:
        print(i, end=' ')
    print(l[-1])


if first[0] != 0:
    head = Node(first[1], first[2])
    l1 = LinkedList(head)
    if first[0] > 1:
        for i in range(first[0] - 1):
            node = Node(first[i * 2 + 3], first[i * 2 + 4])
            l1.add_node(node)

if second[0] != 0:
    head = Node(second[1], second[2])
    l2 = LinkedList(head)
    if second[0] > 1:
        for i in range(second[0] - 1):
            node = Node(second[i * 2 + 3], second[i * 2 + 4])
            l2.add_node(node)

if len(first) == 1 and len(second) == 1:
    print_list([0, 0])
    print_list([0, 0])
elif len(first) == 1 and len(second) > 1:
    print_list([0, 0])
    print_list(second[1:])
elif len(first) > 1 and len(second) == 1:
    print_list([0, 0])
    print_list(first[1:])
else:
    print_list(multiply(l1, l2))
    print_list(add(l1, l2))
