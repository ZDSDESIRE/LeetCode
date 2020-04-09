### 820. 单词的压缩编码

给定一个单词列表，我们将这个列表编码成一个索引字符串  S  与一个索引列表 A。
例如，如果这个列表是 ["time", "me", "bell"]，我们就可以将其表示为 S = "time#bell#" 和 indexes = [0, 2, 5]。
对于每一个索引，我们可以通过从字符串 S  中索引的位置开始读取字符串，直到 "#" 结束，来恢复我们之前的单词列表。
那么成功对给定单词列表进行编码的最小字符串长度是多少呢？

示例：

```text
输入: words = ["time", "me", "bell"]
输出: 10
说明: S = "time#bell#" ， indexes = [0, 2, 5] 。
```

提示：

```text
1 <= words.length <= 2000
1 <= words[i].length <= 7
每个单词都是小写字母 。
```

#### 提交

```py
# 解题思路
# 1、discard函数会删去set中的元素，如果不存在，不会报错
# 2、只要确定set中没有重复单词即可

# Python3
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        word=set(words)
        sum=0
        for i in words:
            for j in range(1, len(i)):
                word.discard(i[j:])
        for k in word:
            sum+=len(k)+1
        return sum
```

#### 参考

##### 预备知识——字典树

#### 方法一：存储后缀

**思路**

如果单词 X 是 Y 的后缀，那么单词 X 就不需要考虑了，因为编码 Y 的时候就同时将 X 编码了。例如，如果 words 中同时有 "me" 和 "time"，我们就可以在不改变答案的情况下不考虑 "me"。
如果单词 Y 不在任何别的单词 X 的后缀中出现，那么 Y 一定是编码字符串的一部分。
因此，目标就是保留所有不是其他单词后缀的单词，最后的结果就是这些单词长度加一的总和，因为每个单词编码后后面还需要跟一个 # 符号。

**算法**

由数据范围可知一个单词最多含有 7 个后缀，所以我们可以枚举单词所有的后缀。对于每个后缀，如果其存在 words 列表中，我们就将其从列表中删除。为了高效删除，我们将 words 用哈希集合（HashSet）来存储。

```py
# Python3
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        good = set(words)
        for word in words:
            for k in range(1, len(word)):
                good.discard(word[k:])

        return sum(len(word) + 1 for word in good)
```

```c++
// C++
class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        unordered_set<string> good(words.begin(), words.end());
        for (const string& word: words) {
            for (int k = 1; k < word.size(); ++k) {
                good.erase(word.substr(k));
            }
        }

        int ans = 0;
        for (const string& word: good) {
            ans += word.size() + 1;
        }
        return ans;
    }
};
```

```java
// Java
class Solution {
    public int minimumLengthEncoding(String[] words) {
        Set<String> good = new HashSet(Arrays.asList(words));
        for (String word: words) {
            for (int k = 1; k < word.length(); ++k)
                good.remove(word.substring(k));
        }

        int ans = 0;
        for (String word: good)
            ans += word.length() + 1;
        return ans;
    }
}
```

**复杂度分析**

- 时间复杂度：O(\∑w_i^2)，其中 w_i 是 words[i] 的长度。每个单词有 w_i 个后缀，对于每个后缀，查询其是否在集合中时需要进行 O(w_i) 的哈希值计算。

- 空间复杂度：O(∑w_i)，存储单词的空间开销。

##### 方法二：字典树

如方法一所说，目标就是留所有不是其他单词后缀的单词。

**算法**

去找到是否不同的单词具有相同的后缀，我们可以将其反序之后插入字典树中。例如，我们有 "time" 和 "me"，可以将 "emit" 和 "em" 插入字典树中。
然后，字典树的叶子节点（没有孩子的节点）就代表没有后缀的单词，统计叶子节点代表的单词长度加一的和即为我们要的答案。

```py
# Python3
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created
        # when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie)
                 for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
                   for i, word in enumerate(words)
                   if len(nodes[i]) == 0)
```

```c++
// C++
class TrieNode{
    TrieNode* children[26];
public:
    int count;
    TrieNode() {
        for (int i = 0; i < 26; ++i) children[i] = NULL;
        count = 0;
    }
    TrieNode* get(char c) {
        if (children[c - 'a'] == NULL) {
            children[c - 'a'] = new TrieNode();
            count++;
        }
        return children[c - 'a'];
    }
};
class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        TrieNode* trie = new TrieNode();
        unordered_map<TrieNode*, int> nodes;

        for (int i = 0; i < (int)words.size(); ++i) {
            string word = words[i];
            TrieNode* cur = trie;
            for (int j = word.length() - 1; j >= 0; --j)
                cur = cur->get(word[j]);
            nodes[cur] = i;
        }

        int ans = 0;
        for (auto& [node, idx] : nodes) {
            if (node->count == 0) {
                ans += words[idx].length() + 1;
            }
        }
        return ans;
    }
};
```

```java
// Java
class Solution {
    public int minimumLengthEncoding(String[] words) {
        TrieNode trie = new TrieNode();
        Map<TrieNode, Integer> nodes = new HashMap();

        for (int i = 0; i < words.length; ++i) {
            String word = words[i];
            TrieNode cur = trie;
            for (int j = word.length() - 1; j >= 0; --j)
                cur = cur.get(word.charAt(j));
            nodes.put(cur, i);
        }

        int ans = 0;
        for (TrieNode node: nodes.keySet()) {
            if (node.count == 0)
                ans += words[nodes.get(node)].length() + 1;
        }
        return ans;

    }
}

class TrieNode {
    TrieNode[] children;
    int count;
    TrieNode() {
        children = new TrieNode[26];
        count = 0;
    }
    public TrieNode get(char c) {
        if (children[c - 'a'] == null) {
            children[c - 'a'] = new TrieNode();
            count++;
        }
        return children[c - 'a'];
    }
}
```

**复杂度分析**

- 时间复杂度：O(∑w_i)，其中 w_i 是 words[i] 的长度。对于每个单词中的每个字母，只需要进行常数次操作。

- 空间复杂度：O(S∗∑w_i)，字典树的空间开销，其中 S 为字符集大小。

**注：**

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/short-encoding-of-words/solution/dan-ci-de-ya-suo-bian-ma-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
