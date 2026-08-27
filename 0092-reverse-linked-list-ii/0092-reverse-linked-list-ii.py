class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prevleft = dummy

        for _ in range(1, left):
            prevleft = prevleft.next

        curr = prevleft.next
        prev = None

        for _ in range(right - left + 1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        leftNode = prevleft.next

        prevleft.next = prev

        leftNode.next = curr

        return dummy.next