func subsets(nums []int) [][]int {
    r := [][]int{}
    s := []int{}
    var d func(int)
    d = func(i int){
        if i>= len(nums) {
            t := make([]int,len(s))
            copy(t,s)
            r = append(r,t)
            return
        }
        s = append(s,nums[i])
        d(i+1)
        s = s[:len(s)-1]
        d(i+1)
    } 
    d(0)
    return r
}
