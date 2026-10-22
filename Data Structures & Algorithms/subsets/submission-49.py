class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # s = set()
        s = []

        def dfs(i,ss):
            s.append(ss.copy())
            for j in range(i,len(nums)):

                ss.append(nums[j])
                dfs(j+1,ss)
                ss.pop()
        
        dfs(0,[])
        return s