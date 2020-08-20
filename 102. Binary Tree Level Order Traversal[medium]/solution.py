# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def levelOrder(self, root):
        levels = []

        def helper(node, level):
            if node:

                if len(levels) == level: # 为当前层创建新的存储空间
                    levels.append([])

                levels[level].append(node.val)
                helper(node.left, level+1)
                helper(node.right, level+1)

        helper(root, 0)
        return levels


class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return root
        
        res=[]
        queue=deque([root])
        
        while queue:
            level=[]
            num=len(queue)
            
            for _ in range(num):
                node=queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
            res.append(level)
        return res