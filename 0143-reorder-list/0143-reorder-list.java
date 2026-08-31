class Solution {
    public void reorderList(ListNode head) {

        if (head == null || head.next == null) {
            return;
        }

        List<ListNode> list = new ArrayList<>();

        ListNode curr = head;

        while (curr != null) {
            list.add(curr);
            curr = curr.next;
        }

        int left = 0;
        int right = list.size() - 1;

        while (left < right) {

            list.get(left).next = list.get(right);
            left++;

            if (left == right) {
                break;
            }

            list.get(right).next = list.get(left);
            right--;
        }

        list.get(left).next = null;
    }
}