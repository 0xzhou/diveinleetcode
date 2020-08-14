### Binary Tree

#### Traverse A Tree

**前序遍历**(pre-order)

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



**中序遍历**(inorder)

对于*二叉搜索树*，中序遍历可以得到升序数组。

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

因为先访问登记的不是root, 故先将stack初始化为空

```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack,result=[],[]
        while root or stack:
            if root:
                stack.append(root)
                root=root.left
            
            else:
                root=stack.pop()
                result.append(root.val)
                root=root.right
        return result
```

**后序遍历(postorder)**

Post-order is widely used in mathematical expression. If you handle this tree in postorder, you can easily handle the expression using a stack. Each time when you meet a operator, you can just pop 2 elements from the stack, calculate the result and push the result back into the stack.

​	1.递归法

同之前的方法思路一样，改变一下访问节点值的顺序

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        self.dfs(root, result)
        return result
        
    def dfs(self, node:TreeNode, result: List[int]):
        if node:
            self.dfs(node.left,result)
            self.dfs(node.right,result)
            result.append(node.val)
```

2. 迭代法

后序遍历的迭代法会复杂一些，需要添加一个`visited`变量来标记是否将当前节点的左子树，右子树添加进了stack

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        result, stack= [],[(root,False)]
        
        while stack:
            node, visited=stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node,True))
                    stack.append((node.right,False))
                    stack.append((node.left,False))
        return result            
```

