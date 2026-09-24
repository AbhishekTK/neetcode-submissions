class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for n in nums:

            np = []

            for p in perms:
                for i in range(len(p)+1):
                    pc = p.copy()
                    pc.insert(i,n)
                    np.append(pc)
            perms = np
        return perms