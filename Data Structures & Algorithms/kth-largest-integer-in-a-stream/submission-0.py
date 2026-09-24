class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.a= nums

    def add(self, val: int) -> int:
        self.a.append(val)
        self.a.sort()
        return self.a[len(self.a)-self.k]