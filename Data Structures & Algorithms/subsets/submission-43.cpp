class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> r;
        vector<int> s;
        dfs(nums,0,s,r);
        return r;
    }

private:
    void dfs(const vector<int>& nums, int i, vector<int>& s, vector<vector<int>>& r ){
        if(i>=nums.size()){
            r.push_back(s);
            return;
        }
        s.push_back(nums[i]);
        dfs(nums, i+1,s,r);
        s.pop_back();
        dfs(nums,i+1,s,r);
    }

};