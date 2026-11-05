impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let (mut l,mut r) = (0,s.len().wrapping_sub(1));
        while l<r{
            s.swap(l,r);
            l+=1;
            r-=1;
        }
    }
}
