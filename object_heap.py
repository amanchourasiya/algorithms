import copy
import linked_list


'''
Implementation of a heap that can work on any object if that object has compare_to() method implemented
'''

class MaxObjectHeap():
    def __init__(self):
        self.heap = []

    def get_parent(self,i):
        return (i-1) // 2
    
    def is_leaf(self,i):
        c1,_ = self.get_child(i)
        if c1 >= self.get_heap_size():
            return True
        else:
            return False
    
    def is_empty(self):
        if len(self.heap) == 0:
            return True
        else:
            False


    def has_one_child(self,i):
        if not self.is_leaf(i):
            _,c2 = self.get_child(i)
            if c2 >= self.get_heap_size():
                return True
            else:
                return False
        else:
            return False


    def get_child(self,i):
        child = 2 * i + 1
        return (child,child+1)
    
    def push(self,node):
        self.heap.append(node)
        if self.get_heap_size() == 1:
            return 

        data_index = self.get_heap_size() -1
        parent_index = self.get_parent(data_index)

        while True:
            if data_index == 0:
                break

            if self.heap[parent_index].compare_to(self.heap[data_index]) == -1:
                self.swap_values(parent_index,data_index)
                data_index = parent_index
                parent_index = self.get_parent(data_index)
            else:
                break
    
    def pop(self):
        if len(self.heap) == 0:
            return None

        ret = copy.deepcopy(self.heap[0])
        self.heap[0] = copy.deepcopy(self.heap[-1])
        del(self.heap[-1])

        # Checking whether new root node is at correct place othersise put it at correct place
        
        parent_index = 0
        child1_index, child2_index = self.get_child(parent_index)
        if self.is_leaf(parent_index):
            return ret
        if self.has_one_child(parent_index):
            if self.heap[parent_index].compare_to(self.heap[child1_index]) > 0:
                return ret
            else:
                self.swap_values(parent_index,child1_index)
                return ret
        #print(parent_index,child1_index,child2_index)

        while (self.heap[parent_index].compare_to(self.heap[child1_index]) == -1) or (self.heap[parent_index].compare_to(self.heap[child2_index]) == -1):
            # It means that parent is smaller that one or more child , so we will repeat
            if self.heap[child1_index].compare_to(self.heap[child2_index]) > 0:
                #print('child1 is bigger')
                self.swap_values(parent_index,child1_index)
                parent_index = child1_index
            else:
                #print('chile2 is bigger')
                self.swap_values(parent_index,child2_index)
                parent_index = child2_index
            
            # If we have reached the leaf there is no possibility of swapping so we will exit
            if self.is_leaf(parent_index):
                break

            child1_index,child2_index = self.get_child(parent_index)
            #print(child1_index,child2_index)
             
            # If there is only one child then there is only one possibility of swapping and 
            # no further swapping will be possible

            if self.has_one_child(parent_index):
                if self.heap[parent_index].compare_to(self.heap[child1_index]) > 0:
                    break
                else:
                    self.swap_values(parent_index,child1_index)
                    break
        
        return ret
        
    def swap_values(self,i,j):
        #print(self.heap[i].data,self.heap[j].data)
        tmp = copy.deepcopy(self.heap[i])
        self.heap[i] = copy.deepcopy(self.heap[j])
        self.heap[j] = tmp

    def get_heap_size(self):
        return len(self.heap)
    
    def peek(self):
        return self.heap[0]


class MinObjectHeap():
    def __init__(self):
        self.heap = []

    def get_parent(self,i):
        return (i-1) // 2
    
    def is_leaf(self,i):
        c1,_ = self.get_child(i)
        if c1 >= self.get_heap_size():
            return True
        else:
            return False
    
    def is_empty(self):
        if len(self.heap) == 0:
            return True
        else:
            False


    def has_one_child(self,i):
        if not self.is_leaf(i):
            _,c2 = self.get_child(i)
            if c2 >= self.get_heap_size():
                return True
            else:
                return False
        else:
            return False


    def get_child(self,i):
        child = 2 * i + 1
        return (child,child+1)
    
    def push(self,node):
        self.heap.append(node)
        if self.get_heap_size() == 1:
            return 

        data_index = self.get_heap_size() -1
        parent_index = self.get_parent(data_index)

        while True:
            if data_index == 0:
                break

            if self.heap[parent_index].compare_to(self.heap[data_index]) == 1:
                self.swap_values(parent_index,data_index)
                data_index = parent_index
                parent_index = self.get_parent(data_index)
            else:
                break
    
    def pop(self):
        if len(self.heap) == 0:
            return None

        ret = copy.deepcopy(self.heap[0])
        self.heap[0] = copy.deepcopy(self.heap[-1])
        del(self.heap[-1])

        # Checking whether new root node is at correct place othersise put it at correct place
        
        parent_index = 0
        child1_index, child2_index = self.get_child(parent_index)
        if self.is_leaf(parent_index):
            return ret
        if self.has_one_child(parent_index):
            if self.heap[parent_index].compare_to(self.heap[child1_index]) < 0:
                return ret
            else:
                self.swap_values(parent_index,child1_index)
                return ret
        #print(parent_index,child1_index,child2_index)

        while (self.heap[parent_index].compare_to(self.heap[child1_index]) == 1) or (self.heap[parent_index].compare_to(self.heap[child2_index]) == 1):
            # It means that parent is smaller that one or more child , so we will repeat
            if self.heap[child1_index].compare_to(self.heap[child2_index]) < 0:
                #print('child1 is bigger')
                self.swap_values(parent_index,child1_index)
                parent_index = child1_index
            else:
                #print('chile2 is bigger')
                self.swap_values(parent_index,child2_index)
                parent_index = child2_index
            
            # If we have reached the leaf there is no possibility of swapping so we will exit
            if self.is_leaf(parent_index):
                break

            child1_index,child2_index = self.get_child(parent_index)
            #print(child1_index,child2_index)
             
            # If there is only one child then there is only one possibility of swapping and 
            # no further swapping will be possible

            if self.has_one_child(parent_index):
                if self.heap[parent_index].compare_to(self.heap[child1_index]) < 0:
                    break
                else:
                    self.swap_values(parent_index,child1_index)
                    break
        
        return ret
        
    def swap_values(self,i,j):
        #print(self.heap[i].data,self.heap[j].data)
        tmp = copy.deepcopy(self.heap[i])
        self.heap[i] = copy.deepcopy(self.heap[j])
        self.heap[j] = tmp

    def get_heap_size(self):
        return len(self.heap)
    
    def peek(self):
        return self.heap[0]




def traverse_heap(heap):
    print('traversed heap',len(heap))
    for i in heap:
        print(i.data)


def test_heap():
    h = MinObjectHeap()
    #h.heap 
    a = [5,7,9,1,3,4,50,-1]
    for i in a:
        x = linked_list.Node(i)
        h.push(x)
    print(h.heap)
    traverse_heap(h.heap)   
    h.pop()
    traverse_heap(h.heap)
    h.pop()
    traverse_heap(h.heap)
    #h.insert(1)
    #print(h.heap)

test_heap()
