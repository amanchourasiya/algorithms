from  object_heap import MaxObjectHeap, traverse_heap
import linked_list

'''
This priority is based on the idea of PriorityQueue in java in which it is mandatory 
that priority queue elements should be comparator objects.

Similarly this queue will work only of the elements stored have compare_to method implemented 
and this method should comapare and return smaller element

compare_to(a,b) method should return following values
if a < b : return -1
if a > b : return 1
if a == b: return 0
'''


class ObjectPriorityQueue():
    def __init__(self):
        self.heap = MinObjectHeap()

    def enqueue(self,node):
        self.heap.push(node)

    
    def dequeue(self):
        return self.heap.pop()

    def peek(self):
        return self.heap.peek()
    
    def is_empty(self):
        return self.heap.is_empty()


def object_priority_queue_test():
    queue = ObjectPriorityQueue()

    a = [4,8,9,2,4,88,23,22]
    for i in a:
        queue.enqueue(linked_list.Node(i))
    
    for i in range(len(a) -1 ):
        print(traverse_heap(queue.heap.heap))
        print(queue.dequeue().data)

#object_priority_queue_test()