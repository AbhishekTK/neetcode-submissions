// Definition for a pair
// class Pair {
//     int key;
//     String value;
//
//     Pair(int key, String value) {
//         this.key = key;
//         this.value = value;
//     }
// }
public class Solution {
    public List<List<Pair>> insertionSort(List<Pair> pairs) {

        List<List<Pair>> snapshots = new ArrayList<>();
        List<Pair> copy = new ArrayList<>(pairs);

        for(int i = 0;i<copy.size();i++){
            Pair key = copy.get(i);
            int j = i-1;
            while(j>=0 && copy.get(j).key > key.key ){
                    copy.set(j+1,copy.get(j));
                    j--;
            }
            copy.set(j+1,key);
            List<Pair> snapshot = new ArrayList<>();
            for (Pair p : copy){
                snapshot.add(new Pair(p.key,p.value));
            }
            snapshots.add(snapshot);
        }
        return snapshots;
    }
}
