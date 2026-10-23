class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = []
        for c in s:
            if (c>='A' and c<='Z') or (c>='a' or c<='z') or (c>='0' and c<='9' ):
                r.append(c)
        
        n =len(r)
        print(r)
        i = 0
        while i>n//2:
            if r[i]!=r[n-i]:
                return False
            i+=1
        return True
