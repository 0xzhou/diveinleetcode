# collections 之 deque()

`deque()`是类似列表(list)的容器，可以实现在两端快速添加(append)和弹出(pop)元素。从两段都可以，大概开销均为O(1)。

尽管在`list`数据结构中也能实现相同操作，例如进行pop(0) 和 insert(0, val) 操作，则要引起O(n) 内存移动的操作。

`deque()`的缺点是，当支持成员检测运算符in 或者下标引用功能时，访问中间的元素会低至O(n)，这时应用`list`结构。

1. 使用可迭代的对象新建`deque`结构

```python
import collections
d=collections.deque('ghi')
for elem in d:
    print(elem.upper())
```

输出为：

```python
G
H
I
```

2. 将`deque()`对象进行旋转

```python
>>> d.extend('jkl')                  # add multiple elements at once
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])
>>> d.rotate(1)                      # right rotation
>>> d
deque(['j', 'k', 'l', 'g', 'h', 'i'])
>>> d.rotate(-1)                     # left rotation
>>> d
deque(['g', 'h', 'i', 'j', 'k', 'l'])

```



