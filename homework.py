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
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
    
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def delete(self, data):
        temp = self.head
        
        if temp and temp.data == data:
            self.haed = temp.next
            return
        
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        
        prev.next = temp.next

    def search(self,data):
        temp = self.haed
        while temp:
            if temp.data == data:
                return True
            temp = temp.next 
        return False
    
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def print_all(self):
        temp = self.head
        while temp:
            print(temp.data, end = " -> ")
            temp = temp.next
        print("None")