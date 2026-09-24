class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pa = [(p,s) for p,s in zip(position,speed)]
        pa.sort(reverse=True)
        r = 1
        prev = (target - pa[0][0])/pa[0][1]
        for i in range(1,len(position)):
            c = pa[i]
            t = (target-c[0])/c[1]
            if t>prev:
                r+=1
                prev = t
        return r
