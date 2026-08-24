# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      cur= root
      q=collections.deque()
      q.append(cur)
      count=0
      while q:
        while cur:
            q.append(cur)
            cur=cur.left
        node= q.pop()

        if count<k:
            count+=1
            val=node.val
        
        if node.right:
            cur=node.right
        
        if count== k:
            return val
      return val 