# arr = [10,25,42,7,3,43,99,53,5]

# sorted_arr = sorted(arr)
# print(sorted_arr)

# O(n)

# def linear_search(target):
#     for item in arr:
#         if item == target:
#             return arr.index(item)
        
#     return -1 

# print(linear_search(242))




# def binary_search(target):
#     left = 0
#     right = len(sorted_arr) - 1
    
#     while left <= right:
#         midd = (left + right) // 2
        
#         if target == sorted_arr[midd]:
#             return midd
        
#         elif target > sorted_arr[midd]:
#             left = midd + 1
        
#         elif target < sorted_arr[midd]:
#             right = midd - 1
            
#     return - 1


# print(binary_search(5))

# O(log2N)


# Stack => LIFO => Last In First Out => (Telegram messsangers) => Web
# Queue => FIFO => First In First Out


class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,new_item):
        self.stack.append(new_item)
    
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
            return
        return -1
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        return self.stack[-1]
        
# my_stack = Stack()

# # print(my_stack.is_empty())

# my_stack.push(10)
# my_stack.push(20)
# my_stack.push(30)

# print(my_stack.is_empty())

# print(my_stack.peek())

# my_stack.pop()

# # print(my_stack.peek())
# print(my_stack.size())
