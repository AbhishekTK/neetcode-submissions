class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 0
        res = 0
        c = False
        l = []
        for i in range(len(nums)):
            e = nums[i]
            if e in l:
                continue
            else:
                print("i,e")
                print(i,e)
                for j in range(e,e+len(nums)):
                    print("j")
                    print(j)
                    print("l")
                    print(l)
                    
                    if j in nums:
                        count += 1
                        res = max(res,count)
                        print("True count,res")
                        print(count,res)
                    else:
                        count = 0
                        print("False count,res")
                        print(count,res)
                        break
                    l.append(j)
                    print("l")
                    print(l)
        return res