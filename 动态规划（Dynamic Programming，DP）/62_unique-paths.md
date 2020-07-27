### 62.不同路径（中等）

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？
![不同路径](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/robot_maze.png)
例如，上图是一个 7 x 3 的网格。有多少可能的路径？

示例  1:

```text
输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
```

示例  2:

```text
输入: m = 7, n = 3
输出: 28
```

提示：

- 1 <= m, n <= 100
- 题目数据保证答案小于等于 2 \* 10 ^ 9

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数组（Array）  # 动态规划（DP）
```

**相似题目**
[63.不同路径 II（中等）](https://leetcode-cn.com/problems/unique-paths-ii)
[64.最小路径和（中等）](https://leetcode-cn.com/problems/minimum-path-sum/)

#### 提交

```py
# Python3
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        f = [0 for _ in range(m)]
        f[0] = 1
        for i in range(0,n):
            for j in range(1,m):
                f[j] += f[j-1]
        return f[m-1]
```

#### 参考

##### 数学法

其实，本道题在排列组合问题中可化为求 C(m+n-2, m-1)（或 C(m+n-2, n-1)）。
即一共有 m 行 n 列，其中需要向下走 m - 1 步，向右走 n - 1 步，一共走 m + n - 2 步。所以就是在 m + n - 2 步中选出哪 m-1 步是向下走的，其余自动为向右走的步数。
TIPS：
本方法要注意计算组合数的时候要先化简，且要用 unsigned long long/double 来表示，否则会超过范围。

```c++
// C++
class Solution {
public:
int uniquePaths(int m, int n) {
    if (m == 1 || n == 1)
        return 1;
    if (m > n)
        swap(m, n); // 保证 m <= n
    // 计算阶乘：不用调用函数，节省空间
    unsigned long long int temp = 1;
    unsigned long long int result = 1;
    for (int i = 1; i <= m-1 ; i++)
    {
        temp *= i;
    }
    for (int i = n; i <= m + n - 2; i++)
    {
        result *= i;
    }
    result = result / temp;
    return result;
}
};
```

##### 递归

其实，本题很容易想到递归。
但是，要注意是用一个数组 a 记录下已经算过的路径数，否则会超时。
TIPS：

1. 可利用对称性，将已经算过的数组单元赋值给对称位置的单元。
2. 本题的记录数组使用静态变量放在 class 外面。

```c++
// C++
static int a[101][101] = { 0 }; // 静态变量放在 class 外面（类似全局变量），并初始化。
class Solution {
public:

int uniquePaths(int m, int n) {
    if (m == 1 || n == 1)
        return 1;
    if (m == 2)
        return n;
    if (n == 2)
        return m;
    if (a[m][n] > 0) // 计算过就直接返回。
        return a[m][n];
    a[m - 1][n] = uniquePaths(m - 1, n);
    a[n][m - 1] = a[m - 1][n]; // 由于本题的对称性，可以直接复制到对称位置
    a[m][n-1] = uniquePaths(m, n - 1);
    a[n - 1][m] = a[m][n - 1]; // 由于本题的对称性，可以直接复制到对称位置
    a[m][n] = a[m - 1][n] + a[m][n-1];
    return  a[m][n]; // 递归法
}
};
```

##### 动态规划

TIPS：
本题使用了动态申请内存的数组 a 去记录已经算过的单元，但要注意内存的申请和释放。

```c++
// C++
int uniquePaths(int m, int n) {
    int **a = new int*[m + 1]; // 二维数组的动态内存申请
    for (int i = 0; i <= m ; i++)
        a[i] = new int[n + 1];
    for (int i = 1; i <= m; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (i == 1 || j == 1)
                a[i][j] = 1;
            else
                a[i][j] = a[i - 1][j] + a[i][j - 1];
        }
    }
    int temp = a[m][n];
    for (int i = 0; i <= m ; i++) // 二维数组的释放
        delete []a[i];
    delete []a;
    return  temp; // 动态规划
}
```

**解题思路**
动态规划 5 大步骤：

1.定义状态：即定义数据元素的含义，这里定义 dp[i][j]为当前位置的路径数，i 表示 i 列，j 表示 j 行

2.建立状态转移方程：因为从题目要求中可以看出，机器人只能向右或向下移动。所以到达 dp[i][j]就可能是经过 dp[i-1][j]到达，
也可能是经过 dp[i][j-1]到达。所以状态转移方程为：dp[i][j]=dp[i-1][j]+dp[i][j-1]

3.设定初始值：通过状态转移方程可以看出，i 和 j 下表要从 1 开始，否则会导致数组溢出异常。同时每一个位置点代表到达当前位置的路径条数，所以要设置最初的路径条数即 dp[i][0]=1,dp[0][j]=1，即第一行，第一列值为 1。

5.状态压缩：即优化数组空间，每次状态的更新只依赖于前一次的状态，优化一般作用于多维数组，观察是否可以将多维数组以一维数组来动态表示，即用一维数组来保存上次的状态。这道题的优化方法是存在的。具体看下面的代码解释。状态转移方程：dp[i] = dp[i-1] + dp[i]

6.选出结果：根据状态转移方程，求路径的总数，因此 dp[-1][-1]表示的是到达最后位置的路径总条数。

```py
# Python3
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 采用二位数组形式的动态规划
        # f[i][j]表示当前移动到的总次数，要求f[-1][-1]
        # 状态转移公式：f[i][j] = f[i-1][j]+f[i][j-1]
        # 初始值：每一步移动的次数可以看做横轴和纵轴的和，因此 f[i][0] = 1,f[0][j]=1
        # 运动的轨迹：要么往下，要么往左
        # 时间复杂度：O(m*n),空间复杂度：O(m*n)

        f = [[0]*n for zong in range(m)]
        for i in range(m):
            f[i][0] = 1
        for j in range(n):
            f[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                f[i][j] = f[i-1][j]+f[i][j-1]
        return f[-1][-1]


        """优化空间复杂度为O(n)"""
        # 对二维矩阵进行压缩成一位数组,将最新生成的值覆盖掉旧的值,逐行求解当前位置的最新路径条数！
        # 实质：在于动态计算并替换当前位置下的路径数最新值
        # 状态转移公式变成：f[i] = f[i-1]+f[i]
        # 初始值： f = [1]*m,取横轴
        # f[-1]表示可能路径的总数
        # 空间复杂度：O(n),时间复杂度:O(m*n)

        f = [1]*m
        for j in range(1,n):
            for i in range(1,m):
                f[i] = f[i-1]+f[i]
        return f[-1]
```
