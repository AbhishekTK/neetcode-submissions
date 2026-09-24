class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l2,l1 = len(nums2),len(nums1)
        # if l2 > l1:
            # return self.findMedianSortedArrays(nums2, nums1)
        
        # h = (l1+l2)/2
        m = nums1+nums2
        m.sort()
        t = len(m)
        if t%2==0:
            return (m[t//2-1]+m[t//2])/2
        else:
            return m[t//2]