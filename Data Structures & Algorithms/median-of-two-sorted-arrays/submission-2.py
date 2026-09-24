class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l2,l1 = len(nums2),len(nums1)
        # if l2 > l1:
            # return self.findMedianSortedArrays(nums2, nums1)
        
        h = (l1+l2)//2+1
        p1,p2 = 0,0
        m1,m2 = 0,0
        for c in range(h):
            m2 = m1
            if p1<l1 and p2<l2:
                if nums1[p1]>nums2[p2]:
                    m1 = nums2[p2]
                    p2+=1
                else:
                    m1 = nums1[p1]
                    p1+=1
            elif p1<l1:
                m1 = nums1[p1]
                p1+=1
            else:
                m1 =nums2[p2]
                p2+=1
        
        if (l1+l2)%2==1:
            return float(m1)
        else:
            return (m1+m2)/2.0