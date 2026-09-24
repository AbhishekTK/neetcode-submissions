class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # memo = set()
        memo = {}
        for i,num in enumerate((nums)):
            diff = target - num

            if diff in memo:
                return [memo[diff],i]
                # if diff > num:
                #     return [i,memo[diff]]
                # else:
                #     return [memo[diff],i]
            memo[num] = i
        # return new list()
        