class MinStack:

    def __init__(self):
        self.a = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.a:
            self.a.append(0)
            self.min = val
        else:
            self.a.append(val-self.min)
            if val-self.min<0:
                self.min = val


    def pop(self) -> None:
        if not self.a:
            return 
        p = self.a.pop()
        if p <0:
            self.min = self.min - p
        
    def top(self) -> int:
        if self.a[-1]>0:
            return self.a[-1]+self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min