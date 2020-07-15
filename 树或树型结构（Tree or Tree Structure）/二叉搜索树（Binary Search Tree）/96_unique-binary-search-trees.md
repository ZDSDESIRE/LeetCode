### 96. 不同的二叉搜索树（中等）

给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

```text
输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 二叉树搜索（Binary Tree Search）  # 动态规划（DP）
```

#### 提交

```py
# Python3
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]
```

#### 参考

##### 方法一：动态规划

**思路**

给定一个有序序列 1 ⋯ n，为了构建出一棵二叉搜索树，我们可以遍历每个数字 i，将该数字作为树根，将 1 ⋯ (i − 1) 序列作为左子树，将 (i + 1) ⋯ n 序列作为右子树。接着我们可以按照同样的方式递归构建左子树和右子树。

在上述构建的过程中，由于根的值不同，因此我们能保证每棵二叉搜索树是唯一的。

由此可见，原问题可以分解成规模较小的两个子问题，且子问题的解可以复用。因此，我们可以想到使用动态规划来求解本题。

**算法**

题目要求是计算不同二叉搜索树的个数。为此，我们可以定义两个函数：

- G(n): 长度为 n 的序列能构成的不同二叉搜索树的个数。

- F(i, n): 以 i 为根、序列长度为 n 的不同二叉搜索树个数 (1 ≤ i ≤ n)。

可见，G(n) 是我们求解需要的函数。

稍后我们将看到，G(n) 可以从 F(i, n) 得到，而 F(i, n) 又会递归地依赖于 G(n)。

首先，根据上一节中的思路，不同的二叉搜索树的总数 G(n)，是对遍历所有 i (1 ≤ i ≤ n) 的 F(i, n) 之和。换言之：

```text
      n
G(n)= ∑ F(i, n)    (1)
      i=1
```

对于边界情况，当序列长度为 1（只有根）或为 0（空树）时，只有一种情况，即：

```text
G(0)=1, G(1)=1
```

给定序列 1 ⋯ n，我们选择数字 i 作为根，则根为 i 的所有二叉搜索树的集合是左子树集合和右子树集合的笛卡尔积，对于笛卡尔积中的每个元素，加上根节点之后形成完整的二叉搜索树，如下图所示：

![dp](https://assets.leetcode-cn.com/solution-static/96/96_fig1.png)

举例而言，创建以 3 为根、长度为 7 的不同二叉搜索树，整个序列是 [1, 2, 3, 4, 5, 6, 7]，我们需要从左子序列 [1, 2] 构建左子树，从右子序列 [4, 5, 6, 7] 构建右子树，然后将它们组合（即笛卡尔积）。

对于这个例子，不同二叉搜索树的个数为 F(3, 7)。我们将 [1,2] 构建不同左子树的数量表示为 G(2), 从 [4, 5, 6, 7] 构建不同右子树的数量表示为 G(4)，注意到 G(n) 和序列的内容无关，只和序列的长度有关。于是，F(3,7) = G(2) ⋅ G(4)。 因此，我们可以得到以下公式：

```text
F(i, n) = G(i − 1) ⋅ G(n − i)       (2)
```

将公式 (1)，(2) 结合，可以得到 G(n) 的递归表达式：

```text
      n
G(n)= ∑ G(i − 1) ⋅ G(n − i)         (3)
      i=1
```

至此，我们从小到大计算 G 函数即可，因为 G(n)的值依赖于 G(0) ⋯ G(n − 1)。

```py
# Python
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G = [0]*(n+1)
        G[0], G[1] = 1, 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                G[i] += G[j-1] * G[i-j]

        return G[n]
```

```c++
// C++
class Solution {
public:
    int numTrees(int n) {
        vector<int> G(n + 1, 0);
        G[0] = 1;
        G[1] = 1;

        for (int i = 2; i <= n; ++i) {
            for (int j = 1; j <= i; ++j) {
                G[i] += G[j - 1] * G[i - j];
            }
        }
        return G[n];
    }
};
```

```java
// Java
class Solution {
    public int numTrees(int n) {
        int[] G = new int[n + 1];
        G[0] = 1;
        G[1] = 1;

        for (int i = 2; i <= n; ++i) {
            for (int j = 1; j <= i; ++j) {
                G[i] += G[j - 1] * G[i - j];
            }
        }
        return G[n];
    }
}
```

```js
// JavaScript
var numTrees = function (n) {
  const G = new Array(n + 1).fill(0)
  G[0] = 1
  G[1] = 1

  for (let i = 2; i <= n; ++i) {
    for (let j = 1; j <= i; ++j) {
      G[i] += G[j - 1] * G[i - j]
    }
  }
  return G[n]
}
```

```golang
// Golang
func numTrees(n int) int {
    G := make([]int, n + 1)
    G[0], G[1] = 1, 1
    for i := 2; i <= n; i++ {
        for j := 1; j <= i; j++ {
            G[i] += G[j-1] * G[i-j]
        }
    }
    return G[n]
}
```

```c
// C
int numTrees(int n) {
    int G[n + 1];
    memset(G, 0, sizeof(G));
    G[0] = G[1] = 1;
    for (int i = 2; i <= n; ++i) {
        for (int j = 1; j <= i; ++j) {
            G[i] += G[j - 1] * G[i - j];
        }
    }
    return G[n];
}
```

**复杂度分析**

- 时间复杂度 : O(n^2)，其中 n 表示二叉搜索树的节点个数。G(n) 函数一共有 n 个值需要求解，每次求解需要 O(n) 的时间复杂度，因此总时间复杂度为 O(n^2)。

- 空间复杂度 : O(n)。我们需要 O(n) 的空间存储 G 数组。

##### 方法二：数学

**思路与算法**

事实上我们在方法一中推导出的 G(n)函数的值在数学上被称为卡塔兰数 C_n。卡塔兰数更便于计算的定义如下:

```text
C_0 = 1, C_{n+1} = {2(2n+1)}/{n+2} C_n
```

证明过程可以参考上述文献，此处不再赘述。

```py
# Python
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
```

```c++
// C++
class Solution {
public:
    int numTrees(int n) {
        long long C = 1;
        for (int i = 0; i < n; ++i) {
            C = C * 2 * (2 * i + 1) / (i + 2);
        }
        return (int)C;
    }
};
```

```java
// Java
class Solution {
    public int numTrees(int n) {
        // 提示：我们在这里需要用 long 类型防止计算过程中的溢出
        long C = 1;
        for (int i = 0; i < n; ++i) {
            C = C * 2 * (2 * i + 1) / (i + 2);
        }
        return (int) C;
    }
}
```

```js
// JavaScript
var numTrees = function (n) {
  let C = 1
  for (let i = 0; i < n; ++i) {
    C = (C * 2 * (2 * i + 1)) / (i + 2)
  }
  return C
}
```

```golang
// Golang
func numTrees(n int) int {
    C := 1
    for i := 0; i < n; i++ {
        C = C * 2 * (2 * i + 1) / (i + 2);
    }
    return C
}
```

```c
// C
int numTrees(int n) {
    long long C = 1;
    for (int i = 0; i < n; ++i) {
        C = C * 2 * (2 * i + 1) / (i + 2);
    }
    return (int)C;
}
```

**复杂度分析**

- 时间复杂度 : O(n)，其中 n 表示二叉搜索树的节点个数。我们只需要循环遍历一次即可。
- 空间复杂度 : O(1)。我们只需要常数空间存放若干变量。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
