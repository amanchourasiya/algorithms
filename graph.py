import linked_list

class Graph():
    def __init__(self,vertices):
        self.vertices = [None] * vertices

    def add_edge(self,v,w):
        if self.vertices[v] is None:
            self.vertices[v] = linked_list.Node(w)
        else:
            self.vertices[v] = self.vertices[v].insert(w)
        if self.vertices[w] is None:
            self.vertices[w] = linked_list.Node(v)
        else:
            self.vertices[w] = self.vertices[w].insert(v)
    
    def adjacent(self,v):
        return self.vertices[v]

    def V(self):
        return len(self.vertices)

    def E(self):
        count = 0
        for vertex in range(len(self.vertices)):
            count = count + vertex_degree(self,vertex)
        return count // 2


'''
API for performing different graph operations
'''
def vertex_degree(graph,vertex):
    v = graph.adjacent(vertex)
    return v.count_elements()
    
def max_degree(graph):
    max = 0
    for vertex in range(len(graph.vertices)):
        if vertex_degree(graph,vertex) > max:
            max = vertex_degree(graph,vertex)
    return max

def test():

    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(3,0)
    graph.add_edge(3,4)
    graph.add_edge(4,0)
    print(graph.V())

test()