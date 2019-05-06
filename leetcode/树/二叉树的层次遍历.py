'''
给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        list1 = []
        list2 = []
        list3 = []
        res = []
        if root:
            list1.append(root)
            res.append([root.val])
        while len(list1)!=0:
            for root in list1:
                if root.left:
                    list2.append(root.left)
                    list3.append(root.left.val)
                if root.right:
                    list2.append(root.right)
                    list3.append(root.right.val)
            if len(list3)!=0:
                res.append(list3)
            list1 = list2
            list2 = []
            list3 = []
        return res
