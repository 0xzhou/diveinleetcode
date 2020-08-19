# Definition for a binary tree node.
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
                if len(levels) == level:
                    levels.append([])
                levels[level].append(node.val)
                helper(node.left, level+1)
                helper(node.right, level+1)

        helper(root, 0)
        return levels

class Solution2:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        levels=[]
        
        if not root:
            return levels
        
        level=0
        queue=deque([root,])
        while queue:
            levels.append([])
            level_length=len(queue)
            
            for i in range(level_length):
                node= queue.popleft()
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)         
            level+=1
            
        return levels