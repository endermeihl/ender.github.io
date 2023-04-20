# leetcode 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = ListNode()
        fast.next=head
        slow = fast
        res=fast
        while n!=0:
            fast=fast.next
            n-=1
        while fast.next!=None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        return res.next  