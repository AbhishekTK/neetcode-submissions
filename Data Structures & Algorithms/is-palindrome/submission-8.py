class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = []
        for c in s:
            if (ord(c)>=ord('A') and ord(c)<=ord('Z')) or (ord(c)>=ord('a') or ord(c)<=ord('z')) or (ord(c)>=ord('0') and ord(c)<=ord('9') ):
                r.append(c)
        
        n =len(r)
        print(r)
        i = 0
        while i>n//2:
            if r[i]!=r[n-i]:
                return False
            i+=1
        return True
