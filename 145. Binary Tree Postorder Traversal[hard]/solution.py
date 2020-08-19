# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iteration
class Solution1:
    def postorderTraversal(self, root: TreeNode):
        
        stack, output = [(root,False)],[]
        
        while stack:
            node, visited = stack.pop()
            
            if node:
                if visited:
                    output.append(node.val)
                else:
                    # 先把node加入stack, 保证post traverse
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return output

# Recursion
class Solution2:
    def preorderTraversal(self, root: TreeNode):
        result=[]
        self.dfs(root, result)
        return result
        
    def dfs(self, node:TreeNode, result: List[int]):
        if node:
            self.dfs(node.left,result)
            self.dfs(node.right,result)
            result.append(node.val)