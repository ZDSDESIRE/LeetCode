### 2 的幂次方（简单）

给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得  n == 2^x ，则认为 n 是 2 的幂次方。

示例 1：

```text
输入：n = 1
输出：true
解释：20 = 1
```

示例 2：

```text
输入：n = 16
输出：true
解释：24 = 16
```

示例 3：

```text
输入：n = 3
输出：false
```

示例 4：

```text
输入：n = 4
输出：true
```

示例 5：

```text
输入：n = 5
输出：false
```

提示：

- -231 <= n <= 231 - 1

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数学（Math）  # 位运算（Bit Manipulation）
```

#### 提交

```py
# Python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1
# 位运算
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
```

#### 参考

##### 方法一：二进制表示

**思路与算法**

一个数 n 是 2 的幂，当且仅当 n 是正整数，并且 n 的二进制表示中仅包含 1 个 1。

因此我们可以考虑使用位运算，将 n 的二进制表示中最低位的那个 1 提取出来，再判断剩余的数值是否为 0 即可。下面介绍两种常见的与「二进制表示中最低位」相关的位运算技巧。

第一个技巧是

```text
n & (n - 1)
```

其中 & 表示按位与运算。该位运算技巧可以直接将 n 二进制表示的最低位 1 移除，它的原理如下：

> 假设 n 的二进制表示为 (a10⋯0)2，其中 a 表示若干个高位，1 表示最低位的那个 1，0⋯0 表示后面的若干个 0，那么 n−1 的二进制表示为：(a01⋯1)2
> 我们将 (a10⋯0)2 与 (a01⋯1)2 进行按位与运算，高位 a 不变，在这之后的所有位都会变为 0，这样我们就将最低位的那个 1 移除了。

因此，如果 n 是正整数并且 n & (n - 1) = 0，那么 n 就是 2 的幂。

第二个技巧是

```text
n & (-n)
```

其中 -n 是 n 的相反数，是一个负数。该位运算技巧可以直接获取 n 二进制表示的最低位的 1。

由于负数是按照补码规则在计算机中存储的，−n 的二进制表示为 n 的二进制表示的每一位取反再加上 1，因此它的原理如下：

> 假设 n 的二进制表示为 (a10⋯0)2
> ，其中 a 表示若干个高位，1 表示最低位的那个 1， 0⋯0 表示后面的若干个 0，那么 −n 的二进制表示为：(aˉ01⋯1)2+(1)2=(aˉ10⋯0)2
> 其中 aˉ 表示将 a 每一位取反。我们将 (a10⋯0)2 与 (aˉ10⋯0)2 进行按位与运算，高位全部变为 0，最低位的 1 以及之后的所有 0 不变，这样我们就获取了 n 二进制表示的最低位的 1。

因此，如果 n 是正整数并且 n & (-n) = n，那么 n 就是 2 的幂。

**代码**

```c++
// C++
class Solution {
public:
    bool isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
        // return n > 0 && (n & -n) == n;
    }
};
```

```c
// C
bool isPowerOfTwo(int n) {
    return n > 0 && (n & (n - 1)) == 0;
    // return n > 0 && (n & -n) == n;
}
```

```java
// Java
class Solution {
    public boolean isPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
        // return n > 0 && (n & -n) == n;
    }
}
```

```c#
// C#
public class Solution {
    public bool IsPowerOfTwo(int n) {
        return n > 0 && (n & (n - 1)) == 0;
        // return n > 0 && (n & -n) == n;
    }
}
```

```js
// JavaScript
var isPowerOfTwo = function (n) {
  return n > 0 && (n & (n - 1)) === 0;
  // return n > 0 && (n & -n) === n;
};
```

```py
# Python3
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        # return n > 0 and (n & -n) == n
```

```golang
// Golang
func isPowerOfTwo(n int) bool {
    return n > 0 && n&(n-1) == 0
    // return n > 0 && n&-n == n
}
```

**复杂度分析**

- 时间复杂度：O(1)。

- 空间复杂度：O(1)。

##### 方法二：判断是否为最大 2 的幂的约数

**思路与算法**

除了使用二进制表示判断之外，还有一种较为取巧的做法。

在题目给定的 32 位有符号整数的范围内，最大的 2 的幂为 2^30 = 10737418242。我们只需要判断 n 是否是 2^30 的约数即可。

```c++
// C++
class Solution {
private:
    static constexpr int BIG = 1 << 30;

public:
    bool isPowerOfTwo(int n) {
        return n > 0 && BIG % n == 0;
    }
};
```

```java
// Java
class Solution {
    static final int BIG = 1 << 30;
    public boolean isPowerOfTwo(int n) {
        return n > 0 && BIG % n == 0;
    }
}
```

```js
// JavaScript
var isPowerOfTwo = function (n) {
  const BIG = 1 << 30;
  return n > 0 && BIG % n === 0;
};
```

```c
// C
const int BIG = 1 << 30;
bool isPowerOfTwo(int n) {
    return n > 0 && BIG % n == 0;
}
```

```c#
// C#
public class Solution {
    const int BIG = 1 << 30;
    public bool IsPowerOfTwo(int n) {
        return n > 0 && BIG % n == 0;
    }
}
```

```py
# Python3
class Solution:
    BIG = 2**30
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and Solution.BIG % n == 0
```

```golang
// Golang
func isPowerOfTwo(n int) bool {
    const big = 1 << 30
    return n > 0 && big%n == 0
}
```

**复杂度分析**

- 时间复杂度：O(1)。

- 空间复杂度：O(1)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/power-of-two/solution/2de-mi-by-leetcode-solution-rny3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
