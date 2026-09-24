class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        m = {c: set() for w in words for c in w}

        for i in range(1,len(words)):
            w1 = words[i-1]
            w2 = words[i]
            ml = min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:ml]==w2[:ml]:
                return ""

            for j in range(ml):
                if w1[j]!=w2[j]:
                    m[w1[j]].add(w2[j])
                    break
        
        v = {}
        r = []

        def d(c):
            if c in v:
                return v[c]
            v[c] = True
            for e in m[c]:
                if d(e):
                    return True
            v[c] = False
            r.append(c)
        for c in m:
            if d(c):
                return ""
        r.reverse()
        return "".join(r)

