import numpy as np
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = [float('inf')]*n
        d[k-1] = 0
        for _ in range(n-1):
            for u,v,w in times:
                if d[u-1]+w< d[v-1]:
                    d[v-1]= d[u-1]+w
        r = max(d)
        return r if r<float('inf') else -1