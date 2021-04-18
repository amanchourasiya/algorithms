import weighted_graph
import sys

class BellmanFord:
    def __init__(self, graph, source):
        self.graph = graph
        self.source = source
        self.edge_to = {}
        # Populate edge_to matrix
        

        self.dist_to = {}
        # Populate dist_to edges
        for vertex in range(len(self.graph.vertices)):
            self.dist_to[vertex] = sys.maxsize -10
        
        self.dist_to[self.source] = 0

    
    def find_spt(self): # SPT means shortest path tree
        edges = self.graph.get_all_edges()
        print('edges', len(edges))
        for _ in range(len(self.graph.vertices)-1):
            print(self.dist_to)
            # relax every vertex
            for edge in edges:
                print(edge.v, edge.w, edge.weight)
                print(self.dist_to)
                if self.dist_to[edge.v] + edge.weight < self.dist_to[edge.w]:
                    self.dist_to[edge.w] =  self.dist_to[edge.v] + edge.weight
                    self.edge_to[edge.w] = edge.w


def test():
    graph = weighted_graph.WeightedGraph(5)
    graph.add_edge(0,1,-1)
    graph.add_edge(0,2,4)
    graph.add_edge(1,2,3)
    graph.add_edge(1,3,2)
    graph.add_edge(1,4,2)
    graph.add_edge(3,2,5)
    graph.add_edge(3,1,1)
    graph.add_edge(4,3,-3)

    bf = BellmanFord(graph, 0)
    bf.find_spt()
    print(bf.dist_to)

test()
