class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        # Step 1: Find the middle of the linked list
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse the second half
        prev = None

        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # Step 3: Compare both halves
        while prev:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next

        return True