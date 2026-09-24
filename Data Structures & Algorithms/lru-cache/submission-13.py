class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.c = []

    def get(self, key: int) -> int:
        for i in range(len(self.c)):
            if self.c[i][0] == key:
                t = self.c.pop(i)
                self.c.append(t)
                return t[1]
        return -1

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.c)):
            if self.c[i][0] == key:
                t = self.c.pop(i)
                t[1]=value
                self.c.append(t)
                return
                # return t[1]
        if len(self.c)==self.cap:
            self.c.pop(0)
        self.c.append([key,value])

        
