class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = headA
        b = headB

        while a != b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        return a 