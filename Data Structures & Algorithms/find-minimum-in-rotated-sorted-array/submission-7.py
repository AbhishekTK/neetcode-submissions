class Solution:
    def findMin(self, nums: List[int]) -> int:

        mn = nums[0]
        i,j = 0,len(nums)-1
        while i<=j:
            if nums[i]<nums[j]:
                mn = min(mn,nums[i])
                break

            m = (i+j)//2;
            mn = min(mn,nums[m])
            if nums[m]>= nums[i]:
                i = m+1
            else:
                j = m -1
            
        return mn

        