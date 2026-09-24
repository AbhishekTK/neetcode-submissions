class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        perm = self.permute(nums[1:])
        r = []
        for p in perm:
            for i in range(len(p)+1):
                pc = p.copy()
                pc.insert(i,nums[0])
                r.append(pc)
        return r