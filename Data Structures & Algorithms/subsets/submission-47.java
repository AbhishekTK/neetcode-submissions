class Solution {
    public void d(int[] n, int i,List<Integer> s, List<List<Integer>> r){
        if (i>=n.length){
            r.add(new ArrayList<>(s));
            return;
        }
        s.add(n[i]);
        d(n,i+1,s,r);
        s.remove(s.size()-1);
        d(n,i+1,s,r);

    }
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> r= new ArrayList<>();
        List<Integer> s= new ArrayList<>();
        d(nums,0,s,r);
        return r;
    }
    
}
