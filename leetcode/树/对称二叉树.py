'''
给定一个二叉树，检查它是否是镜像对称的。

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3
'''
class Solution:
    def find(self , root1 , root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (not root2 and root1) or (root1.val!=root2.val) :
            return False
        return self.find(root1.left , root2.right) and self.find(root1.right , root2.left)
        
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.find(root.left , root.right)
