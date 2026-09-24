class Node:
    def __init__(self,k:int,v:int):
        self.k,self.v = k,v
        self.n,self.p = None,None

class LRUCache:


    def __init__(self, capacity: int):
        self.cap = capacity
        self.c = {}
        self.l,self.r = Node(0,0),Node(0,0)
        self.l.n,self.r.p = self.r,self.l
    
    def remove(self,n):
        np ,nn = n.p,n.n
        # n.p.n = nn
        np.n = nn
        nn.p = np
        # n.n.p = np
    def insert(self,node):
        p,n = self.r.p,self.r
        p.n = n.p = node
        node.p = p
        node.n = n

    def get(self, key: int) -> int:
        if key in self.c:
            self.remove(self.c[key])
            self.insert(self.c[key])
            return self.c[key].v
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.c:
            self.remove(self.c[key])
            # self.c[k].v = value
            # self.insert(self.c[k])
            # return 
        self.c[key] = Node(key,value)
        self.insert(self.c[key])
        if len(self.c)>self.cap:
            lru = self.l.n
            self.remove(lru)
            del self.c[lru.k]
