class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = len(words)
        print([len(w) for w in words])
        m = max([len(w) for w in words])
        me  = [[]*m]
        print(me)
        for w in words:
            for i in range(len(w)):
                me[i].append(w[i])
        print(me)
