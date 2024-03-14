# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Check if:
        # 1). head is empty
        # 2). val is at the head position
        # 3). current node is not null and next node is not null
        
        # # not use dummy head
        # if not head :
        #     return head
        # while head.val == val:
        #     if head.next:
        #         head = head.next
        #     else:
        #         return 
        # cur = head
        # while cur.next:
        #     if cur.next.val == val:
        #         cur.next = cur.next.next
        #     else:
        #         cur = cur.next
        # return head
    
        # use dummy head
        dummyHead = ListNode(0)
        dummyHead.next = head
        
        cur = dummyHead # not dummyHead.next, because we must know the previous Next 
                        # if we  want to delete current node
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummyHead.next
    
        
        