### Binary Tree

#### Traverse A Tree

##### **前序遍历**(pre-order)

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



##### **中序遍历**(inorder)

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

##### **后序遍历(postorder)**

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

##### 层遍历(Lever-order)

Level-order traversal is to traverse the tree level by level. Generally it is based on `Breadth-First Search`, typically, we use a queue to help us to do BFS.

1. 迭代法

​	利用deque结构来存储当前层的所有node，在利用for循环遍历node，保存node的值，再将node的左右子树保存起来。两种保存树结构每层数据的思路，注意体会理解。

```python
from collections import deque
class Solution:
    def levelOrder(self, root):
        if not root: return [] #base case 
        res = []
        #queue to store all the nodes
        queue = deque([root]) 

        while queue:
            level = [] #hold the values at the current level.
            for _ in range(len(queue)): 
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level_vals.append(node.val)
            res.append(level)
        return res
```

```python
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return root
     
        res = []
        queue=deque([root])
        
        while queue:
            level=len(res)
            res.append([])
            num=len(queue)
            for _ in range(num):
                node=queue.popleft()
                if node:
                    res[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return res
```

2. 递归法

将树n层结构用n层list来保存，n层list再保存在一个大的二维数组中。

递归函数输入将要访问的节点和节点层数，需要节点层数的原因是，需要定位录入二维数组中哪个的list，值得注意的是，需要先为当前层创建新的list，然后保存当前层的数据，最后再递归访问下一层。-> 保存数据 = 空间 + 保存操作

```python
class Solution:
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
```



##### **Complexity Analysis**:

The time complexity is `O(N)` because we visit each node exactly once.

And the depth of the tree might be `N` in the worst case. That is to say, the level of recursion might be at most `N` in the worst case. Therefore, taking system stack into consideration, the space complexity is `O(N)` as well. -> **stack overflow** problem



#### Solve Problems Recursively



#### Conclusion

