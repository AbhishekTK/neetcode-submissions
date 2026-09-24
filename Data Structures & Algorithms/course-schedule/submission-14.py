class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {k:[] for k in range(numCourses)}
        for k,v in prerequisites:
            m[k].append(v) 
        v = set()
        def dfs(crs):
            if crs in v:
                return False
            if m[crs] == []:
                return True
            v.add(crs)
            for c in m[crs]:
                if not dfs(c):
                    return False
            v.remove(crs)
            m[crs] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True




                 