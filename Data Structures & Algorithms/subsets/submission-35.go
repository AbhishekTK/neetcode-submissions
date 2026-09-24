func subsets(nums []int) [][]int {
    r:= [][]int{} 
    s := []int{}
    var dfs func(int)
    dfs = func(i int){
        if i>=len(nums){
            t:=make([]int, len(s))
            copy(t,s)
            r = append(r,t)
            return
        }
        s = append(s,nums[i])
        dfs(i+1)
        s = s[:len(s)-1]
        dfs(i+1)
    }
    dfs(0)
    return r
}
