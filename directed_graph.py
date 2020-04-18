class DiGraph():
    def __init__(self,v):
        self.vertices = [[] for i in range(v)]

    def add_edge(self,v,w):
        self.vertices[v].append(w)

    def ajd(self,v):
        return self.vertices[v]

    def E(self):
        count = 0
        for vertex in self.vertices:
            for edge in vertex:
                count +=1
        return count
    