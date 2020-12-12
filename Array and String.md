### Array and String

#### Intro

`Array` is one of the fundamental blocks in data structure. Since a `string` is just formed by an array of characters(字符), they are both similar. Most interview questions fall into this category.

In this card, we will introduce array and string. After finishing this card, you should:

1. Understand the differences between `array` and `dynamic array`;
2. Be familiar with `basic operations` in the array and dynamic array;
3. Understand `multidimensional arrays` and be able to use a `two-dimensional array`;
4. Understand the concept of `string` and the different features string has;
5. Be able to apply the `two-pointer technique` to practical problems.

#### Array

is basic data structure **to store a collection of elements sequentially**. Elements can be accessed randomly and identified by **index**.

##### Dynamic Array

As we mentioned in the previous article, an array has **a fixed capacity** and we need to specify the size of the array when we initialize it.

Therefore, most programming languages offer **built-in** dynamic array which is still a **random access list data structure but with variable size** . For example, we have `vector` in C++ and `ArrayList` in Java.

##### 724. Find Pivot Index - Easy

#### 2D Array

In some languages, the multidimensional array is actually `implemented internally as a one-dimensional array` while in some other languages, there is `actually no multidimensional array` at all.

**1. C++ stores the two-dimensional array as a one-dimensional array.**

<img src="https://raw.githubusercontent.com/Mingy2018/Markdown-photoes/master/img/20201031230932.png"/>

`A[i][j] = A[i*N + j]`

**2. In Java, the two-dimensional array is actually a one-dimensional array which contains M elements, each of which is an array of N integers.**

<img src="https://raw.githubusercontent.com/Mingy2018/Markdown-photoes/master/img/20201031231004.png"/>

##### 498. Diagonal Traverse - Medium 

- [x] 

##### 54. Spiral Matrix - Medium

##### 118. Pascal's Triangle - Easy

性质：

- 第 `n` 层有 `n` 个元素

思路: 

把`num_rows`作为迭代器的上届，`rows`从 `index:0` 到 `index:num_rows-1` 构建 `num_rows`层；

每层有`rows+1`个 元素第一个元素(`index:0`)和最后一个元素(`index:row`)为`1`, 从第二个元素(`index:1`)至倒数第二个数(`index:row-1`)由上一层推导得出。



```c++
class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int>> r(numRows);

        for (int i = 0; i <numRows; i++) {
            r[i].resize(i + 1);
            r[i][0] = r[i][i] = 1;
  
            for (int j = 1; j <= i-1; j++) # for i >1, 第三层时
                r[i][j] = r[i - 1][j - 1] + r[i - 1][j];
        }     
        return r;
    }
};
```

#### String

**String** is an array of `characters`,  string concatenation: slow in Jave, since string in Java is immutable

##### 67. Add Binary





