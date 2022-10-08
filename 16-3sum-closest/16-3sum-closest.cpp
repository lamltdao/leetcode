class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = 10000000;
        for (int i = 0; i < nums.size()-2; ++i) {
            int l = i+1;
            int r = nums.size()-1;
            while (l < r) {
                if (abs(res - target) > abs(nums[i] + nums[l] + nums[r] - target)) {
                    res = nums[i] + nums[l] + nums[r];
                }
                if (nums[l] + nums[r] < target-nums[i]){
                    l++;
                }
                else {
                    r--;
                }
            }
        }
        return res;
    }
};