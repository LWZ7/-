'''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = ListNode(0)
        head = p
        if not l1 and not l2:
            return None
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2
        while l1 and l2:
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l2:
            p.next = l2
        if l1:
            p.next = l1
        return head.next
    
    def helper(self, lists: List[ListNode]) -> ListNode:
        a = len(lists)
        if a==1:
            return lists[0]
        else:
            a_left = self.helper(lists[0:int(a/2)])
            a_right = self.helper(lists[int(a/2):])
            head = self.mergeTwoLists(a_left , a_right)
            return head
            
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists)==0:
            return None
        head = self.helper(lists)
        return head
  '''
  通过递归树分析，算法的时间复杂度是（K-1)*log K + K
  '''
