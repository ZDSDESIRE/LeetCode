### 122.买卖股票的最佳时机 II（简单）

给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

示例 1:

```text
输入: [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
```

示例 2:

```text
输入: [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
```

示例  3:

```text
输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```

提示：

- 1 <= prices.length <= 3 \* 10 ^ 4
- 0 <= prices[i] <= 10 ^ 4

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 贪心算法（Greedy）  # 数组（String）
```

#### 提交

```py
# Python3
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0: profit += tmp
        return profit
```

#### 参考

##### 方法一：动态规划

考虑到「不能同时参与多笔交易」，因此每天交易结束后只可能存在手里有一支股票或者没有股票的状态。

定义状态 dp[i][0] 表示第 i 天交易完后手里没有股票的最大利润，dp[i][1] 表示第 i 天交易完后手里持有一支股票的最大利润（i 从 0 开始）。

考虑 dp[i][0] 的转移方程，如果这一天交易完后手里没有股票，那么可能的转移状态为前一天已经没有股票，即 dp[i−1][0]，或者前一天结束的时候手里持有一支股票，即 dp[i−1][1]，这时候我们要将其卖出，并获得 prices[i] 的收益。因此为了收益最大化，我们列出如下的转移方程：

```text
dp[i][0] = max{dp[i−1][0], dp[i−1][1] + prices[i]}
```

再来考虑 dp[i][1]，按照同样的方式考虑转移状态，那么可能的转移状态为前一天已经持有一支股票，即 dp[i−1][1]，或者前一天结束时还没有股票，即 dp[i−1][0]，这时候我们要将其买入，并减少 prices[i] 的收益。可以列出如下的转移方程：

```text
dp[i][1] = max{dp[i−1][1], dp[i−1][0] − prices[i]}
```

对于初始状态，根据状态定义我们可以知道第 0 天交易结束的时候 dp[0][0]=0，dp[0][1]=−prices[0]。

因此，我们只要从前往后依次计算状态即可。由于全部交易结束后，持有股票的收益一定低于不持有股票的收益，因此这时候 dp[n−1][0] 的收益必然是大于 dp[n−1][1] 的，最后的答案即为 dp[n−1][0]。

```c++
// C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int dp[n][2];
        dp[0][0] = 0, dp[0][1] = -prices[0];
        for (int i = 1; i < n; ++i) {
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        }
        return dp[n - 1][0];
    }
};
```

```java
// Java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[][] dp = new int[n][2];
        dp[0][0] = 0;
        dp[0][1] = -prices[0];
        for (int i = 1; i < n; ++i) {
            dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
            dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
        }
        return dp[n - 1][0];
    }
}
```

```js
// JavaScript
var maxProfit = function (prices) {
  const n = prices.length;
  const dp = new Array(n).fill(0).map((v) => new Array(2).fill(0));
  (dp[0][0] = 0), (dp[0][1] = -prices[0]);
  for (let i = 1; i < n; ++i) {
    dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] + prices[i]);
    dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] - prices[i]);
  }
  return dp[n - 1][0];
};
```

```golang
// Golang
func maxProfit(prices []int) int {
    n := len(prices)
    dp := make([][2]int, n)
    dp[0][1] = -prices[0]
    for i := 1; i < n; i++ {
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
    }
    return dp[n-1][0]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

```c
// C
int maxProfit(int* prices, int pricesSize) {
    int dp[pricesSize][2];
    dp[0][0] = 0, dp[0][1] = -prices[0];
    for (int i = 1; i < pricesSize; ++i) {
        dp[i][0] = fmax(dp[i - 1][0], dp[i - 1][1] + prices[i]);
        dp[i][1] = fmax(dp[i - 1][1], dp[i - 1][0] - prices[i]);
    }
    return dp[pricesSize - 1][0];
}
```

注意到上面的状态转移方程中，每一天的状态只与前一天的状态有关，而与更早的状态都无关，因此我们不必存储这些无关的状态，只需要将 dp[i−1][0] 和 dp[i−1][1] 存放在两个变量中，通过它们计算出 dp[i][0] 和 dp[i][1] 并存回对应的变量，以便于第 i+1 天的状态转移即可。

```c++
// C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int dp0 = 0, dp1 = -prices[0];
        for (int i = 1; i < n; ++i) {
            int newDp0 = max(dp0, dp1 + prices[i]);
            int newDp1 = max(dp1, dp0 - prices[i]);
            dp0 = newDp0;
            dp1 = newDp1;
        }
        return dp0;
    }
};
```

```java
// Java
class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int dp0 = 0, dp1 = -prices[0];
        for (int i = 1; i < n; ++i) {
            int newDp0 = Math.max(dp0, dp1 + prices[i]);
            int newDp1 = Math.max(dp1, dp0 - prices[i]);
            dp0 = newDp0;
            dp1 = newDp1;
        }
        return dp0;
    }
}
```

```js
// JavaScript
var maxProfit = function (prices) {
  const n = prices.length;
  let dp0 = 0,
    dp1 = -prices[0];
  for (let i = 1; i < n; ++i) {
    let newDp0 = Math.max(dp0, dp1 + prices[i]);
    let newDp1 = Math.max(dp1, dp0 - prices[i]);
    dp0 = newDp0;
    dp1 = newDp1;
  }
  return dp0;
};
```

```golang
// Golang
func maxProfit(prices []int) int {
    n := len(prices)
    dp0, dp1 := 0, -prices[0]
    for i := 1; i < n; i++ {
        dp0, dp1 = max(dp0, dp1+prices[i]), max(dp1, dp0-prices[i])
    }
    return dp0
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

```c
// C
int maxProfit(int* prices, int pricesSize) {
    int dp0 = 0, dp1 = -prices[0];
    for (int i = 1; i < pricesSize; ++i) {
        int newDp0 = fmax(dp0, dp1 + prices[i]);
        int newDp1 = fmax(dp1, dp0 - prices[i]);
        dp0 = newDp0;
        dp1 = newDp1;
    }
    return dp0;
}
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 为数组的长度。一共有 2n 个状态，每次状态转移的时间复杂度为 O(1)，因此时间复杂度为 O(2n) = O(n)。

- 空间复杂度：O(n)。我们需要开辟 O(n) 空间存储动态规划中的所有状态。如果使用空间优化，空间复杂度可以优化至 O(1)。

##### 方法二：贪心

由于股票的购买没有限制，因此整个问题等价于寻找 x 个不相交的区间 (l_i,r_i] 使得如下的等式最大化

```text
x
∑ a[r_i]-a[l_i]
i=1
```

其中 l_i 表示在第 l_i 天买入，r_i 表示在第 r_i 天卖出。

同时我们注意到对于 (l_i, r_i] 这一个区间贡献的价值 a[r_i] - a[l_i]，其实等价于 (l_i, l_i+1],(l_i+1, l_i+2], ..., (r_i-1, r_i] 这若干个区间长度为 1 的区间的价值和，即

```text
a[r_i] - a[l_i] = (a[r_i] - a[r_i-1]) + (a[r_i-1] - a[r_i-2]) + ... + (a[l_i+1] - a[l_i])
```

因此问题可以简化为找 x 个长度为 1 的区间 (l_i, l_i+1] 使得
x
∑ a[l_i+1] − a[l_i]  
i=1
价值最大化。
贪心的角度考虑我们每次选择贡献大于 00 的区间即能使得答案最大化，因此最后答案为

```text
     n−1
ans = ∑ max{0, a[i] − a[i−1]}
     i=1
```

其中 n 为数组的长度。

需要说明的是，贪心算法只能用于计算最大利润，计算的过程并不是实际的交易过程。

考虑题目中的例子 [1,2,3,4,5]，数组的长度 n = 5，由于对所有的 1 ≤ i < n 都有 a[i] > a[i-1]，因此答案为

```text
     n−1
ans = ∑ a[i] − a[i−1] = 4
     i=1
```

但是实际的交易过程并不是进行 4 次买入和 4 次卖出，而是在第 1 天买入，第 5 天卖出。

```c++
// C++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int n = prices.size();
        for (int i = 1; i < n; ++i) {
            ans += max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
};
```

```java
// Java
class Solution {
    public int maxProfit(int[] prices) {
        int ans = 0;
        int n = prices.length;
        for (int i = 1; i < n; ++i) {
            ans += Math.max(0, prices[i] - prices[i - 1]);
        }
        return ans;
    }
}
```

```js
// JavaScript
var maxProfit = function (prices) {
  let ans = 0;
  let n = prices.length;
  for (let i = 1; i < n; ++i) {
    ans += Math.max(0, prices[i] - prices[i - 1]);
  }
  return ans;
};
```

```golang
// Golang
func maxProfit(prices []int) (ans int) {
    for i := 1; i < len(prices); i++ {
        ans += max(0, prices[i]-prices[i-1])
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

```c
// C
int maxProfit(int* prices, int pricesSize) {
    int ans = 0;
    for (int i = 1; i < pricesSize; ++i) {
        ans += fmax(0, prices[i] - prices[i - 1]);
    }
    return ans;
}
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 为数组的长度。我们只需要遍历一次数组即可。

- 空间复杂度：O(1)。只需要常数空间存放若干变量。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/solution/mai-mai-gu-piao-de-zui-jia-shi-ji-ii-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
