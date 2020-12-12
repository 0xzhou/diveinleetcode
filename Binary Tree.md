### Binary Tree

- 144. Binary Tree Preorder Traversal - Medium 
- 94. Binary Tree Inorder Traversal - Medium 
- 145. Binary Tree Postorder Traversal - Medium 
- 102. Binary Tree Level Order Traversal - Medium
- 104. Maximum Depth of Binary Tree - Easy
- 101. Symmetric Tree - Easy
- 112. Path Sum - Easy
- 250. Count Univalue Subtrees - Medium

- 106. Construct Binary Tree from Inorder and Postorder Traversal - Medium
- 105. Construct Binary Tree from Preorder and Inorder Traversal - Medium
- 116. Populating Next Right Pointers in Each Node - Medium
- 117. Populating Next Right Pointers in Each Node II - Medium
- 236. Lowest Common Ancestor of a Binary Tree - Medium
- 297. Serialize and Deserialize Binary Tree - Hard
- 106. Construct Binary Tree from Inorder and Postorder Traversal - Medium
- 105. Construct Binary Tree from Preorder and Inorder Traversal - Medium
- 116. Populating Next Right Pointers in Each Node - Medium
- 117. Populating Next Right Pointers in Each Node II - Medium
- 236. Lowest Common Ancestor of a Binary Tree - Medium
- 297. Serialize and Deserialize Binary Tree - Hard

#### Introduction

A `Binary Tree` is one of the most typical tree structure. As the name suggests, a binary tree is a tree data structure in which each node has `at most two children`, which are referred to as the left child and the right child.

#### Traverse A Tree

理解并区别不同的遍历方法:

1. DFS: 深度优先策略可细分为**前序，中序，后序**遍历先掌握递归法，再学习迭代法
2. BFS: 最后利用`BFS`进行**层遍历**。

<img src="https://raw.githubusercontent.com/Mingy2018/Markdown-photoes/master/img/20201030194912.png"/>

##### **前序遍历**(Preorder)

[根节点， 左子树， 右子树]

1. 递归法(Recursion)

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
                stack.append(node.right) # 后访问
                stack.append(node.left)	# 先访问
        return result
```

##### **中序遍历**(Inorder)

[左子树，根节点，右子树]

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
        # 定义空数组
        stack,result=[],[]
        while stack or root: #注意循环条件
            if root: # 先尽可能往左遍历，同时保存经过的节点
                stack.append(root)
                root=root.left
            else:
                root=stack.pop() # 回到上一节点
                result.append(root.val) 
                root=root.right # 访问上一节点的右子树
        return result
```

##### **后序遍历(Postorder)**

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
        if not root: return [] #special case 
        res = []
        #queue to store all the nodes
        queue = deque([root]) 

        while queue:
            level = [] #hold the values at the current level.
            for _ in range(len(queue)): #这里很巧妙，上轮添加多少，这轮访问多少
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node.val)
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

递归函数输入为: **访问节点**和**该节点所在层数**，需要节点层数的原因是，需要定位录入二维数组中哪个的list，值得注意的是，需要先为当前层创建新的list，然后保存当前层的数据，最后再递归访问下一层。-> 保存数据 = 空间 + 保存操作

递归函数的功能: 保存当前节点，递归下一批次节点。

```python
class Solution:
    def levelOrder(self, root):
        levels = []

        def helper(node, level):
            if node: # 先判断节点是否存在
                if len(levels) == level: # 判断是否需要新建
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

Actually, `recursion` is one of the most powerful and frequently-used methods for solving tree related problems. We are going to introduce two typical recursive solutions for solving tree-related problems.

##### "Top-down" Solution

This method can be considered as a kind of **preorder** traversal.

`top_down(root, params)`

Algorithms:

```pseudocode
1. return specific value for null node
2. update the answer if needed                      // answer <-- params
3. left_ans = top_down(root.left, left_params)      // left_params<-- root.val, params
4. right_ans = top_down(root.right, right_params)   // right_params <-- root.val, params 
5. return the answer if needed                      // answer <-- left_ans, right_ans
```

For instance, given a binary tree, find its maximum depth. 

```pseudocode
1. return if root is null
2. if root is a leaf node:
3.      answer = max(answer, depth)         // update the answer if needed
4. maximum_depth(root.left, depth + 1)      // call the function recursively for left child
5. maximum_depth(root.right, depth + 1)     // call the function recursively for right child
```

##### "Bottom-up" Solution

This can be considered as a kind of **postorder** traversal.

Algorithms:

```pseudocode
1. return specific value for null node
2. left_ans = bottom_up(root.left)          // call function recursively for left child
3. right_ans = bottom_up(root.right)        // call function recursively for right child
4. return answers                           // answer <-- left_ans, right_ans, root.val
```

Take the maximum depth as same example. If we know the maximum depth `l` of the subtree rooted at its **left** child and the maximum depth `r` of the subtree rooted at its **right** child, we can choose the maximum between them and add 1 to get the maximum depth of the subtree rooted at the current node. That is `x = max(l, r) + 1`.

```pseudocode
1. return 0 if root is null                 // return 0 for null node
2. left_depth = maximum_depth(root.left)
3. right_depth = maximum_depth(root.right)
4. return max(left_depth, right_depth) + 1  // return depth of the subtree rooted at root
```



##### Maximum Depth of Binary Tree - Easy

`maxDepth()`的意思是，返回当前节点的最深深度。利用该性质可以递归。

如果root为空，height返回0。如果为非空，递归左子树，递归右子树，将最深深度+1。

**"Bottom-up"**

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        left_height=self.maxDepth(root.left)
        right_height=self.maxDepth(root.right)
        
        return max(left_height, right_height) +1
```

**"Top-down"**

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.ans = 0
        
        def top_down(node, depth):
            self.ans = max(self.ans, depth)
            if node:
                top_down(node.left, depth+1)
                top_down(node.right, depth+1)
            else:
                return self.ans
        top_down(root, 0)
        return self.ans
```

##### Symmetric Tree - Easy

设计一个递归函数，判断思路两个Node是否对称。函数的功能是判断两个Node是否满足对称的条件：

1. node1.val == node2.val 
2. node1的左子树 , node2的右子树 是否对称

3. node1的右子树 , node2的左子树 是否对称

Recursive method

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        return self.aresymmetric(root, root)
        
    def aresymmetric(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2:
            return False
        else:
            return node1.val == node2.val \
        	and self.aresymmetric(node1.left, node2.right)\
            and self.aresymmetric(node1.right, node2.left)
```

Iterative method

```python
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        if not root: return True
        
        stack = collections.deque([(root,root)])
        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))
        return True
```

##### Path Sum - Easy

注意 leaf node 的定义，必须是 node children。

Recursive method:

```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root: return False
        
        sum -= root.val
        if not root.left and not root.right: # reach the leaf node
            return sum == 0 ##
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
```

Iterative method:

```python
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if not root:
            return False
        
        de = [(root, sum - root.val)]
        while de:
            node, cur_sum = de.pop()
            if not node.left and not node.right and cur_sum == 0:
                return True
            if node.right:
                de.append((node.right, cur_sum - node.right.val))
            if node.left:
                de.append((node.left, cur_sum - node.left.val))
        return False
```

##### Count Univalue Subtrees - Medium

Given a node in our tree, it is a univalue subtree if it meets one of the following criteria:

1. the node has no children (base case)
2. All of the node's children are univalue subtrees, and the node and its children all have the same value

Recursive method:

a kind of "bottom up" thinking

```python
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        if not root: return 0
        
        self.count = 0 #
        self.isuni(root)
        return self.count
    
    def isuni(self, node): # 判断节点是否构成univalue subtree
 						   # count在过程中计算，并不是返回值
        # 情况一: criteria 1    
        if not node.left and not node.right:
            self.count += 1
            return True
        # 情况二: criteria 2
        is_uni = True
        if node.left:
            is_uni =self.isuni(node.left) and is_uni and node.left.val == node.val 
        if node.right:
            is_uni =self.isuni(node.right) and is_uni and node.right.val == node.val     
        self.count += is_uni
        
        return is_uni # 体会function的功能，考虑返回的值
```

方法二：

```python
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
        self.count = 0
        self.is_valid_part(root, 0)
        return self.count
           
    def is_valid_part(self, node, val):
        
        if not node: return True
        
        if not all([self.is_valid_part(node.left, node.val),
                   self.is_valid_part(node.right, node.val)]):
            return False
        
        self.count += 1
        
        return node.val == val
```

#### Conclusion

##### Construct Binary Tree from Inorder and Postorder Traversal - Medium

Think it in recursive way: 

1. 首先访问后序数组`postorder`的最后一个元素，定义为根节点`root`

2. 该根节点(设下标为 `index`)将中序数组`inorder`划分为两个数组，左边的数组 `l` 构成左子树，右边 `r`构成右子树

   - `l = inorderp[0:index] `
   - `r = inorder[index+1:]`

3. 在后序数组中找出 `l`, `r` 对应的子数组

   - 与 `l` 对应的后序子数组：`postorder[0:index]`

   - 与 `r`对应的后序子数组：`postorder[index:-1]`

4. 分别构建左子树，右子树；与 `root` 关联

```python
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        if not postorder: return None
        
        root = TreeNode(postorder[-1])
        indx = inorder.index(postorder[-1])
        
        root.left = self.buildTree(inorder[0:indx], postorder[0:indx])
        root.right = self.buildTree(inorder[indx+1:], postorder[indx:-1])
        
        return root
```

 ##### Construct Binary Tree from Preorder and Inorder Traversal - Medium

Think it in recursive way: 

1. 首先访问前序数组`preorder`的第一个元素，定义为根节点`root`

2. 该根节点(设下标为 `index`)将中序数组`inorder`划分为两个数组，左边的数组 `l` 构成左子树，右边 `r`构成右子树

   - `l = inorderp[0:index] `
   - `r = inorder[index+1:]`

3. 在前序数组中找出 `l`, `r` 对应的子数组

   - 与 `l` 对应的后序子数组：`postorder[1:index+1]`

   - 与 `r`对应的后序子数组：`postorder[index+1:]`

4. 分别构建左子树，右子树；与 `root` 关联

```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        
        if not preorder: return None
        
        root = TreeNode(preorder[0])
        indx = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:indx+1],inorder[0:indx])
        root.right = self.buildTree(preorder[indx+1:], inorder[indx+1:])
        
        return root
```

##### Populating Next Right Pointers in Each Node - Medium

思路：

1. 按照层遍历对二叉树遍历
2. 对每一层的处理
   - 最后一个元素: next 为空
   - 其他节点: next 为下一个 

<img src="https://raw.githubusercontent.com/Mingy2018/Markdown-photoes/master/img/20201030213909.png"/>

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root: return None
        
        stack = collections.deque([root])
        level = 0
        while stack:
            for i in range(2**level):
                node = stack.popleft()
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                if i != (2**level-1):
                    node.next = stack[0]
            level += 1
        return root
```

##### Populating Next Right Pointers in Each Node II - Medium

<img src="https://raw.githubusercontent.com/Mingy2018/Markdown-photoes/master/img/20201030214946.png"/>

思路与上题类似，不过判断每层的节点时，用 `len(queue)`进行计算。

```python
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root: return None
        
        queue = collections.deque([root])
        
        while queue:
            num = len(queue)
            for i in range(num):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i < num-1:
                    node.next = queue[0]
        return root
```

##### Lowest Common Ancestor of a Binary Tree - Medium

限定条件:

-  all `node.val` are unique
- q != p

解法一: "Bottom up" Thinking

`lowestCommomAncestor` 功能是判断一个`node`是否是`p`, `q`的 **LCA**， 若是返回该node, 若不是返回None.

1. 若 `root` 为空，`p` 或 `q`: 直接返回 `root`
2. 判断左子树是否满足条件，判断右子树是否满足条件

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        
        return left or right
```

解法二: 

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        
        def dfs(node):
            # reach the end of a branch, return False
            if not node: 
                return False
            # left and right recursion
            left = dfs(node.left)
            right = dfs(node.right)
            # if the current node if one of p and q
            mid = node == p or node == q
            
            # if any two of three flags true -> current node is the LCA
            if mid + right + left >= 2:
                self.ans = node
            # return if either of the three is True    
            return mid or left or right
        
        dfs(root)
        return self.ans 
```

#####  Serialize and Deserialize Binary Tree - Hard

