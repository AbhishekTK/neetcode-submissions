class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s = []
        r = []
        n = len(nums)
        def dfs(i,ss,n):
            # if i>=n:
                # return
            if i>=n:
                r.append(ss.copy())
                return
            
            ss.append(nums[i])
            print(i,ss)
            dfs(i+1,ss,n)
            ss.pop()
            print(i,ss)
            dfs(i+1,ss,n)
        dfs(0,[],n)
        return r