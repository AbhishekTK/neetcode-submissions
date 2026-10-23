class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = ""
        for c in s:
            if (ord(c)>=ord('A') and ord(c)<=ord('Z')) or (ord(c)>=ord('a') and ord(c)<=ord('z')) or (ord(c)>=ord('0') and ord(c)<=ord('9') ):
                r+=c
        
        n =len(r)
        print(r)
        i = 0
        while i<n//2:
            print(r[i].lower(),r[n-i-1].lower())
            if r[i].lower()!=r[n-i-1].lower():
                return False
            i+=1
        return True
