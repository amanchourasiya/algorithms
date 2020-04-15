from weighted_graph import WeightedGraph
from object_priority_queue import ObjectPriorityQueue

class PrimsLazyMst():
    def __init__(self,weighted_graph):
        self.weighted_graph = weighted_graph
        self.pqueue = ObjectPriorityQueue()
        self.is_vertex_added = [False] * len(self.weighted_graph.vertices)
        self.mst = []
        self.mst_length = len(self.weighted_graph.vertices) -1
        self.current_mst_length = 0
        self.create_mst()
    
    def add_edges_to_pq(self,v):
        for edge in self.weighted_graph.get_edges(v):
            self.pqueue.enqueue(edge)
    
    def create_mst(self):
        self.add_edges_to_pq(0)
        self.is_vertex_added[0] = True
        while self.current_mst_length != self.mst_length or self.pqueue.is_empty():
            edge = self.pqueue.dequeue()
            v = edge.either()
            w = edge.other(v)

            # If both the vertices are already added in MST then we will skip this edge
            if self.is_vertex_added[v] and self.is_vertex_added[w]:
                continue

            self.mst.append(edge)
            self.current_mst_length +=1
            if self.is_vertex_added[v]:
                self.add_edges_to_pq(w)
                self.is_vertex_added[w] = True
            else:
                self.add_edges_to_pq(v)
                self.is_vertex_added[v] = True
        
    def get_mst(self):
        for edge in self.mst:
            print(edge.v,edge.w,edge.weight)
            
def test_prims_lazy_mst():
    w_graph = WeightedGraph(4)
    w_graph.add_edge(1,0,-10)
    w_graph.add_edge(1,2,-35)
    w_graph.add_edge(0,2,-15)
    w_graph.add_edge(0,3,-12)
    w_graph.add_edge(1,3,-11)
    w_graph.add_edge(2,3,-30)
    prims_lazy = PrimsLazyMst(w_graph)
    prims_lazy.get_mst()

test_prims_lazy_mst()
