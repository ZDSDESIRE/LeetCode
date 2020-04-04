# 1160.拼写单词（简单）

给你一份『词汇表』（字符串数组） words  和一张『字母表』（字符串） chars。
假如你可以用  chars  中的『字母』（字符）拼写出 words  中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：
每次拼写时，chars 中的每个字母都只能用一次。
返回词汇表  words  中你掌握的所有单词的长度之和。

示例 1：

```text
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释：可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
```

示例 2：

```text
输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
```

提示：

```text
1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
所有字符串中都仅包含小写英文字母
```

#### 提交

```js
// JavaScript
/**
 * @param {string[]} words
 * @param {string} chars
 * @return {number}
 */
var countCharacters = function (words, chars) {
  var len = 0;
  for (let i = 0; i < words.length; i++) {
    if (isHasAllChar(chars, words[i])) {
      len = len + words[i].length;
    }
  }
  return len;
};

/**
 * @param {string} chars
 * @param {string} word
 * @return {boolean}
 */
var isHasAllChar = function (chars, word) {
  var bool = true;
  wd_strs = word.split("");
  for (let ch of wd_strs) {
    if (chars.indexOf(ch) !== -1) {
      chars = chars.replace(ch, "");
    } else bool = false;
  }
  return bool;
};
```

#### 参考

##### 方法一：哈希表记数

**思路和算法**
显然，对于一个单词 word，只要其中的每个字母的数量都不大于 chars 中对应的字母的数量，那么就可以用 chars 中的字母拼写出 word。所以我们只需要用一个哈希表存储 chars 中每个字母的数量，再用一个哈希表存储 word 中每个字母的数量，最后将这两个哈希表的键值对逐一进行比较即可。

```py
# Python3
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_cnt = collections.Counter(chars)
        ans = 0
        for word in words:
            word_cnt = collections.Counter(word)
            for c in word_cnt:
                if chars_cnt[c] < word_cnt[c]:
                    break
            else:
                ans += len(word)
        return ans
```

```c++
// C++
class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        unordered_map<char, int> chars_cnt;
        for (char c : chars)
            ++chars_cnt[c];
        int ans = 0;
        for (string word : words) {
            unordered_map<char, int> word_cnt;
            for (char c : word)
                ++word_cnt[c];
            bool is_ans = true;
            for (char c : word)
                if (chars_cnt[c] < word_cnt[c]) {
                    is_ans = false;
                    break;
                }
            if (is_ans)
                ans += word.size();
        }
        return ans;
    }
};
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 为所有字符串的长度和。我们需要遍历每个字符串，包括 chars 以及数组 words 中的每个单词。
- 空间复杂度：O(S)，其中 S 为字符集大小，在本题中 S 的值为 26（所有字符串仅包含小写字母）。程序运行过程中，最多同时存在两个哈希表，使用的空间均不超过字符集大小 S，因此空间复杂度为 O(S)。

**注：**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters/solution/pin-xie-dan-ci-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
