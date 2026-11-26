class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums)%k!= 0:
            return False
        nums.sort(reverse=True)
        
        t = sum(nums)//k
        used = [False]*len(nums)
        def b(i,k,sss):
            if k==0:
                return True
            if sss==t:
                return b(0,k-1,0)
            for j in range(i,len(nums)):
                if used[j] or sss+nums[j]>t:
                    continue
                used[j] = True
                if b(j+1,k,sss+nums[j]):
                    return True
                used[j] = False
                if sss==0:
                    return False
            return False
        return b(0,k,0)
            

