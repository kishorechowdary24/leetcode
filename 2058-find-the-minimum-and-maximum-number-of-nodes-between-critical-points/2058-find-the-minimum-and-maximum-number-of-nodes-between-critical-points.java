class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {

        ListNode prev = head;
        ListNode curr = head.next;

        int position = 1;

        int firstCritical = -1;
        int prevCritical = -1;

        int minDistance = Integer.MAX_VALUE;

        while (curr != null && curr.next != null) {

            ListNode next = curr.next;

            // Check if current node is a critical point
            if ((curr.val > prev.val && curr.val > next.val) ||
                (curr.val < prev.val && curr.val < next.val)) {

                // First critical point
                if (firstCritical == -1) {
                    firstCritical = position;
                }

                // Calculate distance from previous critical point
                if (prevCritical != -1) {
                    int distance = position - prevCritical;
                    minDistance = Math.min(minDistance, distance);
                }

                // Current critical point becomes previous critical point
                prevCritical = position;
            }

            prev = curr;
            curr = curr.next;
            position++;
        }

        // Fewer than 2 critical points
        if (firstCritical == prevCritical) {
            return new int[]{-1, -1};
        }

        // Distance between first and last critical points
        int maxDistance = prevCritical - firstCritical;

        return new int[]{minDistance, maxDistance};
    }
}