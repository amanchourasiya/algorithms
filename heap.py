class Heap():
    def __init__(self):
        self.heap = []

    def get_parent(self,i):
        return (i-1) // 2
    
    def get_child(self,i):
        child = 2 * i + 1
        return (child,child+1)
    
    def insert(self,data):
        self.heap.append(data)
        if self.get_heap_size() == 1:
            return 

        data_index = self.get_heap_size() -1
        parent = self.get_parent(data_index)

        while True:
            if data_index == 0:
                break

            if self.heap[parent] < self.heap[data_index]:
                self.swap_values(parent,data_index)
                data_index = parent
                parent = self.get_parent(data_index)
            else:
                break

    def swap_values(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]

    
    def get_heap_size(self):
        return len(self.heap)

def test_heap():
    h = Heap()
    #h.heap 
    a = [5,7,9,1,3,4,5]
    for i in a:
        h.insert(i)
    print(h.heap)
    h.insert(1)
    print(h.heap)

test_heap()