
class TreeNode:
    def __init(self,val=0,left=None,right=None):
        self.val=0
        self.left=left
        self.right=right

class Solution:

    def preorderTraversal(self, root: TreeNode):
        output=[]
        self.pre_bfs(root,output)
        return output

    def pre_bfs(self,node:TreeNode, output:List[int]):
        if node:
            output.append(node.val)
            self.pre_bfs(node.left,ouput)
            self.pre_bfs(node.right,output)

        return None
