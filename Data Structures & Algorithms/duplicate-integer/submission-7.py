class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        print(set(nums))
        print(len(set(nums)))

        print(len((nums)))
        print(len(nums) == len(set(nums)))
        
        return True if ( len(nums) != len(set(nums))) else False