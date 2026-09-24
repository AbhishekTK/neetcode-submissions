class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        v = [False]*len(nums)
        def b(s):
            if len(s) == len(nums):
                r.append(s[:])
                return

            for i in range(len(nums)):    
                if v[i]:
                    continue
                if i>0 and nums[i]== nums[i-1] and not v[i]:
                    continue
                v[i]=True
                s.append(nums[i])
                b(s)
                v[i] = False
                s.pop()
        b([])
        return r