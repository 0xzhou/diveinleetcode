**树的前序遍历**(preorder)

[根节点， 左子树， 右子树]

1. 递归法(Recursion)

思路更加直观

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        self.dfs(root, result)
        return result
        
    def dfs(self, node:TreeNode, result: List[int]):
        if node:
            result.append(node.val)
            self.dfs(node.left,result)
            self.dfs(node.right,result)
```

2. 迭代法(Iteration)

使用stack数据结构来记录遍历顺序，使用`node`对当前正在访问的节点进行标记

```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # pre-order可以先把根节点放进stack
        stack, result= [root],[]
        # 还有未访问的节点时
        while stack:
            node=stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return result
```



**树的中序遍历**(inorder)

1. 递归法(Recursion)

根据前序遍历的思路，改一下顺序即可用

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        self.dfs(root, result)
        return result
        
    def dfs(self, node:TreeNode, result: List[int]):
        if node:
            self.dfs(node.left,result)
            result.append(node.val)
            self.dfs(node.right,result)
```

2. 迭代法(Iteration)

