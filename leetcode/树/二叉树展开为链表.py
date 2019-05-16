'''
给定一个二叉树，原地将它展开为链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        temp = root.right
        root.right = root.left
        root.left = None
        while(root.right):
            root = root.right
        root.right = temp
'''        
为什么用后序遍历？因为首先要看左右子树是否已经是叶子结点,递归返回之后再把树变成链表
第一步，遍历左子树
第二步，遍历右子树
第三步，把右子树保存到temp中
第六步，把左子树放到右子树上（此时左子树已经符合链表要求）
第七步，左子树为空
第八步，遍历右子树，直到右子树的叶子结点
第九步，把temp塞到右子树叶子结点的右节点上
'''
