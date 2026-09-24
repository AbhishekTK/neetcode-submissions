class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Arrays.asList(nums).stream().sorted()
        // Set<int> s = new Set
        int t = (int)Arrays.stream(nums).distinct().count();
        // System.out.println(t);
        if((t)==nums.length){
            return false;
        }
        return true;
    }
}