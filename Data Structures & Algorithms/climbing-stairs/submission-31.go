func climbStairs(n int) int {
    o := 1
        t :=1
        for i:=0,i<n-1;i++{
            tp := o
            o = o+t
            t = tp
        }
    return o 
}
