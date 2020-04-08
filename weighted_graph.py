import linked_list

class WeightedGraph():
    def __init__(self,v):
        self.v = v
        self.vertices = [None] * v

    def add_edge(self,v,w,weight):
        edge = Edge(v,w,weight)

        if self.vertices[v] is None:
            self.vertices[v] = linked_list.Node(edge)
        else:
            self.vertices[v] = self.vertices[v].insert(edge)
        
        if self.vertices[w] is None:
            self.vertices[w] = linked_list.Node(edge)
        else:
            self.vertices[w] = self.vertices[w].insert(edge)
    
    def adj(self,v):
        return self.vertices[v]


class Edge():
    def __init__(self,v,w,weight):
        self.v = v
        self.w = w
        self.weight = weight

    def either(self):
        return self.v
    
    def other(self,vertex):
        if vertex == self.v:
            return self.w
        else:
            return self.v

    def comapare_to(self,edge):
        if self.weight < edge.weight:
            return -1
        elif self.weight > edge.weight:
            return 1
        else:
            return 0