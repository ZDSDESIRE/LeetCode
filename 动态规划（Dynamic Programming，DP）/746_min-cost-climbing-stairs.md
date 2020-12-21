### 746.使用最小花费爬楼梯（简单）

数组的每个索引作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值 cost[i](索引从 0 开始)。

每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。

您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例  1:

```text
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。
```

示例 2:

```text
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。
```

注意：

- cost 的长度将会在[2, 1000]。
- 每一个 cost[i]将会是一个 Integer 类型，范围为[0, 999]。

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数组（String）  # 动态规划（DP）
```

#### 提交

```js
// JavaScript
// 递归
var minCostClimbingStairs = function (cost) {
  d = (i) => (i >= cost.length ? 0 : cost[i] + Math.min(d(i + 1), d(i + 2)));
  return Math.min(d(0), d(1));
};
// 动态规划
var minCostClimbingStairs = function (cost) {
  let dp = new Uint32Array(cost.length + 1),
    i = 1;
  while (i++ < cost.length)
    dp[i] = Math.min(dp[i - 2] + cost[i - 2], dp[i - 1] + cost[i - 1]);
  return dp[i - 1];
};
```

#### 参考

##### 方法一：动态规划

假设数组 cost 的长度为 n，则 n 个阶梯分别对应下标 0 到 n−1，楼层顶部对应下标 n，问题等价于计算达到下标 n 的最小花费。可以通过动态规划求解。

创建长度为 n+1 的数组 dp，其中 dp[i] 表示达到下标 i 的最小花费。

由于可以选择下标 0 或 1 作为初始阶梯，因此有 dp[0] = dp[1] = 0。

当 2 ≤ i ≤ n 时，可以从下标 i-1 使用 cost[i−1] 的花费达到下标 i，或者从下标 i-2 使用 cost[i−2] 的花费达到下标 ii。为了使总花费最小，dp[i] 应取上述两项的最小值，因此状态转移方程如下：

```text
dp[i] = min(dp[i−1] + cost[i−1], dp[i−2] + cost[i−2])
```

依次计算 dp 中的每一项的值，最终得到的 dp[n] 即为达到楼层顶部的最小花费。

```c++
// C++
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        vector<int> dp(n + 1);
        dp[0] = dp[1] = 0;
        for (int i = 2; i <= n; i++) {
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[n];
    }
};
```

```java
// Java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int[] dp = new int[n + 1];
        dp[0] = dp[1] = 0;
        for (int i = 2; i <= n; i++) {
            dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
        }
        return dp[n];
    }
}
```

```js
// JavaScript
var minCostClimbingStairs = function (cost) {
  const n = cost.length;
  const dp = new Array(n + 1);
  dp[0] = dp[1] = 0;
  for (let i = 2; i <= n; i++) {
    dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
  }
  return dp[n];
};
```

```golang
// Golang
func minCostClimbingStairs(cost []int) int {
    n := len(cost)
    dp := make([]int, n+1)
    for i := 2; i <= n; i++ {
        dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
    }
    return dp[n]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

```py
# Python3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)
        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        return dp[n]
```

```c
// C
int minCostClimbingStairs(int* cost, int costSize) {
    int dp[costSize + 1];
    dp[0] = dp[1] = 0;
    for (int i = 2; i <= costSize; i++) {
        dp[i] = fmin(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
    }
    return dp[costSize];
}
```

上述代码的时间复杂度和空间复杂度都是 O(n)。注意到当 i ≥ 2 时，dp[i] 只和 dp[i−1] 与 dp[i−2] 有关，因此可以使用滚动数组的思想，将空间复杂度优化到 O(1)。

```c++
// C++
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        int prev = 0, curr = 0;
        for (int i = 2; i <= n; i++) {
            int next = min(curr + cost[i - 1], prev + cost[i - 2]);
            prev = curr;
            curr = next;
        }
        return curr;
    }
};
```

```java
// Java
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int n = cost.length;
        int prev = 0, curr = 0;
        for (int i = 2; i <= n; i++) {
            int next = Math.min(curr + cost[i - 1], prev + cost[i - 2]);
            prev = curr;
            curr = next;
        }
        return curr;
    }
}
```

```js
// JavaScript
var minCostClimbingStairs = function (cost) {
  const n = cost.length;
  let prev = 0,
    curr = 0;
  for (let i = 2; i <= n; i++) {
    let next = Math.min(curr + cost[i - 1], prev + cost[i - 2]);
    prev = curr;
    curr = next;
  }
  return curr;
};
```

```py
# Python3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        prev = curr = 0
        for i in range(2, n + 1):
            nxt = min(curr + cost[i - 1], prev + cost[i - 2])
            prev, curr = curr, nxt
        return curr
```

```golang
// Golang
func minCostClimbingStairs(cost []int) int {
    n := len(cost)
    pre, cur := 0, 0
    for i := 2; i <= n; i++ {
        pre, cur = cur, min(cur+cost[i-1], pre+cost[i-2])
    }
    return cur
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
```

```c
// C
int minCostClimbingStairs(int* cost, int costSize) {
    int prev = 0, curr = 0;
    for (int i = 2; i <= costSize; i++) {
        int next = fmin(curr + cost[i - 1], prev + cost[i - 2]);
        prev = curr;
        curr = next;
    }
    return curr;
}
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 是数组 cost 的长度。需要依次计算每个 dp 值，每个值的计算需要常数时间，因此总时间复杂度是 O(n)。

- 空间复杂度：O(1)。使用滚动数组的思想，只需要使用有限的额外空间。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/min-cost-climbing-stairs/solution/shi-yong-zui-xiao-hua-fei-pa-lou-ti-by-l-ncf8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
