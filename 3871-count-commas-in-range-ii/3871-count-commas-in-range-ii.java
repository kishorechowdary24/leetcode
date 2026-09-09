class Solution {
    public long countCommas(long n) {
        long c = 0;
        long p = 1000;

        while (p <= n) {
            c += n - p + 1;
            p *= 1000;
        }

        return c;
    }
}