class Solution {
    public int longestOnes(int[] nums, int k) {
        int n = nums.length;
        int maxlength = 0;
        for (int i = 0; i < n; i++){
            int countzero = 0;
            for(int j = i; j < n; j++){
                if (nums[j] == 0){
                    countzero++;
                }
                if(countzero > k){
                    break;
                }
                maxlength = Math.max(maxlength, j - i + 1);
            }
        }
        return maxlength;
    }
}