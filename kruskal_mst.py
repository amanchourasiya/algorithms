from object_priority_queue import ObjectPriorityQueue 
from union_find import UnionFind

class KruskalMst():
    def __init__(self,weighted_graph):
        self.weighted_graph = weighted_graph
        self.pqueue = ObjectPriorityQueue()
        self.mst_length = len(weighted_graph.vertices) - 1
        self.current_mst_length = 0
        self.mst = []
        self.union = UnionFind(len(weighted_graph.vertices))
        self.edges = weighted_graph.get_edges()


    def fill_pq(self):
        for edge in self.edges:
            self.pqueue.enqueue(edge)

    def createMst(self):
        node = None
        while self.current_mst_length != self.mst_length:
            node = self.pqueue.peek()
            v = node.either()
            w = node.other(v)
            
            if len(self.union) != 0:
                if not self.union.check_union(v,w):
                    self.union.add_union(v,w)
                    self.mst.append(node)
                    self.current_mst_length +=1
            self.pqueue.dequeue()


        