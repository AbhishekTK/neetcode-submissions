class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nn = [1] + nums +[1]
        dp  = {}
        def d(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            
            dp[(l,r)] = 0

            for i in range(l,r+1):
                c = nn[l-1]*nn[i]*nn[r+1]
                c+=d(l,i-1)+d(i+1,r)
                dp[(l,r)]= max(dp[(l,r)],c)
            return dp[(l,r)]
        return d(1,len(nn)-2)