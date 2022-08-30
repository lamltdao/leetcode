Put all nodes to a stack. Init carry = 1
```
While carry = 1:
> pop node from stack.
> inc node.val by 1. if node.val = 9, node.val = 0. otherwise, carry = 0
if carry = 1 # still carry 1 after inc all current nodes, cases like 99, 999, ...
new_head = Node(1)
new_head.next = head
head = new_head
return head
```