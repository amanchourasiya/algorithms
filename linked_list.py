'''
Creating a node of list
'''
class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

    def insert(self,data):
        node = Node(data)
        node.next = self
        return node

    def traverse_list(self):
        tmp = self
        while tmp is not None:
            print(tmp.data)
            tmp = tmp.next
    
    def count_elements(self):
        tmp = self
        count = 0
        while tmp is not None:
            count+=1
            tmp = tmp.next
        return count

    def compare_to(self,node):
        if self.data < node.data:
            return -1
        elif self.data > node.data:
            return 1
        else:
            return 0