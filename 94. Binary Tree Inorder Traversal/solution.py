# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Iteration
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack, output= [],[]
        
        while stack or root:
            
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                output.append(root.val)
                root=root.right
        return output

# Recursion
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        output=[]
        self.dfs_inorder(root, output)
        return output

    def dfs_inorder(self, root, output):
        
        if not root:
            return 0
        else:
            self.dfs_inorder(root.left, output)
            output.append(root.val)
            self.dfs_inorder(root.right, output)
        return output