class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return -1
        
    def push(self,item):
        self.items.append(item)
    
            

def solution(arr):
    stack = Stack()
    
    for n in arr:
        if n != stack.peek():
            stack.push(n)
    
    return stack.items