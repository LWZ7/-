给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = head
        for i in range(n):
            p = p.next
        p1 = head
        if not p:
            head = head.next
            return head
        while p.next:
            p = p.next
            p1 = p1.next
        p2 = p1.next
        p1.next = p2.next
        p2.next = None
        return head
