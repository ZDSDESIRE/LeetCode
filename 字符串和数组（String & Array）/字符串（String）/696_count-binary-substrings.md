### 696.计数二进制字串（简单）

给定一个字符串 s，计算具有相同数量 0 和 1 的非空(连续)子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是组合在一起的。

重复出现的子串要计算它们出现的次数。

示例 1 :

```text
输入: "00110011"
输出: 6
解释: 有6个子串具有相同数量的连续1和0：“0011”，“01”，“1100”，“10”，“0011” 和 “01”。

请注意，一些重复出现的子串要计算它们出现的次数。

另外，“00110011”不是有效的子串，因为所有的0（和1）没有组合在一起。
```

示例 2 :

```text
输入: "10101"
输出: 4
解释: 有4个子串：“10”，“01”，“10”，“01”，它们具有相同数量的连续1和0。
```

注意：

- s.length  在 1 到 50,000 之间。
- s  只包含“0”或“1”字符。

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 字符串（String）
```

#### 提交

```py
# Python3
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        res = 0
        i = 0
        for j in range(1, len(s)):
            if s[i] != s[j]:
                res += min(count, j - i)
                count = j - i
                i = j
        res += min(count, len(s) - i)
        return res
```

#### 参考

##### 方法一：按字符分组

**思路与算法**

我们可以将字符串 s 按照 0 和 1 的连续段分组，存在 counts 数组中，例如 s = 00111011，可以得到这样的 counts 数组：counts = {2, 3, 1, 2}。

这里 counts 数组中两个相邻的数一定代表的是两种不同的字符。假设 counts 数组中两个相邻的数字为 u 或者 v，它们对应着 u 个 0 和 v 个 1，或者 u 个 1 和 v 个 0。它们能组成的满足条件的子串数目为 min{u, v}，即一对相邻的数字对答案的贡献。

我们只要遍历所有相邻的数对，求它们的贡献总和，即可得到答案。

不难得到这样的实现：

```c++
// C++
class Solution {
public:
    int countBinarySubstrings(string s) {
        vector<int> counts;
        int ptr = 0, n = s.size();
        while (ptr < n) {
            char c = s[ptr];
            int count = 0;
            while (ptr < n && s[ptr] == c) {
                ++ptr;
                ++count;
            }
            counts.push_back(count);
        }
        int ans = 0;
        for (int i = 1; i < counts.size(); ++i) {
            ans += min(counts[i], counts[i - 1]);
        }
        return ans;
    }
};
```

```java
// Java
class Solution {
    public int countBinarySubstrings(String s) {
        List<Integer> counts = new ArrayList<Integer>();
        int ptr = 0, n = s.length();
        while (ptr < n) {
            char c = s.charAt(ptr);
            int count = 0;
            while (ptr < n && s.charAt(ptr) == c) {
                ++ptr;
                ++count;
            }
            counts.add(count);
        }
        int ans = 0;
        for (int i = 1; i < counts.size(); ++i) {
            ans += Math.min(counts.get(i), counts.get(i - 1));
        }
        return ans;
    }
}
```

```js
// JavaScript
var countBinarySubstrings = function (s) {
  const counts = [];
  let ptr = 0,
    n = s.length;
  while (ptr < n) {
    const c = s.charAt(ptr);
    let count = 0;
    while (ptr < n && s.charAt(ptr) === c) {
      ++ptr;
      ++count;
    }
    counts.push(count);
  }
  let ans = 0;
  for (let i = 1; i < counts.length; ++i) {
    ans += Math.min(counts[i], counts[i - 1]);
  }
  return ans;
};
```

```golang
// Golang
func countBinarySubstrings(s string) int {
    counts := []int{}
    ptr, n := 0, len(s)
    for ptr < n {
        c := s[ptr]
        count := 0
        for ptr < n && s[ptr] == c {
            ptr++
            count++
        }
        counts = append(counts, count)
    }
    ans := 0
    for i := 1; i < len(counts); i++ {
        ans += min(counts[i], counts[i-1])
    }
    return ans
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
```

```c
// C
int countBinarySubstrings(char* s) {
    int n = strlen(s);
    int counts[n], counts_len = 0;
    memset(counts, 0, sizeof(counts));
    int ptr = 0;
    while (ptr < n) {
        char c = s[ptr];
        int count = 0;
        while (ptr < n && s[ptr] == c) {
            ++ptr;
            ++count;
        }
        counts[counts_len++] = count;
    }
    int ans = 0;
    for (int i = 1; i < counts_len; ++i) {
        ans += fmin(counts[i], counts[i - 1]);
    }
    return ans;
}
```

这个实现的时间复杂度和空间复杂度都是 O(n)。

对于某一个位置 i，其实我们只关心 i - 1 位置的 counts 值是多少，所以可以用一个 last 变量来维护当前位置的前一个位置，这样可以省去一个 counts 数组的空间。

**代码**

```c++
// C++
class Solution {
public:
    int countBinarySubstrings(string s) {
        int ptr = 0, n = s.size(), last = 0, ans = 0;
        while (ptr < n) {
            char c = s[ptr];
            int count = 0;
            while (ptr < n && s[ptr] == c) {
                ++ptr;
                ++count;
            }
            ans += min(count, last);
            last = count;
        }
        return ans;
    }
};
```

```java
// Java
class Solution {
    public int countBinarySubstrings(String s) {
        int ptr = 0, n = s.length(), last = 0, ans = 0;
        while (ptr < n) {
            char c = s.charAt(ptr);
            int count = 0;
            while (ptr < n && s.charAt(ptr) == c) {
                ++ptr;
                ++count;
            }
            ans += Math.min(count, last);
            last = count;
        }
        return ans;
    }
}
```

```js
// JavaScript
var countBinarySubstrings = function (s) {
  let ptr = 0,
    n = s.length,
    last = 0,
    ans = 0;
  while (ptr < n) {
    const c = s.charAt(ptr);
    let count = 0;
    while (ptr < n && s.charAt(ptr) === c) {
      ++ptr;
      ++count;
    }
    ans += Math.min(count, last);
    last = count;
  }
  return ans;
};
```

```golang
// Golang
func countBinarySubstrings(s string) int {
    var ptr, last, ans int
    n := len(s)
    for ptr < n {
        c := s[ptr]
        count := 0
        for ptr < n && s[ptr] == c {
            ptr++
            count++
        }
        ans += min(count, last)
        last = count
    }

    return ans
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
```

```c
// C
int countBinarySubstrings(char* s) {
    int ptr = 0, n = strlen(s), last = 0, ans = 0;
    while (ptr < n) {
        char c = s[ptr];
        int count = 0;
        while (ptr < n && s[ptr] == c) {
            ++ptr;
            ++count;
        }
        ans += fmin(count, last);
        last = count;
    }
    return ans;
}
```

**复杂度分析**

- 时间复杂度：O(n)。
- 空间复杂度：O(1)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/count-binary-substrings/solution/ji-shu-er-jin-zhi-zi-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
