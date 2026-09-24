class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, List<String>> res = new HashMap<>();

        for(String s : strs){
            int[] m = new int[26];
            for (char c : s.toCharArray()){
                m[c - 'a'] += 1;

            }
            String k = Arrays.toString(m);
            res.putIfAbsent(k, new ArrayList<>());
            res.get(k).add(s);
        }
        return new ArrayList<>(res.values());

        
    }
}
