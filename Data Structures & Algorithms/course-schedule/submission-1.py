class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        a = { i:[] for i in range(numCourses)}
        
        for p in prerequisites:
            a[p[0]].append(p[1])
        v = set()
        
        def cdfs(n):
            if n in v:
                return False
            if a[n] == []:
                return True
            v.add(n)
            for an in a[n]:
                if not cdfs(an):
                    return False
            v.remove(n)
            a[n] = []
            return True
            
        for i in range(numCourses):
            if not cdfs(i):
                return False
        return True