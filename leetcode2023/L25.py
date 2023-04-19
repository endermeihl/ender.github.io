class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        tail = dummy
        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            head = pre.next
            while pre.next != tail:
                cur = pre.next
                pre.next = cur.next
                cur.next = tail.next
                tail.next = cur
            pre = head
            tail = head
        return dummy.next

