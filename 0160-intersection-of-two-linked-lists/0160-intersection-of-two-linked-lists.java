/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        int LenA = 0;
        int LenB = 0;

        ListNode a = headA;
        ListNode b = headB;

        while (a != null){
            LenA++;
            a = a.next;
        }

        while (b != null){
            LenB++;
            b = b.next;
        }

        a = headA;
        b = headB;

        while (LenA > LenB){
            a = a.next;
            LenA--;
        }

        while (LenB > LenA){
            b = b.next;
            LenB--;
        }

        while(a != b){
            a = a.next;
            b = b.next;
        }

        return a;
        
    }
}