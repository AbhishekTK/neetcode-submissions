class CountSquares:

    def __init__(self):
        self.pc = defaultdict(lambda: defaultdict(int))


    def add(self, point: List[int]) -> None:
        self.pc[point[0]][point[1]]+=1

    def count(self, point: List[int]) -> int:
        r = 0
        x1,y1 = point
        for y2 in pc[x1]:
            s = y2-y1
            if s==0:
                continue
            x3,x4 = x1+s,x1-s
            r+=(self.pc[x1][y2]*self.pc[x3][y1]*self.pc[x3][y2])
            r+=(self.pc[x1][y2]*self.pc[x4][y1]*self.pc[x4][y2])
        return r
