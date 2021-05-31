### 342. 4 的幂（简单）

给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x

示例 1：

```text
输入：n = 16
输出：true
```

示例 2：

```text
输入：n = 5
输出：false
```

示例 3：

```text
输入：n = 1
输出：true
```

提示：

- -231 <= n <= 231 - 1

进阶：

- 你能不使用循环或者递归来完成本题吗？

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-four
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数学（Math）  # 位运算（Bit Manipulation）
```

#### 提交

```py
# Python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
```

#### 参考

**前言**
如果 n 是 4 的幂，那么 n 一定也是 2 的幂。因此我们可以首先判断 n 是否是 2 的幂，在此基础上再判断 n 是否是 4 的幂。

##### 方法一：二进制表示中 1 的位置

**思路与算法**

如果 n 是 4 的幂，那么 n 的二进制表示中有且仅有一个 1，并且这个 1 出现在从低位开始的第偶数个二进制位上（这是因为这个 1 后面必须有偶数个 0）。这里我们规定最低位为第 0 位，例如 n = 16 时，n 的二进制表示为(10000)2
唯一的 1 出现在第 4 个二进制位上，因此 n 是 4 的幂。
由于题目保证了 n 是一个 32 位的有符号整数，因此我们可以构造一个整数 mask，它的所有偶数二进制位都是 0，所有奇数二进制位都是 1。这样一来，我们将 n 和 mask 进行按位与运算，如果结果为 0，说明 n 二进制表示中的 1 出现在偶数的位置，否则说明其出现在奇数的位置。

根据上面的思路，mask 的二进制表示为：mask=(10101010101010101010101010101010)2

我们也可以将其表示成 16 进制的形式，使其更加美观：mask=(AAAAAAAA)16
**代码**

```c++
// C++
class Solution {
public:
    bool isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0xaaaaaaaa) == 0;
    }
};
```

```java
// Java
class Solution {
    public boolean isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0xaaaaaaaa) == 0;
    }
}
```

```c#
// C#
public class Solution {
    public bool IsPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && (n & 0xaaaaaaaa) == 0;
    }
}
```

```py
# Python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n & 0xaaaaaaaa) == 0
```

```c
// C
bool isPowerOfFour(int n) {
    return n > 0 && (n & (n - 1)) == 0 && (n & 0xaaaaaaaa) == 0;
}
```

```js
// JavaScript
var isPowerOfFour = function (n) {
  return n > 0 && (n & (n - 1)) === 0 && (n & 0xaaaaaaaa) === 0;
};
```

```golang
// Golang
func isPowerOfFour(n int) bool {
    return n > 0 && n&(n-1) == 0 && n&0xaaaaaaaa == 0
}
```

**复杂度分析**

- 时间复杂度：O(1)。

- 空间复杂度：O(1)。

##### 方法二：取模性质

**思路与算法**

如果 n 是 4 的幂，那么它可以表示成 4^x 的形式，我们可以发现它除以 3 的余数一定为 1，即：

```text
4^x ≡ (3+1)^x ≡ 1^x ≡ 1(mod 3)
```

如果 n 是 2 的幂却不是 4 的幂，那么它可以表示成 4^x × 2 的形式，此时它除以 3 的余数一定为 2。

因此我们可以通过 n 除以 3 的余数是否为 1 来判断 n 是否是 4 的幂。

**代码**

```c++
// C++
class Solution {
public:
    bool isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && n % 3 == 1;
    }
};
```

```java
// Java
class Solution {
    public boolean isPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && n % 3 == 1;
    }
}
```

```js
// JavaScript
var isPowerOfFour = function (n) {
  return n > 0 && (n & (n - 1)) === 0 && n % 3 === 1;
};
```

```c#
// C#
public class Solution {
    public bool IsPowerOfFour(int n) {
        return n > 0 && (n & (n - 1)) == 0 && n % 3 == 1;
    }
}
```

```py
# Python3
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
```

```c
// C
bool isPowerOfFour(int n) {
    return n > 0 && (n & (n - 1)) == 0 && n % 3 == 1;
}
```

```golang
// Golang
func isPowerOfFour(n int) bool {
    return n > 0 && n&(n-1) == 0 && n%3 == 1
}
```

**复杂度分析**

- 时间复杂度：O(1)O。

- 空间复杂度：O(1)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/power-of-four/solution/4de-mi-by-leetcode-solution-b3ya/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
