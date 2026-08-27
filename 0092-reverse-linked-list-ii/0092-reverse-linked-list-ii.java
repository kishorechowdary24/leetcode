class Solution {
    public ListNode reverseBetween(ListNode head, int left, int right) {

        if (left == right) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;

        ListNode prevLeft = dummy;

        // Move to the node before left
        for (int i = 1; i < left; i++) {
            prevLeft = prevLeft.next;
        }

        // Start reversing
        ListNode curr = prevLeft.next;
        ListNode prev = null;

        for (int i = 0; i < right - left + 1; i++) {

            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // Connect the reversed portion
        ListNode leftNode = prevLeft.next;

        prevLeft.next = prev;
        leftNode.next = curr;

        return dummy.next;
    }
}