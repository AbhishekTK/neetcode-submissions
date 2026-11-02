class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        m = {}
        for i,c in enumerate(s):
            # if c in m:

            m[c]= i

        # print(m)
        size = 0
        r = []
        end = 0
        
        for i,c in enumerate(s):
            size+=1
            end = max(end,m[c])
            if i== end:
                r.append(size)
                size = 0 
        return r