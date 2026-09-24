func maxSlidingWindow(nums []int, k int) []int {
    op := make([]int, 0,len(nums)-k+1)
        for i:=0;i<=len(nums)-k;i++{
            m := nums[i]
            for j:=i;j<i+k;j++{
                if m<nums[j]{
                    m = nums[j]
                }
            }
            op = append(op,m)
        }
    return op
}
