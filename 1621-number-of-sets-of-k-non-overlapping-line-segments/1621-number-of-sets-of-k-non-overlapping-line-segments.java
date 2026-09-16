class Solution {
    public int numberOfSets(int n, int k) {
        long MOD = 1000000007;

        long[][] dp = new long[n][k + 1];
        for (int i = 0; i < n; i++) {
            dp[i][0] = 1;
        }

        for (int segments = 1; segments <= k; segments++) {
            long sum = 0;

            for (int points = 1; points < n; points++) {

                sum = (sum + dp[points - 1][segments - 1]) % MOD;

                dp[points][segments] =
                    (dp[points - 1][segments] + sum) % MOD;
            }
        }

        return (int) dp[n - 1][k];
    }
}