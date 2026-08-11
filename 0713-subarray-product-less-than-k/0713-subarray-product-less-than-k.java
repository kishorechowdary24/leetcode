class Solution {
    public int numSubarrayProductLessThanK(int[] nums, int k) {
        if (k<= 1){
            return 0;
        }
        int count = 0;
        int n = nums.length;

        for (int i =0; i < n; i++){
            int prod  = 1;

            for(int j = i; j >= 0; j--){
                prod *= nums[j];
                if(prod < k){
                    count++;
                }
                else{
                    break;
                }
            }
        }
        return count;
}
}