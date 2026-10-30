from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand)%groupSize!=0:
            return False
        
        c = Counter(hand)
        
        for n in hand:
            s = n
            while c[s-1]:
                s = s-1
            while s<=n:
                while c[s]:
                    for i in range(s,s+groupSize):
                        if not c[i]:
                            return False
                        c[i]-=1
                s+=1
        return True
                    
            