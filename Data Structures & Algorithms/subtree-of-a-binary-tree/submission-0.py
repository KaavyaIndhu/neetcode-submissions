# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: TreeNode, subRoot:TreeNode) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root,subRoot):
            return True
        a=self.isSubtree(root.left,subRoot)
        b=self.isSubtree(root.right,subRoot)
        return a or b

    def sameTree(self, root:TreeNode ,subRoot:TreeNode)->bool:
            if not root and not subRoot:
                return True
            if root and subRoot and (root.val==subRoot.val):
                a=self.sameTree(root.left,subRoot.left)
                b=self.sameTree(root.right,subRoot.right)
                return a and b
            else:
                return False
        