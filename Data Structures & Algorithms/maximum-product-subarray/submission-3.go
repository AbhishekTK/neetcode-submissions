func maxProduct(nums []int) int {
    res  := nums[0]

    for i := range(len(nums)){

        c := nums[i]
        res = max(c,res)
        for j := i+1;j<len(nums);j++{
            c *= nums[j]
            res = max(c,res)
        }
    }
    return res
}
