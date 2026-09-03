class Solution {
    public boolean uniformArray(int[] nums1) {

        int min = nums1[0];
        boolean hasOdd = false;

        for (int num : nums1) {
            min = Math.min(min, num);

            if (num % 2 != 0) {
                hasOdd = true;
            }
        }

        // Smallest element cannot be changed,
        // so its parity decides the final parity.
        if (min % 2 != 0) {
            return true;
        }

        // Minimum is even.
        // If there is any odd number, that odd number
        // cannot become even.
        if (hasOdd) {
            return false;
        }

        return true;
    }
}