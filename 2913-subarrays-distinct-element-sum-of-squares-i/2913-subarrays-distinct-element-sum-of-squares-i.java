
import java.util.*;

class Solution {
    public int sumCounts(List<Integer> nums) {
        int ans = 0;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                Set<Integer> distinct = new HashSet<>();

                for (int k = i; k <= j; k++) {
                    distinct.add(nums.get(k));
                }

                int count = distinct.size();
                ans += count * count;
            }
        }

        return ans;
    }
}

