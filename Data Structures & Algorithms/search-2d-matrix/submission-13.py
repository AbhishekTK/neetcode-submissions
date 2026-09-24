class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c = len(matrix), len(matrix[0])
        dr = -1
        for i,r in enumerate(matrix):
            print(i)
            print(r)
            if target >= r[0] and target<= r[-1]:
                dr = i
        print(dr)
        l,ri = 0,c-1
        if dr==-1:
            return False
        while l<=ri:
            print(l)
            print(ri)
            m = (l+ri)//2
            print("m",m)
            print(matrix[dr][m])
            print(target)
            if target == matrix[dr][m]:
                print(matrix[dr][m])
                print(target)
                return True
            if target> matrix[dr][m]:
                l = m+1
            else:
                ri = m-1
        return False