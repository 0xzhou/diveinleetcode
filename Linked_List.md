### Introduction

Each node in a singly-linked list contains not only the value but also `a reference field` to link to the next node.

In most cases, we will use the `head` node (the first node) to represent the whole list.

*hint*: (这是重点和值得思考的地方)

* drawback compared with array: It takes us `O(N)` time on average to `visit an element by index`
* ad: `insert` and `delete` operations in next, you will realize the benefit of the linked list.



#### Add Operation

add a new node `cur` after given node `prev`:

1. Link the "next" field of `cur` to prev's `next node`
2. Link the "next" field of `prev` to `cur`

链表的优势：

Unlike an array, we don’t need to move all elements past the inserted element. Therefore, you can insert a new node into a linked list in `O(1)` time complexity, which is **very efficient**.



add a new node at beginning `head`:

1. Link the new node `cur` to our original head node `head`

2. Assign `cur` to `head`

   

####  Delete Operation

原理很简单：

1. Find cur's previous node `prev` and its next node `next`;

2. Link `prev` to cur's next node `next`.

It is easy to find out `next` using the reference field of `cur`. However, we have to traverse the linked list from the head node to find out `prev` which will take `O(N)` time on average, where N is the length of the linked list. So the time complexity of deleting a node will be `O(N)`.

Space complexity: O(1).





### Reverse Linked List

算法思路：

1. 将`head`的下一个node移动到`head`前
2. 再把`head`的next node移动到**最前**
3. 直到`head`的next为None

time complexity: $O(n)$

space complexity: $O(1)$



**Details of Algorithm:**

keep track of two node: 

* `the original head node`	
* `the new head node`

We use two pointers in one linked list at the same time.  One pointer `head` always points at out original head node, and `curHead` always points at our newest head node.

See the example:

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/15/screen-shot-2018-04-14-at-181603.png)

1. use `p` to indicate the next node of the `head` node, link the `head` to the "next" field of `p`

![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/14/screen-shot-2018-04-14-at-182301.png)

2. Then, we link the "next" field of `p` to the `curHead`

3. Now, out linked list actually looks like the picture below, and we set `curHead` to be `p`

   ![img](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/15/screen-shot-2018-04-14-at-182507.png)

