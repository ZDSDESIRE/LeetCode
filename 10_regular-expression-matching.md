### 10.正则表达式匹配（困难）

给你一个字符串  s  和一个字符规律  p，请你来实现一个支持 '.'  和  '\*'  的正则表达式匹配。

```text
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
```

所谓匹配，是要涵盖   整个   字符串  s 的，而不是部分字符串。

说明:

- s  可能为空，且只包含从  a-z  的小写字母。
- p  可能为空，且只包含从  a-z  的小写字母，以及字符  .  和  \*。
  示例 1:

```text
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
```

示例 2:

```text
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
```

示例  3:

```text
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
```

示例 4:

```text
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
```

示例 5:

```text
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/regular-expression-matching
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 提交

**解题思路**

1. 先判断 s 和 p 的第一个字符是否匹配
2. 处理 p[1] 为 \* 号的情况：匹配 0 个或多个字符
3. 处理 . 号的情况：匹配一个字符

```py
# Python3
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s  # 结束条件

        first_match = (len(s) > 0) and p[0] in {s[0], '.'}
        # 先处理 `*`
        if len(p) >=2 and p[1] == '*':
            # 匹配0个 | 多个
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))

        # 处理 `.` ，匹配一个
        return first_match and self.isMatch(s[1:], p[1:])
```

#### 参考

##### 方法一：动态规划

**思路与算法**

题目中的匹配是一个「逐步匹配」的过程：我们每次从字符串 p 中取出一个字符或者「字符 + 星号」的组合，并在 s 中进行匹配。对于 p 中一个字符而言，它只能在 s 中匹配一个字符，匹配的方法具有唯一性；而对于 p 中字符 + 星号的组合而言，它可以在 s 中匹配任意自然数个字符，并不具有唯一性。因此我们可以考虑使用动态规划，对匹配的方案进行枚举。

我们用 f[i][j] 表示 s 的前 i 个字符与 p 中的前 j 个字符是否能够匹配。在进行状态转移时，我们考虑 p 的第 j 个字符的匹配情况：

- 如果 p 的第 j 个字符是一个小写字母，那么我们必须在 s 中匹配一个相同的小写字母，即

```text
            f[i−1][j−1],  s[i] = p[j]
f[i][j] = {
            false,        s[i] ≠ p[j]
```

也就是说，如果 s 的第 i 个字符与 p 的第 j 个字符不相同，那么无法进行匹配；否则我们可以匹配两个字符串的最后一个字符，完整的匹配结果取决于两个字符串前面的部分。

如果 p 的第 j 个字符是 \*，那么就表示我们可以对 p 的第 j - 1 个字符匹配任意自然数次。在匹配 0 次的情况下，我们有

```text
f[i][j] = f[i][j - 2]
```

也就是我们「浪费」了一个字符 + 星号的组合，没有匹配任何 s 中的字符。

在匹配 1, 2, 3, ⋯ 次的情况下，类似地我们有

```text
f[i][j] = f[i − 1][j − 2],  if s[i] = p[j − 1]
f[i][j] = f[i − 2][j − 2],  if s[i − 1] = s[i] = p[j − 1]
f[i][j] = f[i − 3][j − 2],  if s[i − 2] = s[i − 1] = s[i] = p[j − 1]
```

如果我们通过这种方法进行转移，那么我们就需要枚举这个组合到底匹配了 s 中的几个字符，会增导致时间复杂度增加，并且代码编写起来十分麻烦。我们不妨换个角度考虑这个问题：字母 + 星号的组合在匹配的过程中，本质上只会有两种情况：

- 匹配 ss 末尾的一个字符，将该字符扔掉，而该组合还可以继续进行匹配；

- 不匹配字符，将该组合扔掉，不再进行匹配。

如果按照这个角度进行思考，我们可以写出很精巧的状态转移方程：

```text
          f[i − 1][j] or f[i][j−2], s[i] = p[j − 1]
f[i][j]={
          f[i][j − 2],  s[i] ≠ p[j−1]
```

在任意情况下，只要 p[j] 是 .，那么 p[j] 一定成功匹配 s 中的任意一个小写字母。

最终的状态转移方程如下：

```text
                                f[i − 1][j − 1],  matches(s[i], p[j])
            if (p[j] ≠ ‘*’) = {
                                false,        otherwise
f[i][j]= {
                          f[i − 1][j] or f[i][j − 2], matches(s[i], p[j − 1])
            otherwise = {
                          f[i][j − 2],  otherwise
```

其中 matches(x, y) 判断两个字符是否匹配的辅助函数。只有当 y 是 . 或者 x 和 y 本身相同时，这两个字符才会匹配。

**细节**

动态规划的边界条件为 f[0][0] = true，即两个空字符串是可以匹配的。最终的答案即为 f[m][n]，其中 m 和 n 分别是字符串 s 和 p 的长度。由于大部分语言中，字符串的字符下标是从 0 开始的，因此在实现上面的状态转移方程时，需要注意状态中每一维下标与实际字符下标的对应关系。

在上面的状态转移方程中，如果字符串 p 中包含一个字符+星号的组合（例如 a*），那么在进行状态转移时，会先将 a 进行匹配（当 p[j] 为 a 时），再将 a* 作为整体进行匹配（当 p[j] 为 _ 时）。然而，在题目描述中，我们必须将 a_ 看成一个整体，因此将 a 进行匹配是不符合题目要求的。看来我们进行了额外的状态转移，这样会对最终的答案产生影响吗？这个问题留给读者进行思考。

```py
# Python3
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def matches(i: int, j: int) -> bool:
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        f = [[False] * (n + 1) for _ in range(m + 1)]
        f[0][0] = True
        for i in range(m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    f[i][j] |= f[i][j - 2]
                    if matches(i, j - 1):
                        f[i][j] |= f[i - 1][j]
                else:
                    if matches(i, j):
                        f[i][j] |= f[i - 1][j - 1]
        return f[m][n]
```

```c++
// C++
class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.size();
        int n = p.size();

        auto matches = [&](int i, int j) {
            if (i == 0) {
                return false;
            }
            if (p[j - 1] == '.') {
                return true;
            }
            return s[i - 1] == p[j - 1];
        };

        vector<vector<int>> f(m + 1, vector<int>(n + 1));
        f[0][0] = true;
        for (int i = 0; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (p[j - 1] == '*') {
                    f[i][j] |= f[i][j - 2];
                    if (matches(i, j - 1)) {
                        f[i][j] |= f[i - 1][j];
                    }
                }
                else {
                    if (matches(i, j)) {
                        f[i][j] |= f[i - 1][j - 1];
                    }
                }
            }
        }
        return f[m][n];
    }
};
```

```java
// Java
class Solution {
    public boolean isMatch(String s, String p) {
        int m = s.length();
        int n = p.length();

        boolean[][] f = new boolean[m + 1][n + 1];
        f[0][0] = true;
        for (int i = 0; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (p.charAt(j - 1) == '*') {
                    f[i][j] = f[i][j - 2];
                    if (matches(s, p, i, j - 1)) {
                        f[i][j] = f[i][j] || f[i - 1][j];
                    }
                }
                else {
                    if (matches(s, p, i, j)) {
                        f[i][j] = f[i - 1][j - 1];
                    }
                }
            }
        }
        return f[m][n];
    }

    public boolean matches(String s, String p, int i, int j) {
        if (i == 0) {
            return false;
        }
        if (p.charAt(j - 1) == '.') {
            return true;
        }
        return s.charAt(i - 1) == p.charAt(j - 1);
    }
}
```

```golang
// Golang
func isMatch(s string, p string) bool {
    m, n := len(s), len(p)
    matches := func(i, j int) bool {
        if i == 0 {
            return false
        }
        if p[j-1] == '.' {
            return true
        }
        return s[i-1] == p[j-1]
    }

    f := make([][]bool, m + 1)
    for i := 0; i < len(f); i++ {
        f[i] = make([]bool, n + 1)
    }
    f[0][0] = true
    for i := 0; i <= m; i++ {
        for j := 1; j <= n; j++ {
            if p[j-1] == '*' {
                f[i][j] = f[i][j] || f[i][j-2]
                if matches(i, j - 1) {
                    f[i][j] = f[i][j] || f[i-1][j]
                }
            } else if matches(i, j) {
                f[i][j] = f[i][j] || f[i-1][j-1]
            }
        }
    }
    return f[m][n]
}
```

**复杂度分析**

- 时间复杂度：O(mn)，其中 m 和 n 分别是字符串 s 和 p 的长度。我们需要计算出所有的状态，并且每个状态在进行转移时的时间复杂度为 O(1)。

- 空间复杂度：O(mn)，即为存储所有状态使用的空间。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/regular-expression-matching/solution/zheng-ze-biao-da-shi-pi-pei-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
