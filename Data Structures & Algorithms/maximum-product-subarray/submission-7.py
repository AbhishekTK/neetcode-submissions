class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        a,c = [],[]
        res = float('-inf')
        for n in nums:
            res = max(res,n)
            if n==0:
                if c:
                    a.append(c)
                c = []
            else:
                c.append(n)
        if c:
            a.append(c)
        print(a)
        for sub in a:
            negs = sum(1 for i in sub if i<0)
            prod = 1
            need = negs if negs%2 == 0 else negs -1
            negs = 0
            j = 0

            for i in range(len(sub)):
                prod *= sub[i]
                if sub[i]<0:
                    negs+=1
                    while negs> need:
                        prod //= sub[j]
                        if sub[j]<0:
                            negs -=1
                        j+=1
                if j<=i:
                    res = max(res,prod)

        return res