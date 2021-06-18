### 483. 最小好进制（困难）

对于给定的整数 n, 如果 n 的 k（k>=2）进制数的所有数位全为 1，则称  k（k>=2）是 n 的一个好进制。

以字符串的形式给出 n, 以字符串的形式返回 n 的最小好进制。

示例 1：

```text
输入："13"
输出："3"
解释：13 的 3 进制是 111。
```

示例 2：

```text
输入："4681"
输出："8"
解释：4681 的 8 进制是 11111。
```

示例 3：

```text
输入："1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。
```

提示：

- n 的取值范围是  [3, 10^18]。
- 输入总是有效且没有前导 0。

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-good-base
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数学（Math）  # 二分查找（Binary Search）
```

#### 提交

```py
# Python3
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n) # base 进制转为十进制
        # 等比数列求和
        def sum(base, N):
            return (1 - base ** N) // (1 - base)
        # bin(n) 会计算出 n 的二进制表示，其会返回形如 '0b10111' 的字符串，，因此需要减去 2
        for N in range(len(bin(n)) - 2, 0, -1):
            left = 2
            right = n - 1
            while left <= right:
                mid = (left + right) // 2
                value = sum(mid, N)

                if value < n:
                    left = mid + 1
                elif value > n:
                    right = mid - 1
                else:
                    return str(mid)
```

**复杂度分析**

- 时间复杂度：O(n × log^2 n)
- 空间复杂度：O(1)

#### 参考

##### 方法一：数学

**思路及解法**

假设正整数 n 在 k (k≥2) 进制下的所有数位都为 1，且位数为 m + 1，那么有：

```text
n = k^0 + k^1 + k^2 + ... + k^m
```

我们首先讨论两种特殊情况：

- m = 0，此时 n = 1，而题目保证 n ≥ 3，所以本题中 m>0。
- m = 1，此时 n = (11)\_k，即 k = n − 1 ≥ 2，这保证了本题有解。

**结论一**：m < log_k n
这个结论帮助我们限制了 mm 的范围，本题中 3 ≤ n ≤ 10^18 且 k ≥ 2，所以 m < log_2 10^{18} < 60。

**结论二**：k = ⌊m√n⌋
这个结论帮助我们在 n 和 m 已知的情况下快速确定 kk 的值。

综合上述两个结论，依据结论一，我们知道 mm 的取值范围为 [1, logkn)，且 m = 1 时必然有解。因为随着 m 的增大，k 不断减小，所以我们只需要从大到小检查每一个 mm 可能的取值，利用结论二快速算出对应的 k 值，然后校验计算出的 kk 值是否有效即可。如果 k 值有效，我们即可返回结果。

在实际代码中，我们首先算出 m 取值的上界 mMax，然后从上界开始向下枚举 m 值，如果当前 m 值对应的 k 合法，那么我们即可返回当前的 k 值。如果我们一直检查到 m = 2 都没能找到答案，那么此时即可直接返回 m = 1 对应的 k 值：n − 1。

**代码**

```js
// JavaScript
var smallestGoodBase = function (n) {
  const nVal = parseInt(n);
  const mMax = Math.floor(Math.log(nVal) / Math.log(2));
  for (let m = mMax; m > 1; m--) {
    const k = BigInt(Math.floor(Math.pow(nVal, 1.0 / m)));
    if (k > 1) {
      let mul = BigInt(1),
        sum = BigInt(1);
      for (let i = 1; i <= m; i++) {
        mul *= k;
        sum += mul;
      }
      if (sum === BigInt(n)) {
        return k + "";
      }
    }
  }
  return BigInt(n) - BigInt(1) + "";
};
```

复杂度分析

时间复杂度：O(log^2 n)。至多需要进行 O(log n)次检查，每次检查的时间复杂度为 O(logn)。

空间复杂度：O(1)。只需要常数的空间保存若干变量。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/smallest-good-base/solution/zui-xiao-hao-jin-zhi-by-leetcode-solutio-csqn/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
