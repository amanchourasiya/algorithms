class Stack():
    
    def __init__(self):
        self.linked_list = None
    
    def is_stack_empty(self):
        if self.linked_list is None:
            return True
        else:
            return False

    def pop(self):
        if not self.is_stack_empty():
            element = self.linked_list.peek_first_node()
            self.linked_list = self.linked_list.delete()
            return element


    def push(self,data):
        if self.linked_list is None:
            self.linked_list = self.Node(data)
        else:
            self.linked_list = self.linked_list.insert(self.Node(data))

    def peek(self):
        return self.linked_list.peek_first_node()
    
    class Node():
        def __init__(self,data):
            self.data = data
            self.next = None
        
        def insert(self,node):
            node.next = self
            return node
        
        def delete(self):
            node = self.next
            self = None
            return node
        
        def peek_first_node(self):
            return self.data


def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop(),s.pop(),s.pop())

test_stack()