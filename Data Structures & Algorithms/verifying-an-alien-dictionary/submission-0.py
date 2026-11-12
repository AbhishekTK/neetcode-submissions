class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = len(words)
        m = max(words)
        me  = []*m
        for w in words:
            for i in range(len(w)):
                me[i].append(w[i])
        print(me)
