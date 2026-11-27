class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        
        def c(l):
            r = []
            for i in range(4):
                d = str((int(l[i])+1)%10)
                r.append(l[:i]+d+l[i+1:])
                d = str((int(l[i])-1+10)%10)
                r.append(l[:i]+d+l[i+1:])
            return r
        v = set(deadends)
        q = deque([("0000",0)])
        while q:
            l,t = q.popleft()
            if l == target:
                return t
            for ch in c(l):
                if ch not in v:
                    v.add(ch)
                    q.append((ch,t+1))
        return -1