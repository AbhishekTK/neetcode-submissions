class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> m = new HashSet<>();
        for (int i: nums){
            if(m.contains(i)){
                return true;
            }
            m.add(i);
        }
        return false;
    }
}