class queue:
    def __init__(self):
        self.items = []
    
    def __repr__(self):
        return f'queue object: data={self.items}'
    
    def is_empty(self):
        return not self.items
    
    def enqueue(self, item):
        self.items.append(item)  # Corrected to append the item
    
    def dequeue(self):
        return self.items.pop(0)  # Added the dequeue method
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0] if self.items else None  # Added check for empty queue
    
if __name__ == '__main__':  # Corrected the if statement
    q = queue()
    print(q.is_empty())  # Corrected the method call
    q.enqueue('first')
    q.enqueue('second')

    print(q)
    print(q.dequeue())
    print(q)
    print(q.size())
    print(q.peek())
