'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        temp = res
        tempsum = 0
        while True:
            #这样做可以避免链表长度不一的问题
            if l1:
                tempsum = l1.val + tempsum
                l1 = l1.next
            if l2:
                tempsum = tempsum + l2.val
                l2 = l2.next
            temp.val = tempsum % 10
            #取十位，如果是0，并且两个链表都是空的，跳出循环，结束
            tempsum = int(tempsum / 10)
            if not l1 and not l2 and tempsum == 0:
                break
            #把生成节点放在最后，如果有进位的话方便处理
            temp.next = ListNode(0)
            temp = temp.next
        return res
#------------------------------下面是自己写的----------------------------------------------
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l2 and l1:
            return l1
        if not l1 and l2:
            return l2
        a = ListNode(0)
        head = a
        temp = 0
        while l1 and l2:
            temp = l1.val+l2.val+temp
            if temp >= 10:
                b = ListNode(int(temp % 10))
                temp = int(temp/10)
            else:
                b = ListNode(temp)
                temp = 0
            a.next = b
            a = a.next
            l1 = l1.next
            l2 = l2.next
        if not l2 and l1:
            while l1:
                temp = l1.val+temp
                if temp >= 10:
                    b = ListNode(int(temp % 10))
                    temp = int(temp/10)
                else:
                    b = ListNode(temp)
                    temp = 0
                a.next = b
                a = a.next   
                l1 = l1.next
            if temp != 0:
                b = ListNode(int(temp))
                a.next = b
        if not l1 and l2:
            while l2:
                temp = l2.val+temp
                if temp >= 10:
                    b = ListNode(int(temp % 10))
                    temp = int(temp/10)
                else:
                    b = ListNode(temp)
                    temp = 0
                a.next = b
                a = a.next   
                l2 = l2.next
            if temp != 0:
                b = ListNode(int(temp))
                a.next = b
        if not l2 and not l1:
            if temp!=0:
                a.next = ListNode(int(temp))
        return head.next
