class Solution {
    public long[] resultArray(int[] nums, int k) {

        long[] ans = new long[k];

        long[] dp = new long[k];

        for (int num : nums) {

            long[] newDp = new long[k];

            int remainder = num % k;
            newDp[remainder]++;

            for (int r = 0; r < k; r++) {

                if (dp[r] == 0) {
                    continue;
                }

                int newRemainder = (r * remainder) % k;

                newDp[newRemainder] += dp[r];
            }

            for (int r = 0; r < k; r++) {
                ans[r] += newDp[r];
            }

            dp = newDp;
        }

        return ans;
    }
}