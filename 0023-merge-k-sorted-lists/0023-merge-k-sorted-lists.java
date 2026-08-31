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
    public ListNode mergeKLists(ListNode[] lists) {
        ArrayList<Integer> nums = new ArrayList<>();

        for (ListNode head: lists){

            while(head != null){
                nums.add(head.val);
                head = head.next;
            }

        }

        Collections.sort(nums);

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;
        for (int num : nums){
            curr.next = new ListNode(num);
            curr = curr.next;
    }

        return dummy.next;
    }
}