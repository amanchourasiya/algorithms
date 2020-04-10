class QuickFind():
    def __init__(self,v):
        self.vertices = [i for i in range(v)]
    
    def add_union(self,v,w):
        x = self.vertices[w]
        for i in range(len(self.vertices)):
            if self.vertices[i] == x:
                self.vertices[i] = self.vertices[v]

        #self.vertices[w] = self.vertices[v]
    
    def check_union(self,v,w):
        if self.vertices[v] == self.vertices[w]:
            return True
        else:
            return False

class QuickUnion():
    def __init__(self,v):
        self.vertices = [i for i in range(v)]

    def add_union(self,v,w):
        self.vertices[w] = v

    def find_root(self,v):
        while self.vertices[v] != v:
            v = self.vertices[v]
        return v
    
    def check_union(self,v,w):
        root_v = self.find_root(v)
        root_w = self.find_root(w)

        if root_v == root_w:
            return True
        else:
            return False

class UnionFind():
    def __init__(self,v):
        self.vertices = [i for i in range(v)]

    def find_root(self,v):
        while self.vertices[v] != v:
            v = self.vertices[v]
        return v

    def add_union(self,v,w):
        self.vertices[w] = self.find_root(v)
    
    def check_union(self,v,w):
        root_v = self.find_root(v)
        root_w = self.find_root(w)

        if root_v == root_w:
            return True
        else:
            return False


def quick_find_test():
    qf = QuickFind(9)
    qf.add_union(0,1)
    print(qf.vertices)
    qf.add_union(1,2)
    qf.add_union(2,3)
    qf.add_union(4,5)
    qf.add_union(6,7)
    qf.add_union(7,8)
    qf.add_union(6,8)
    #qf.add_union(2,4)
    qf.add_union(1,8)
    print(qf.vertices)

    print(qf.check_union(2,3))
    print(qf.check_union(3,4))

def quick_union_test():
    qf = QuickUnion(9)
    qf.add_union(0,1)
    qf.add_union(1,2)
    qf.add_union(2,3)
    qf.add_union(4,5)
    qf.add_union(6,7)
    qf.add_union(7,8)
    #qf.add_union(6,8)
    qf.add_union(2,4)
    #qf.add_union(1,8)
    print(qf.vertices)

    print(qf.check_union(2,3))
    print(qf.check_union(3,4))

def union_find_test():
    qf = UnionFind(9)
    qf.add_union(0,1)
    qf.add_union(1,2)
    qf.add_union(2,3)
    qf.add_union(4,5)
    qf.add_union(6,7)
    qf.add_union(7,8)
    #qf.add_union(6,8)
    #qf.add_union(2,4)
    qf.add_union(1,8)
    print(qf.vertices)

    print(qf.check_union(2,3))
    print(qf.check_union(1,8))

#quick_find_test()
#quick_union_test()
#union_find_test()