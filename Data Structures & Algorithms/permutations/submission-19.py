class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        c = [False]*len(nums)
        def b(c,curr):
            f = False
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for i,num in enumerate(nums):
                if c[i] != True:
                    curr.append(nums[i])
                    c[i] = True
                    b(c,curr)
                    curr.pop()
                    c[i] = False
                # b(c,curr)
        b(c,[])
        return res

