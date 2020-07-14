### 837.新 21 点（中等）

爱丽丝参与一个大致基于纸牌游戏 “21 点” 规则的游戏，描述如下：

爱丽丝以 0 分开始，并在她的得分少于 K 分时抽取数字。 抽取时，她从 [1, W] 的范围中随机获得一个整数作为分数进行累计，其中 W 是整数。 每次抽取都是独立的，其结果具有相同的概率。

当爱丽丝获得不少于 K 分时，她就停止抽取数字。 爱丽丝的分数不超过 N 的概率是多少？

示例 1：

```text
输入：N = 10, K = 1, W = 10
输出：1.00000
说明：爱丽丝得到一张卡，然后停止。
```

示例 2：

```text
输入：N = 6, K = 1, W = 10
输出：0.60000
说明：爱丽丝得到一张卡，然后停止。
在 W = 10 的 6 种可能下，她的得分不超过 N = 6 分。
```

示例 3：

```text
输入：N = 21, K = 17, W = 10
输出：0.73278
```

提示：

```text
1、0 <= K <= N <= 10000
2、1 <= W <= 10000
3、如果答案与正确答案的误差不超过 10^-5，则该答案将被视为正确答案通过。
4、此问题的判断限制时间已经减少
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/new-21-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 提交

```py
# Python3
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [1] * (N + 1)
        cur = 0
        for i in range(1, N + 1):
            if i <= K:
                cur += dp[i - 1]
            if K + W >= i > W:
                cur -= dp[i - 1 - W]
            dp[i] = cur / W
        return sum(dp[K:])
```

#### 参考

##### 方法一：动态规划

爱丽丝获胜的概率只和下一轮开始前的得分有关，因此根据得分计算概率。

令 dp[x] 表示从得分为 x 的情况开始游戏并且获胜的概率，目标是求 dp[0] 的值。

根据规则，当分数达到或超过 K 时游戏结束，游戏结束时，如果分数不超过 N 则获胜，如果分数超过 N 则失败。因此当 K ≤ x≤ min(N, K + W − 1) 时有 dp[x] = 1，当 x > min(N, K + W − 1) 时有 dp[x]=0。

```text
为什么分界线是 min(N, K+W−1)？首先，只有在分数不超过 N 时才算获胜；其次，可以达到的最大分数为 K + W - 1，即在最后一次抽取数字之前的分数为 K−1，并且抽到了 W。
```

当 0 ≤ x ≤ K 时，如何计算 dp[x] 的值？注意到每次在范围 [1, W] 内随机抽取一个整数，且每个整数被抽取到的概率相等，因此可以得到如下状态转移方程：

```text
dp[x]= (dp[x+1] + dp[x+2] + ⋯ + dp[x+W]) / W
```

根据状态转移方程，可以实现如下简单的动态规划：

```py
# Python3
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W + 1)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        for i in range(K - 1, -1, -1):
            for j in range(1, W + 1):
                dp[i] += dp[i + j] / W
        return dp[0]
```

```c++
// C++
class Solution {
public:
    double new21Game(int N, int K, int W) {
        if (K == 0) {
            return 1.0;
        }
        vector<double> dp(K + W + 1);
        for (int i = K; i <= N && i < K + W; i++) {
            dp[i] = 1.0;
        }
        for (int i = K - 1; i >= 0; i--) {
            for (int j = 1; j <= W; j++) {
                dp[i] += dp[i + j] / W;
            }
        }
        return dp[0];
    }
};
```

```java
// Java
class Solution {
    public double new21Game(int N, int K, int W) {
        if (K == 0) {
            return 1.0;
        }
        double[] dp = new double[K + W + 1];
        for (int i = K; i <= N && i < K + W; i++) {
            dp[i] = 1.0;
        }
        for (int i = K - 1; i >= 0; i--) {
            for (int j = 1; j <= W; j++) {
                dp[i] += dp[i + j] / W;
            }
        }
        return dp[0];
    }
}
```

```golang
// Golang
func new21Game(N int, K int, W int) float64 {
    if K == 0 {
        return 1.0
    }
    dp := make([]float64, K + W + 1)
    for i := K; i <= N && i < K + W; i++ {
        dp[i] = 1.0
    }
    for i := K - 1; i >= 0; i-- {
        for j := 1; j <= W; j++ {
            dp[i] += dp[i + j] / float64(W)
        }
    }
    return dp[0]
}
```

上述解法的时间复杂度是 O(N + KW)，会超出时间限制，因此需要优化。

考虑对 dp 的相邻项计算差分，有如下结果：

```text
dp[x] − dp[x + 1]= (dp[x + 1] − dp[x + W + 1]) / W

```

其中 0 ≤ x < K−1。

因此可以得到新的状态转移方程：

```text
dp[x]= dp[x + 1]− (dp[x + W + 1] − dp[x + 1]) / W
```

其中 0 ≤ x < K − 1。

注意到上述状态转移方程中 x 的取值范围，当 x = K − 1 时不适用。因此对于 dp[K − 1] 的值，需要通过

```text
dp[K − 1]= (dp[K] + dp[K + 1] + ⋯ + dp[K + W − 1]) / W
```

计算得到。注意到只有当 K ≤ x ≤ min(N, K + W − 1) 时才有 dp[x] = 1，因此

```text
dp[K − 1]= (min(N, K + W − 1) − K + 1) / W = min(N − K + 1, W) / W
```

可在 O(1) 时间内计算得到 dp[K - 1] 的值。

对于 dp[K - 2] 到 dp[0] 的值，则可通过新的状态转移方程得到。

```py
# Python3
class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K == 0:
            return 1.0
        dp = [0.0] * (K + W + 1)
        for i in range(K, min(N, K + W - 1) + 1):
            dp[i] = 1.0
        dp[K - 1] = float(min(N - K + 1, W)) / W
        for i in range(K - 2, -1, -1):
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W
        return dp[0]
```

```c++
// C++
class Solution {
public:
    double new21Game(int N, int K, int W) {
        if (K == 0) {
            return 1.0;
        }
        vector<double> dp(K + W + 1);
        for (int i = K; i <= N && i < K + W; i++) {
            dp[i] = 1.0;
        }
        dp[K - 1] = 1.0 * min(N - K + 1, W) / W;
        for (int i = K - 2; i >= 0; i--) {
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W;
        }
        return dp[0];
    }
};
```

```java
// Java
class Solution {
    public double new21Game(int N, int K, int W) {
        if (K == 0) {
            return 1.0;
        }
        double[] dp = new double[K + W + 1];
        for (int i = K; i <= N && i < K + W; i++) {
            dp[i] = 1.0;
        }
        dp[K - 1] = 1.0 * Math.min(N - K + 1, W) / W;
        for (int i = K - 2; i >= 0; i--) {
            dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / W;
        }
        return dp[0];
    }
}
```

```golang
// Golang
func new21Game(N int, K int, W int) float64 {
    if K == 0 {
        return 1.0
    }
    dp := make([]float64, K + W + 1)
    for i := K; i <= N && i < K + W; i++ {
        dp[i] = 1.0
    }

    dp[K - 1] = 1.0 * float64(min(N - K + 1, W)) / float64(W)
    for i := K - 2; i >= 0; i-- {
        dp[i] = dp[i + 1] - (dp[i + W + 1] - dp[i + 1]) / float64(W)
    }
    return dp[0]
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
```

**复杂度分析**

- 时间复杂度：O(min(N, K + W))。即需要计算的 dp 值的数量 min(N, K + W − 1)。

- 空间复杂度：O(K + W)。创建了一个长度为 K + W + 1 的数组 dp。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/new-21-game/solution/xin-21dian-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
