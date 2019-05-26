'''
给定一个二叉搜索树（Binary Search Tree），把它转换成为累加树（Greater Tree)，使得每个节点的值是原来的节点值加上所有大于它的节点值之和。

例如：

输入: 二叉搜索树:
              5
            /   \
           2     13

输出: 转换为累加树:
             18
            /   \
          20     13
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    per = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        self.convertBST(root.right)
        root.val+=self.per
        self.per = root.val
        self.convertBST(root.left)
        return root
#本来我的做法是：遍历每个节点，遍历的同时把该树中所有的值大于它的节点保存到数组中，完了之后再遍历一遍树，把原来树的值替换成数组的值，但最后超时了
#不超时的方法是反向中序遍历，按照右->根->左的顺序遍历
