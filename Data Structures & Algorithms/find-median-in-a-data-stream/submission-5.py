class MedianFinder:

    def __init__(self):
        self.l = []

    def addNum(self, num: int) -> None:
        self.l.append(num)

    def findMedian(self) -> float:
        self.l.sort()
        n = len(self.l)
        return self.l[n//2] if n%2!=0 else (self.l[n//2] +self.l[(n//2)-1])/2
        