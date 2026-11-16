class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        c = defaultdict(int)
        for n in nums:
            c[n]+=1
        r = []
        for i in range(len(nums)):
            c[nums[i]]-=1
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                c[nums[j]]-=1
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                for k in range(j+1,len(nums)):
                    c[nums[k]]-=1
                    if k>j+1 and nums[k]==nums[k-1]:
                        continue
                    f = target -(nums[k]+nums[j]+nums[i])
                    if c[f]>0:
                        r.append([f,nums[k],nums[j],nums[i]])
                for k in range(j+1,len(nums)): 
                    c[nums[k]]+=1
            for j in range(i+1,len(nums)): 
                c[nums[j]]+=1
        for i in range(len(nums)): 
            c[nums[i]]+=1
        return r