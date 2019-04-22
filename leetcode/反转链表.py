'''
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    #迭代版
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        else:
            p1 = head
            p2 = head.next
            p1.next = None
            while p2:
                p3 = p2.next
                p2.next = p1
                p1 = p2
                p2 = p3
            return p1            
    #递归版
    def reverseList(self, head: ListNode) -> ListNode:
        return self.recursive(head)[0]
    
    def recursive(self, head):
        if not head or not head.next:
            return head, head
        head_new, last = self.recursive(head.next)
        last.next = head
        head.next = None
        return head_new, head
