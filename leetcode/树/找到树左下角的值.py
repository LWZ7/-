'''
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = -1
    high = 0
    
    def helper(self , h , root):
        if root == None:
            return 
        h+=1
        if root.left==None and root.right==None:
            if h>self.high:
                self.res = root.val
                self.high = h
            return

        self.helper(h , root.left)
        self.helper(h , root.right)
        
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.helper(0 , root)
        return self.res
