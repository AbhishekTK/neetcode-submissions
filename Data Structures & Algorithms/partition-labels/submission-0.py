class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i,c in enumerate(s):
            m[c]= i
        print(m)
        size = 0
        r = []
        return r