# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        count = 0
        while current and count < k:
            current = current.next
            count +=1

        if count < k: # 剩餘節點數
            return head
        
        prev = None
        current = head

        for _ in range(k):
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        head.next = self.reverseKGroup(current,k) # reverse 後 tail 變成 head
        return prev # 新的 head
            

            
