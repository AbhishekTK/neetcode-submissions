class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        s = []


        for a in asteroids:
            while s and s[-1]>0 and a<0:
                d = s[-1]+a

                if d>0:
                    a=0
                elif d<0:
                    s.pop()
                else:
                    a=0
                    s.pop()
                    

                 
            if a:
                s.append(a)
        return s
