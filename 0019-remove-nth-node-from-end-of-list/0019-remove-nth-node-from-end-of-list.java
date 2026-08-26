class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {

        int length = 0;
        ListNode curr = head;

        // Find length
        while (curr != null) {
            length++;
            curr = curr.next;
        }
        int pos = length - n;
        if (pos == 0) {
            return head.next;
        }

        curr = head;

        for (int i = 1; i < pos; i++) {
            curr = curr.next;
        }

        curr.next = curr.next.next;

        return head;
    }
}