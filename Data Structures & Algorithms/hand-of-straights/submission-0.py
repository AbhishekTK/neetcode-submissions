from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize!=0:
            return False
        
        c = Counter(hand)
        
        st =True
        l = len(hand)
        while True:
            m = 1001
            for k,v in c.items():
                if m>k and v>0:
                    m = k
            if m==1001:
                return True
            for i in range(1,groupSize):
                if c[m+1]<=0:
                    return False
                else:
                    c[m+1] -=1
                    
            