class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        r = set()
        candidates.sort()
        def dfs(i,c,t):
            if t==target:
                r.add(tuple(c))
                return
            if i == len(candidates) or t>target:
                return
            
            c.append(candidates[i])
            dfs(i+1,c,t+candidates[i])
            c.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,c,t)
            
        dfs(0,[],0)
        return [list(res) for res in r]
                