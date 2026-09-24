class Solution {
    public boolean hasDuplicate(int[] nums) {
        // Arrays.asList(nums).stream().sorted()
        // Set<int> s = new Set
        // int t = (int)Arrays.stream(nums).distinct().count();
        // System.out.println(t);
        Set<Integer> u = new HashSet<>();
        Set<Integer> us = Arrays.stream(nums).boxed().filter( e -> !u.add(e)).collect(Collectors.toSet());
        if(us.isEmpty()){
            return false;
        }
        return true;
    }
}