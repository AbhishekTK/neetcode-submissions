func subsets(nums []int) [][]int {
    n:= len(nums)
    r := [][]int{}

    for i:=0; i<(1<<n);i++{
        ss:= []int{}
        for j:=0;j<n;j++{
            if (i & (1<<j)) != 0{
                ss=append(ss,nums[j])
            }
        }
        r= append(r,ss)
    }
    return r
}
