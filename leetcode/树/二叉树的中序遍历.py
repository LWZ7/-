'''
给定一个二叉树，返回它的中序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,3,2]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        list1 = []
        if not root:
            return res
        
        while root or len(list1)>0:
            if root:
                list1.append(root)
                root = root.left
            else:
                root = list1.pop()
                res.append(root.val)
                root = root.right
        return res
#需要两个list，一个作为栈使用，另一个保存遍历结果。
#如果不用两个栈的话循环无法退出
#如果是空节点，就从栈里面弹出父节点，然后看它有没有右节点
