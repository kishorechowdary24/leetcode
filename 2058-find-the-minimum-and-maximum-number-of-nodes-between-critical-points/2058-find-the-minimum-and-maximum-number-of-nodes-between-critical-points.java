/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        List<Integer> criticalPoints = new ArrayList<>();

        int position = 1;

        ListNode prev = head;
        ListNode curr = head.next;

        while (curr != null && curr.next != null){
            ListNode next = curr.next;

            if (curr.val > prev.val && curr.val > next.val){
                criticalPoints.add(position);
            }

            else if(curr.val < prev.val && curr.val < next.val){
                criticalPoints.add(position);
            }

            prev = curr;
            curr = curr.next;
            position++;
        }

        if (criticalPoints.size() < 2){
            return new int[]{-1, -1};
        }

        int minDistance = Integer.MAX_VALUE;
        int maxDistance = 0;

        for (int i = 1; i< criticalPoints.size(); i++){
            int distance = criticalPoints.get(i) - criticalPoints.get(i-1);

            minDistance = Math.min(minDistance, distance);

        }

        maxDistance = criticalPoints.get(criticalPoints.size() -1) - criticalPoints.get(0);

        return new int[]{minDistance, maxDistance};
    }
}