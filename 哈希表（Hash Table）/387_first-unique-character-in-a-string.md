### 387.字符串中的第一个唯一字符（简单）

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回-1。

示例：

```text
s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
```

提示：你可以假定该字符串只包含小写字母。

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 哈希表（Hash Table）  # 字符串（String）
```

#### 提交

```js
// JavaScript
/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
  let r = new Set(),
    i = -1;
  while (++i < s.length)
    if (r.has(s[i]) === false)
      if (i === s.lastIndexOf(s[i])) return i;
      else r.add(s[i]);
  return -1;
};
```

#### 参考

##### 方法一：使用哈希表存储频数

**思路与算法**

我们可以对字符串进行两次遍历。

在第一次遍历时，我们使用哈希映射统计出字符串中每个字符出现的次数。在第二次遍历时，我们只要遍历到了一个只出现一次的字符，那么就返回它的索引，否则在遍历结束后返回 -1。

**代码**

```js
// JavaScript
var firstUniqChar = function (s) {
  const frequency = _.countBy(s);
  for (const [i, ch] of Array.from(s).entries()) {
    if (frequency[ch] === 1) {
      return i;
    }
  }
  return -1;
};
```

```c++
// C++
class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<int, int> frequency;
        for (char ch: s) {
            ++frequency[ch];
        }
        for (int i = 0; i < s.size(); ++i) {
            if (frequency[s[i]] == 1) {
                return i;
            }
        }
        return -1;
    }
};
```

```java
// Java
class Solution {
    public int firstUniqChar(String s) {
        Map<Character, Integer> frequency = new HashMap<Character, Integer>();
        for (int i = 0; i < s.length(); ++i) {
            char ch = s.charAt(i);
            frequency.put(ch, frequency.getOrDefault(ch, 0) + 1);
        }
        for (int i = 0; i < s.length(); ++i) {
            if (frequency.get(s.charAt(i)) == 1) {
                return i;
            }
        }
        return -1;
    }
}
```

```py
# Python3
class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = collections.Counter(s)
        for i, ch in enumerate(s):
            if frequency[ch] == 1:
                return i
        return -1
```

```golang
// Golang
func firstUniqChar(s string) int {
    cnt := [26]int{}
    for _, ch := range s {
        cnt[ch-'a']++
    }
    for i, ch := range s {
        if cnt[ch-'a'] == 1 {
            return i
        }
    }
    return -1
}
```

```c
// C
struct hashTable {
    int key;
    int val;
    UT_hash_handle hh;
};

int firstUniqChar(char* s) {
    struct hashTable* frequency = NULL;
    int n = strlen(s);
    for (int i = 0; i < n; i++) {
        int ikey = s[i];
        struct hashTable* tmp;
        HASH_FIND_INT(frequency, &ikey, tmp);
        if (tmp == NULL) {
            tmp = malloc(sizeof(struct hashTable));
            tmp->key = ikey;
            tmp->val = 1;
            HASH_ADD_INT(frequency, key, tmp);
        } else {
            tmp->val++;
        }
    }
    for (int i = 0; i < n; i++) {
        int ikey = s[i];
        struct hashTable* tmp;
        HASH_FIND_INT(frequency, &ikey, tmp);
        if (tmp != NULL && tmp->val == 1) {
            return i;
        }
    }
    return -1;
}
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 是字符串 s 的长度。我们需要进行两次遍历。

- 空间复杂度：O(∣Σ∣)，其中 Σ 是字符集，在本题中 s 只包含小写字母，因此 ∣Σ∣≤ 26。我们需要 O(∣Σ∣) 的空间存储哈希映射。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string/solution/zi-fu-chuan-zhong-de-di-yi-ge-wei-yi-zi-x9rok/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
