class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s = []

        for o in operations:
            if o=="+":
                s.append(s[-1]+s[-2])
            elif o=="C":
                s.pop()
            elif o=="D":
                s.append(s[-1]*2)
            else:
                s.append(o)
        return sum(s)