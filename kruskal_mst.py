from object_priority_queue import ObjectPriorityQueue 
from union_find import UnionFind
from weighted_graph import WeightedGraph, Edge

class KruskalMst():
    def __init__(self,weighted_graph):
        self.weighted_graph = weighted_graph
        self.pqueue = ObjectPriorityQueue()
        self.mst_length = len(weighted_graph.vertices) - 1
        self.current_mst_length = 0
        self.mst = []
        self.union = UnionFind(len(weighted_graph.vertices))
        self.edges = weighted_graph.get_edges()
        self.fill_pq()
        self.createMst()


    def fill_pq(self):
        for edge in self.edges:
            self.pqueue.enqueue(edge)

    def createMst(self):
        node = None
        while self.current_mst_length != self.mst_length or self.pqueue.is_empty():
            node = self.pqueue.peek()
            v = node.either()
            w = node.other(v)
            
            
            if not self.union.check_union(v,w):
                self.union.add_union(v,w)
                self.mst.append(node)
                self.current_mst_length +=1
            self.pqueue.dequeue()
        
    def get_mst(self):
        for edge in self.mst:
            print(edge.v,edge.w,edge.weight)
            

def test_kruskal():
    w_graph = WeightedGraph(4)
    w_graph.add_edge(1,0,-10)
    w_graph.add_edge(1,2,-35)
    w_graph.add_edge(0,2,-15)
    w_graph.add_edge(0,3,-12)
    w_graph.add_edge(1,3,-11)
    w_graph.add_edge(2,3,-30)
    '''
    w_graph.add_edge(4,6,-1)
    w_graph.add_edge(3,8,-2)
    w_graph.add_edge(8,7,-5)
    w_graph.add_edge(6,8,-8)
    w_graph.add_edge(7,6,-17)
    '''

    k = KruskalMst(w_graph)
    k.get_mst()
    '''
    s = w_graph.get_edges()
    pq = ObjectPriorityQueue()
    for s1 in s:
        pq.enqueue(s1)
    while True:
        a = pq.dequeue()
        if a is None:
            break
        print(a.v,a.w,a.weight)
    '''

test_kruskal()
    


        