
class WeightedGraph():
    def __init__(self,v):
        self.vertices = [None] * v

    def add_edge(self,v,w,weight):
        edge = Edge(v,w,weight)

        if self.vertices[v] is None:
            self.vertices[v] = Node(edge)
        else:
            self.vertices[v] = self.vertices[v].insert(edge)
        
        if self.vertices[w] is None:
            self.vertices[w] = Node(edge)
        else:
            self.vertices[w] = self.vertices[w].insert(edge)
    
    def adj(self,v):
        return self.vertices[v]
    
    def get_edges(self):
        ret = set()
        for vertex in self.vertices:
            tmp = vertex
            while tmp is not None:
                ret.add(tmp)
                tmp = tmp.next
        return ret



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

    def get_weight(self):
        return self.weight

    def comapare_to(self,edge):
        if self.weight < edge.weight:
            return -1
        elif self.weight > edge.weight:
            return 1
        else:
            return 0

# Supporting data structure to store a linked list attached to each vertex
class Node():
    def __init__(self,edge):
        self.edge = edge
        self.next = None

    def insert(self,edge):
        node = Node(edge)
        node.next = self
        return node

    def traverse_list(self):
        tmp = self
        while tmp is not None:
            print(tmp.edge.v,tmp.edge.w,tmp.edge.weight)
            tmp = tmp.next

    def comapare_to(self,node):
        if self.edge.weight < node.edge.weight:
            return -1
        elif self.edge.weight > node.edge.weight:
            return 1
        else:
            return 0
        

    
def test_node():
    n = Node(Edge(1,2,.090))
    n = n.insert(Edge(2,3,33))
    n = n.insert(Edge(2,5,22))
    n.traverse_list()

test_node()
