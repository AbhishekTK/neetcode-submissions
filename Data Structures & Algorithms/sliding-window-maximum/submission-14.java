class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        List<Integer> r = new ArrayList<>();
        for(int i=0;i<nums.length -k+1;i++){
            int m = nums[i];
            for(int j=i;j<i+k;j++){
                m = Math.max(m,nums[j]);
            }
            r.add(m);
        }
        return r.stream().mapToInt(Integer::intValue).toArray();
    }
}
