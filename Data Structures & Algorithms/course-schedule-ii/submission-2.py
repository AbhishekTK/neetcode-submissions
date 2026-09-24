class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj = [[] for _ in range(numCourses)]
        for c,cr in prerequisites:
            adj[c].append(cr)
        r = []
        v,cy = set(),set()
        def dfs(ci):
            if ci in cy:
                return False
            if ci in v:
                return True
            cy.add(ci)
            for cr in adj[ci]:
                if dfs(cr)==False:
                    return False
            cy.remove(ci)
            v.add(ci)
            r.append(ci)
            return True
        for c in range(numCourses):
            if dfs(c) ==False:
                return []
        return r
            
            