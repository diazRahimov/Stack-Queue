class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def print_all(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)

# ll.print_all()


# ============ QUEUE ============ #

from collections import deque

queue = deque()


queue.append(10)
queue.append(20)
queue.append(30)

print(queue.popleft())