import heapq

class NewPriorityQueue:
    def __init__(self, nodes):
        self.nodes = nodes
        heapq.heapify(self.nodes)

    def push(self, node):
        heapq.heappush(self.nodes, node)

    def pop(self):
        return heapq.heappop(self.nodes)
    
    def decreasekey(self, key, value):
        for i in range(len(self.nodes)):
            if self.nodes[i][0] == key:
                self.nodes[i] = (key, value)
    
    def contains(self, nodekey):
        for node in self.nodes:
            if node[0] == nodekey:
                return True
        return False

