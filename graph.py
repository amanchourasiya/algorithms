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

'''
Implements depth first search algorithm
'''
class DepthSearchFirstPaths():
    def __init__(self,graph,s):
        no_of_vertices = len(graph.vertices)

        # isVisited will be used to track if a vertex is already visited
        self.isVisited = [False] * no_of_vertices 

        # edgeTo will keep track of the edge of vertex by which we reached to this index
        self.edgeTo = [-1] * no_of_vertices

        # count will keep track of connected components w.r.t. disconnected graphs
        self.count = 0

        # List keeping track of connected components cluster
        self.cc = [-1] * no_of_vertices
        self.dfs_wrapper(graph,s)
        self.printPath()
    
    def dfs_wrapper(self,graph,s):
        #self.dfs(graph,s)
        #self.count = self.count + 1
        #print(self.all_nodes_travesed())
        while self.all_nodes_travesed() == False:
            n = self.get_first_unvisited_node()
            self.dfs(graph,n)
            self.count = self.count + 1

    def dfs(self,graph,s):
        self.isVisited[s] = True
        self.graph = graph
        self.cc[s] = self.count
        nodes = self.graph.adjacent(s)
        tmp = nodes
        while tmp is not None:
            if self.isVisited[tmp.data] == False:
                self.dfs(self.graph,tmp.data)
                self.edgeTo[tmp.data] = s
                self.cc[tmp.data] = self.count
            tmp = tmp.next

    
    def printPath(self):
        print(self.edgeTo)
        print(self.cc)

    # Checks and returns the first node that is marked isVisited False
    def get_first_unvisited_node(self):
        vertices = self.isVisited
        for i in range(len(vertices)):
            if vertices[i] == False:
                return i
    
    # Checks if all nodes are traversed
    def all_nodes_travesed(self):
        vertices = self.isVisited
        print(vertices)
        for vertex in vertices:
            if vertex == False:
                return False
        return True

    # Check if two vertices are in same connected component
    def is_cc(self,v,w):
        vertices = self.cc
        if vertices[v] == vertices[w]:
            return True
        else:
            return False

from collections import deque
class BreadthFirstSearchPaths():
    def __init__(self,graph,s):
        self.graph = graph
        self.isVisited = [False] * len(self.graph.vertices)
        self.edgeTo = [-1] * len(self.graph.vertices)
        self.bfs(s)
        self.printPath()
    
    def bfs(self,s):
        q = deque()

        q.append(s)
        self.isVisited[s] = True

        while len(q) != 0:
            v = q.pop()
            nodes = self.graph.adjacent(v)
            tmp =nodes
            while tmp is not None:
                if self.isVisited[tmp.data] == False:
                    q.append(tmp.data)
                    self.isVisited[tmp.data] = True
                    self.edgeTo[tmp.data] = v
                tmp = tmp.next
    
    def printPath(self):
        print(self.edgeTo)
            


def test():

    graph = Graph(12)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(0,6)
    graph.add_edge(5,5)
    graph.add_edge(6,4)
    graph.add_edge(4,3)
    graph.add_edge(4,5)
    graph.add_edge(5,3)
    graph.add_edge(7,8)
    graph.add_edge(9,10)
    graph.add_edge(10,11)
    g = DepthSearchFirstPaths(graph,0)
    print(g.is_cc(1,2),g.is_cc(5,7),g.is_cc(7,9))

    

test()