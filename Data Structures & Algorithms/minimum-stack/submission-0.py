class MinStack:

    def __init__(self):
        self.es = []
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        if not self.es or val <= self.es[-1]:
            self.es.append(val)

    def pop(self) -> None:
        val = self.s.pop()
        if val == self.es[-1]:
            self.es.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.es[-1]