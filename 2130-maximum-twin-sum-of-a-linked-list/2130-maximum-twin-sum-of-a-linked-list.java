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
    public int pairSum(ListNode head) {
        ArrayList<Integer> List = new ArrayList<>();

        while (head != null){
            List.add(head.val);
            head = head.next;
        }

        int i = 0;
        int j = List.size() - 1;
        int ans = 0;

        while (i < j ){
            ans = Math.max(ans, List.get(i) + List.get(j));

            i++;
            j--;
        }
        return ans;
    }
}