
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val= val
        self.left=left
        self.right= right 

def maxDepth(self, root):

    if not root:
        return 0

    else:
        left_height=self.maxDepth(root.left)
        right_height=self.maxDepth(root.right)
    return max(left_height, right_height) + 1 