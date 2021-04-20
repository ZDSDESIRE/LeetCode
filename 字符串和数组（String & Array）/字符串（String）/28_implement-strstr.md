### 28. 实现 strStr()（简单）

实现 strStr() 函数。

给你两个字符串 haystack 和 needle，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回   -1 。

**说明：**

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

示例 1：

```text
输入：haystack = "hello", needle = "ll"
输出：2
```

示例 2：

```text
输入：haystack = "aaaaa", needle = "bba"
输出：-1
```

示例 3：

```text
输入：haystack = "", needle = ""
输出：0
```

提示：

- 0 <= haystack.length, needle.length <= 5 \* 104
- haystack 和 needle 仅由小写英文字符组成

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 字符串（String）  # 双指针（Two Pointers）
```

#### 提交

```js
/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
  return haystack.indexOf(needle);
};
```

#### 参考

##### 方法一：利用 JS 的 substring 函数

```js
// JavaScript
var strStr = function (haystack, needle) {
  if (needle === "") return 0;
  for (var i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle[0]) {
      if (haystack.substring(i, i + needle.length) === needle) return i;
    }
  }
  return -1;
};
```

##### 方法二：暴力法

```py
# Python3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lenA, lenB = len(haystack), len(needle)
        if not lenB:
            return 0
        if lenB > lenA:
            return -1

        for i in range(lenA - lenB + 1):
            if haystack[i:i + lenB] == needle:
                return i
        return -1
```

**复杂度分析**

- 时间复杂度: O(NM)，其中待匹配串长为 N，模式串串长为 M；
- 空间复杂度：O(1)。

##### 方法三：KMP（Knuth-Morris-Pratt）算法

**思路及算法**

KMP 算法，由 Donald Knuth、James H.Morris 和 Vaughan Pratt 三人于 19771977 年联合发表。

KMP 算法的核心为前缀函数，记作 π(i)，其定义如下：

-- 对于长度为 m 的字符串 s，其前缀函数 π(i)(0 ≤ i < m) 表示 s 的子串 s[0 : i] 的最长的相等的真前缀与真后缀的长度。特别地，如果不存在符合条件的前后缀，那么 π(i)=0。其中真前缀与真后缀的定义为不等于自身的的前缀与后缀。

代码实现分为两部分：

- 第一部分是求 needle 部分的前缀函数，我们需要保留这部分的前缀函数值。
- 第二部分是求 haystack 部分的前缀函数，我们无需保留这部分的前缀函数值。只需要用一个变量记录上一个位置的前缀函数值即可。当某个位置的前缀函数值等于 m 时，说明我们就找到了一次字符串 needle 在字符串 haystack 中的出现（因为此时真前缀恰为字符串 needle，真后缀为以当前位置为结束位置的字符串 haystack 的子串），我们计算出起始位置，将其返回即可。

**代码**

```c++
// C++
class Solution {
public:
    int strStr(string haystack, string needle) {
        int n = haystack.size(), m = needle.size();
        if (m == 0) {
            return 0;
        }
        vector<int> pi(m);
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && needle[i] != needle[j]) {
                j = pi[j - 1];
            }
            if (needle[i] == needle[j]) {
                j++;
            }
            pi[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && haystack[i] != needle[j]) {
                j = pi[j - 1];
            }
            if (haystack[i] == needle[j]) {
                j++;
            }
            if (j == m) {
                return i - m + 1;
            }
        }
        return -1;
    }
};
```

```c
// C
int strStr(char* haystack, char* needle) {
    int n = strlen(haystack), m = strlen(needle);
    if (m == 0) {
        return 0;
    }
    int pi[m];
    pi[0] = 0;
    for (int i = 1, j = 0; i < m; i++) {
        while (j > 0 && needle[i] != needle[j]) {
            j = pi[j - 1];
        }
        if (needle[i] == needle[j]) {
            j++;
        }
        pi[i] = j;
    }
    for (int i = 0, j = 0; i < n; i++) {
        while (j > 0 && haystack[i] != needle[j]) {
            j = pi[j - 1];
        }
        if (haystack[i] == needle[j]) {
            j++;
        }
        if (j == m) {
            return i - m + 1;
        }
    }
    return -1;
}
```

```java
// Java
class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        if (m == 0) {
            return 0;
        }
        int[] pi = new int[m];
        for (int i = 1, j = 0; i < m; i++) {
            while (j > 0 && needle.charAt(i) != needle.charAt(j)) {
                j = pi[j - 1];
            }
            if (needle.charAt(i) == needle.charAt(j)) {
                j++;
            }
            pi[i] = j;
        }
        for (int i = 0, j = 0; i < n; i++) {
            while (j > 0 && haystack.charAt(i) != needle.charAt(j)) {
                j = pi[j - 1];
            }
            if (haystack.charAt(i) == needle.charAt(j)) {
                j++;
            }
            if (j == m) {
                return i - m + 1;
            }
        }
        return -1;
    }
}
```

```js
// JavaScript
var strStr = function (haystack, needle) {
  const n = haystack.length,
    m = needle.length;
  if (m === 0) {
    return 0;
  }
  const pi = new Array(m).fill(0);
  for (let i = 1, j = 0; i < m; i++) {
    while (j > 0 && needle[i] !== needle[j]) {
      j = pi[j - 1];
    }
    if (needle[i] == needle[j]) {
      j++;
    }
    pi[i] = j;
  }
  for (let i = 0, j = 0; i < n; i++) {
    while (j > 0 && haystack[i] != needle[j]) {
      j = pi[j - 1];
    }
    if (haystack[i] == needle[j]) {
      j++;
    }
    if (j === m) {
      return i - m + 1;
    }
  }
  return -1;
};
```

```golang
// Golang
func strStr(haystack, needle string) int {
    n, m := len(haystack), len(needle)
    if m == 0 {
        return 0
    }
    pi := make([]int, m)
    for i, j := 1, 0; i < m; i++ {
        for j > 0 && needle[i] != needle[j] {
            j = pi[j-1]
        }
        if needle[i] == needle[j] {
            j++
        }
        pi[i] = j
    }
    for i, j := 0, 0; i < n; i++ {
        for j > 0 && haystack[i] != needle[j] {
            j = pi[j-1]
        }
        if haystack[i] == needle[j] {
            j++
        }
        if j == m {
            return i - m + 1
        }
    }
    return -1
}
```

**复杂度分析**

- 时间复杂度：O(n + m)，其中 n 是字符串 haystack 的长度，m 是字符串 needle 的长度。我们至多需要遍历两字符串一次。

- 空间复杂度：O(m)，其中 m 是字符串 needle 的长度。我们只需要保存字符串 needle 的前缀函数。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/implement-strstr/solution/shi-xian-strstr-by-leetcode-solution-ds6y/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
