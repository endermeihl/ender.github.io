# Problem: 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        temp = ListNode()
        temp.next = head
        res = temp
        res.next = head
        while temp.next!=None and temp.next.next!=None:
            temp1 = temp.next
            temp2 = temp.next.next
            temp.next = temp2
            temp1.next = temp2.next
            temp2.next = temp1
            temp = temp.next.next
        return res.next