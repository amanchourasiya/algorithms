class DirectedEdge():
    def __init__(self,v,w,weight):
        self.v = v
        self.w = w
        self.weight = weight

    def edge_from(self):
        return self.v
    
    def edge_to(self):
        return self.w

    def weight(self):
        return self.weight


class EdgeWeightedDiGraph():
    def __init__(self,v):
        self.vertices = [[] for i in range(v)]

    def add_edge(self,edge):
        self.vertices[edge.edge_from()] = edge
    
    def adj(self,v):
        return self.vertices[v]

        