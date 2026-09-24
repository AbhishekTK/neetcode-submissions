class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        stones.sort()

        while n>1:
            d = stones.pop() - stones.pop()
            n -=2

            if d>0:
                # m = 0
                l = 0
                r = n
                while l<r:
                    mid = (l+r)//2
                    if d> stones[mid]:
                        l = mid+1
                    else:
                        r = mid
                p= l
                n+=1
                stones.append(0)
                for i in range(n-1,p,-1):
                    stones[i] = stones[i-1]
                stones[p] = d

        return stones[0] if n>0 else 0

        