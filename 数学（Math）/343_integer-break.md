### 343.整数拆分（中等）

给定一个正整数 n，将其拆分为至少两个正整数的和，并使这些整数的乘积最大化。 返回你可以获得的最大乘积。

示例 1:

输入: 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
示例  2:

输入: 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
说明: 你可以假设 n 不小于 2 且不大于 58。

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数学（Math）  # 动态规划（DP）
```

#### 提交

```py
# Python3
class Solution:
    def integerBreak(self, n: int) -> int:
        ans = 0
        # 拆分成 i 份
        for i in range(2, n + 1):
            # 每份的份额为 share
            share = n // i
            # 总共多余的部分 extra
            extra = n % i
            # 有 extra 份额外加 1，剩下的 i-extra 份仍然保持原有份额 share
            tmp = (share + 1)**extra*share**(i - extra)
            ans = max(ans, tmp)
        return ans

```

#### 参考

##### 方法一：数学推导

**解题思路**

- 设将整数 n 拆分为 a 个小数字：

```text
n = n_1 + n_2 + ... + n_a
```

- 本题等价于求解：

```text
max(n_1 ✖ n_2 ✖ ... ✖ n_a)
```

> 以下数学推导总体分为两步：① 当所有拆分出的数字相等时，乘积最大。② 最优拆分数字为 3 。

**数学推导**

- 以下公式为“算术几何均值不等式” ，等号当且仅当 n_1 = n_2 = ... = n_a 时成立。

```text
(n_1 + n_2 + ... + n_a) / a ≥ a √ {n_1 n_2 ... n_a}
```

> 推论一： 若拆分的数量 a 确定， 则 各拆分数字相等时 ，乘积最大。

- 设将数字以因子 x 等分为 a 个，即 n = ax ，则乘积为 x^a 。观察以下公式，由于 n 为常数，因此当 x^{1/x} 取最大值时， 乘积达到最大值。

```text
x^a = x^{n/x} = (x^{1/x})^n
```

- 根据分析，可将问题转化为求 y = x^{1/x} 的极大值，因此对 x 求导数。

```text
lny = (1/x) ln x                   取对数
(1/y) y1 = 1/x^2 - (1/x^2) ln x    对 x 求导
         = (1 - ln x)/x^2
    y1 = {(1 - ln x)/x^2} x^{1/x}  整理得
```

- 令 y1 = 0 ，则 1 - ln x = 0 ，易得驻点为 x_0 = e ≈ 2.7；根据以下公式，可知 x_0 为极大值点。

```text
    >0, x∈[−∞,e)
y1 {
    <0, x∈(e,∞]
```

- 由于因子 x 必须为整数，最接近 e 的整数为 2 或 3 。如下式所示，代入 x = 2 和 x = 3 ，得出 x = 3 时，乘积达到最大。

```text
y(3) = 3^{1/3} ≈ 1.44
y(2) = 2^{1/2} ≈ 1.41
```

- 口算对比方法：给两数字同时取 6 次方，再对比。

```text
[y(3)]^6 = (3^{1/3})^6 = 9
[y(2)]^6 = (2^{1/2})^6 = 8
```

> 推论二： 将数字 n 尽可能以因子 3 等分时，乘积最大。

**拆分规则**

1. 最优： 3 。把数字 n 可能拆为多个因子 3 ，余数可能为 0, 1, 2 三种情况。
2. 次优： 2 。若余数为 2 ；则保留，不再拆为 1+1 。
3. 最差： 1 。若余数为 1 ；则应把一份 3 + 1 替换为 2 + 2，因为 2 ✖ 2 > 3 ✖ 1。

**算法流程**

1. 当 n ≤ 3 时，按照规则应不拆分，但由于题目要求必须拆分，因此必须拆出一个因子 1 ，即返回 n - 1 。
2. 当 n > 3 时，求 n 除以 3 的 整数部分 a 和 余数部分 b （即 n = 3a + b ），并分为以下三种情况：
   - 当 b = 0 时，直接返回 3^a；
   - 当 b = 1 时，要将一个 1 + 3 转换为 2 + 2，因此返回 3^{a-1} ✖ 4；
   - 当 b = 2 时，返回 3^a ✖ 2。

![数学推导](https://pic.leetcode-cn.com/1d32896766463a7a74ffafe47e7f57008e563b8fe7a8e4d52525732ac8d34275-Picture2.png)

**代码**

> Python 中常见有三种幂计算函数： \* 和 pow() 的时间复杂度均为 O(log a)；而 math.pow() 始终调用 C 库的 pow() 函数，其执行浮点取幂，时间复杂度为 O(1)。

```py
# Python3
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = n // 3, n % 3
        if b == 0: return int(math.pow(3, a))
        if b == 1: return int(math.pow(3, a - 1) * 4)
        return int(math.pow(3, a) * 2)
```

```java
// Java
class Solution {
    public int integerBreak(int n) {
        if(n <= 3) return n - 1;
        int a = n / 3, b = n % 3;
        if(b == 0) return (int)Math.pow(3, a);
        if(b == 1) return (int)Math.pow(3, a - 1) * 4;
        return (int)Math.pow(3, a) * 2;
    }
}
```

**复杂度分析**

- 时间复杂度 O(1)：仅有求整、求余、次方运算。
  - 求整和求余运算：查阅资料，提到不超过机器数的整数可以看作是 O(1)；
  - 幂运算：查阅资料，提到浮点取幂为 O(1) 。
- 空间复杂度 O(1)：a 和 b 使用常数大小额外空间。

**注**
作者：jyd
链接：https://leetcode-cn.com/problems/integer-break/solution/343-zheng-shu-chai-fen-tan-xin-by-jyd/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

##### 方法二：动态规划

对于的正整数 n，当 n ≥ 2 时，可以拆分成至少两个正整数的和。令 k 是拆分出的第一个正整数，则剩下的部分是 n - k，n - k 可以不继续拆分，或者继续拆分成至少两个正整数的和。由于每个正整数对应的最大乘积取决于比它小的正整数对应的最大乘积，因此可以使用动态规划求解。

创建数组 dp，其中 dp[i] 表示将正整数 i 拆分成至少两个正整数的和之后，这些正整数的最大乘积。特别地，0 不是正整数，1 是最小的正整数，0 和 1 都不能拆分，因此 dp[0] = dp[1] = 0。

当 i ≥ 2 时，假设对正整数 i 拆分出的第一个正整数是 j(1 ≤ j < i)，则有以下两种方案：

- 将 i 拆分成 j 和 i - j 的和，且 i - j 不再拆分成多个正整数，此时的乘积是 j ✖ (i-j)；

- 将 i 拆分成 j 和 i-j 的和，且 i-j 继续拆分成多个正整数，此时的乘积是 j ✖ dp[i − j]。

因此，当 j 固定时，有 dp[i] = max(j × (i − j), j × dp[i − j])。由于 j 的取值范围是 1 到 i - 1，需要遍历所有的 j 得到 dp[i] 的最大值，因此可以得到状态转移方程如下：

```text
dp[i] = max{max(j × (i − j), j × dp[i − j])}
        1≤j<i
```

最终得到 dp[n] 的值即为将正整数 n 拆分成至少两个正整数的和之后，这些正整数的最大乘积。

```py
# Python3
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]
```

```c++
// C++
class Solution {
public:
    int integerBreak(int n) {
        vector <int> dp(n + 1);
        for (int i = 2; i <= n; i++) {
            int curMax = 0;
            for (int j = 1; j < i; j++) {
                curMax = max(curMax, max(j * (i - j), j * dp[i - j]));
            }
            dp[i] = curMax;
        }
        return dp[n];
    }
};
```

```java
// Java
class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n + 1];
        for (int i = 2; i <= n; i++) {
            int curMax = 0;
            for (int j = 1; j < i; j++) {
                curMax = Math.max(curMax, Math.max(j * (i - j), j * dp[i - j]));
            }
            dp[i] = curMax;
        }
        return dp[n];
    }
}
```

```golang
// Golang
func integerBreak(n int) int {
    dp := make([]int, n + 1)
    for i := 2; i <= n; i++ {
        curMax := 0
        for j := 1; j < i; j++ {
            curMax = max(curMax, max(j * (i - j), j * dp[i - j]))
        }
        dp[i] = curMax
    }
    return dp[n]
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
```

```c
// C
int integerBreak(int n) {
    int dp[n + 1];
    memset(dp, 0, sizeof(dp));
    for (int i = 2; i <= n; i++) {
        int curMax = 0;
        for (int j = 1; j < i; j++) {
            curMax = fmax(curMax, fmax(j * (i - j), j * dp[i - j]));
        }
        dp[i] = curMax;
    }
    return dp[n];
}
```

**复杂度分析**

- 时间复杂度：O(n^2)，其中 n 是给定的正整数。对于从 2 到 n 的每一个整数都要计算对应的 dp 值，计算一个整数对应的 dp 值需要 O(n) 的时间复杂度，因此总时间复杂度是 O(n^2)。

- 空间复杂度：O(n)，其中 n 是给定的正整数。创建一个数组 dp，其长度为 n + 1。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/integer-break/solution/zheng-shu-chai-fen-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
