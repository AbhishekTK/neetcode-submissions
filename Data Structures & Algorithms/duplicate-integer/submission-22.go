// import "fmt"
func hasDuplicate(nums []int) bool {
    s := make(map[int]bool)
    fmt.Println("s",s)
    for _,n:= range nums{
        fmt.Println("s",s)
        if s[n]{
            return true
        }
        s[n] = true
    }
    fmt.Println("s",s)
    fmt.Println("%T",(s))
    return false
}
