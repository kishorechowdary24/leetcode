class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        // Reverse both lists
        l1 = reverse(l1);
        l2 = reverse(l2);

        int carry = 0;

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        // Add the two numbers
        while (l1 != null || l2 != null || carry != 0) {

            int sum = carry;

            if (l1 != null) {
                sum += l1.val;
                l1 = l1.next;
            }

            if (l2 != null) {
                sum += l2.val;
                l2 = l2.next;
            }

            carry = sum / 10;

            curr.next = new ListNode(sum % 10);
            curr = curr.next;
        }

        return reverse(dummy.next);
    }

    private ListNode reverse(ListNode head) {

        ListNode prev = null;
        ListNode curr = head;

        while (curr != null) {

            ListNode next = curr.next;

            curr.next = prev;
            prev = curr;
            curr = next;
        }

        return prev;
    }
}