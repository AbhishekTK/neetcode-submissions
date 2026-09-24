func hasDuplicate(nums []int) bool {
    s := make(map[int]bool)
    for _,n:= range nums{
        if s[n]{
            return true
        }
        s[n] = true
    }
    fmt.Println(s)
    // fmt.Println(type(s))
    return false
}
