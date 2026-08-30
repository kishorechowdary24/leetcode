class Solution {
    public int minimumDeletions(int[] nums) {

        int n = nums.length;

        int min = nums[0];
        int max = nums[0];

        int minIndex = 0;
        int maxIndex = 0;
        for (int i = 1; i < n; i++) {

            if (nums[i] < min) {
                min = nums[i];
                minIndex = i;
            }

            if (nums[i] > max) {
                max = nums[i];
                maxIndex = i;
            }
        }

        int a = Math.min(minIndex, maxIndex);
        int b = Math.max(minIndex, maxIndex);

        int front = b + 1;

        int back = n - a;
        int both = (a + 1) + (n - b);

        return Math.min(front, Math.min(back, both));
    }
}