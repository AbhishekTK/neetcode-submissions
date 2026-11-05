impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        fn reverse(s: &mut Vec<char>, l:usize,r:usize){
            if l<r{
                reverse(s,l+1,r-1);
                s.swap(l,r);
            }

        }
        if !s.is_empty(){
            reverse(s,0,s.len()-1)
        }
    }
}
