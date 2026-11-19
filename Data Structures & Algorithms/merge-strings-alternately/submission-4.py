class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p,q = 0,0
        # if word1>word2:
        #     return 
        r = []
        while p<len(word1) and q<len(word2):
            r.append(word1[p])
            r.append(word2[q])
            p+=1
            q+=1

        r.append(word1[p:])
        r.append(word2[q:])
        return "".join(r)
        