### 131.分割回文串（中等）

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

示例 1：

```text
输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
```

示例 2：

```text
输入：s = "a"
输出：[["a"]]
```

提示：

- 1 <= s.length <= 16
- s 仅由小写英文字母组成

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 回溯算法（Backtracking）  # 深度优先搜索（DFS）  # 动态规划（DP）
```

#### 提交

```py
# Python3
# 回溯算法
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])
        helper(s, [])
        return res
# DP + DFS
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if (s[i] == s[j]) and (i - j <= 2 or dp[j + 1][i - 1]):
                    dp[j][i] = True
        res = []

        def helper(i, tmp):
            if i == n:
                res.append(tmp)
            for j in range(i, n):
                if dp[i][j]:
                    helper(j + 1, tmp + [s[i: j + 1]])

        helper(0, [])
        return res
```

#### 参考
