# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        carry = 1
        tmp = head
        stk = []
        while tmp is not None:
            stk.append(tmp)
            tmp = tmp.next
        while carry == 1 and len(stk) > 0:
            cur_node = stk.pop()
            if cur_node.val == 9:
                cur_node.val = 0
            else:
                cur_node.val += 1
                carry = 0
        if carry == 1:
            new_head = ListNode(1)
            new_head.next = head
            head = new_head
        return head