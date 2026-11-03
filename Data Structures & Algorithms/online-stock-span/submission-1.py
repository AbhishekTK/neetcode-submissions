class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        self.s.append(price)
        if len(self.s)==1:
            return 1
        for i in range(len(self.s)-2,-1,-1):
            if self.s[i]>price :
                return len(self.s) - i-1
        return len(self.s)

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)