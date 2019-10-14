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
        while current.next is not None:
            res.append(current.get_data)
            current = current.next
        return res
