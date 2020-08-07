### 336.回文对（困难）

给定一组互不相同的单词，找出所有不同的索引对(i, j)，使得列表中的两个单词，words[i] + words[j]，可拼接成回文串。

示例 1：

```text
输入：["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]]
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]
```

示例 2：

```text
输入：["bat","tab","cat"]
输出：[[0,1],[1,0]]
解释：可拼接成的回文串为 ["battab","tabbat"]
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 字典树（Tire）  # 哈希表（Hash Table）  # 字符串（String）
```

#### 提交

```py
# Python3
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        # 核心思想--枚举前缀和后缀
        # 如果两个字符串 k1，k2 组成一个回文字符串会出现三种情况
        # len(k1) == len(k2),则需要比较 k1 == k2[::-1]
        # len(k1) < len(k2),例如，k1 = a, k2 = abb,可组成 abba
        # 因为 k2 后缀 bb 已经是回文字符串了，则需要找 k1 与 k2 剩下相等的部分
        # len(k1) > len(k2),例如，k1 = bba, k2 = a,组成 abba
        # 因为 k1 前缀 bb 已经是回文字符串了，则需要找 k1 剩下与 k2 相等的部分

        res = []
        worddict = {word: i for i, word in enumerate(words)}  # 构建一个字典，key 为 word，valie 为索引
        for i, word in enumerate(words):
            # i 为word索引，word 为字符串
            for j in range(len(word) + 1):
                # 这里 +1 是因为，列表切片是前闭后开区间
                tmp1 = word[:j]  # 字符串的前缀
                tmp2 = word[j:]  # 字符串的后缀
                if tmp1[::-1] in worddict and worddict[tmp1[::-1]] != i and tmp2 == tmp2[::-1]:
                    # 当 word 的前缀在字典中，且不是 word 自身，且 word 剩下部分是回文(空也是回文)
                    # 则说明存在能与 word 组成回文的字符串
                    res.append([i, worddict[tmp1[::-1]]])  # 返回此时的 word 下标和找到的字符串下标

                if j > 0 and tmp2[::-1] in worddict and worddict[tmp2[::-1]] != i and tmp1 == tmp1[::-1]:
                    # 当 word 的后缀在字典中，且不是 word 自身，且 word 剩下部分是回文(空也是回文)
                    # 则说明存在能与 word 组成回文的字符串
                    # 注意：因为是后缀，所以至少要从 word 的第二位算起，所以 j > 0
                    res.append([worddict[tmp2[::-1]], i])  # 返回此时的 word 下标和找到的字符串下标
        return res
```

#### 参考

**写在前面**
本题可以想到暴力做法，我们枚举每一对字符串的组合，暴力判断它们是否能够构成回文串即可。时间复杂度 O(n^2 ✖ m)，其中 n 是字符串的数量，m 是字符串的平均长度。时间复杂度并不理想，考虑进行优化。

##### 方法一：枚举前缀和后缀

**思路及算法**

假设存在两个字符串 s_1 和 s_2，s_1 + s_2 是一个回文串，记这两个字符串的长度分别为 len_1 和 len_2，我们分三种情况进行讨论：

1. len_1 = len_2，这种情况下 s_1 是 s_2 的翻转。
2. len_1 > len_2，这种情况下我们可以将 s_1 拆成左右两部分：t_1 和 t_2，其中 t_1 是 s_2 的翻转，t_2 是一个回文串。
3. len_1 < len_2，这种情况下我们可以将 s_2 拆成左右两部分：t_1 和 t_2，其中 t_2 是 s_1 的翻转，t_1 是一个回文串。

这样，对于每一个字符串，我们令其为 s_1 和 s_2 中较长的那一个，然后找到可能和它构成回文串的字符串即可。

具体地说，我们枚举每一个字符串 k，令其为 s_1 和 s_2 中较长的那一个，那么 k 可以被拆分为两部分，t_1 和 t_2。

1. 当 t_1 是回文串时，符合情况 3，我们只需要查询给定的字符串序列中是否包含 t_2 的翻转。
2. 当 t_2 是回文串时，符合情况 2，我们只需要查询给定的字符串序列中是否包含 t_1 的翻转。
   也就是说，我们要枚举字符串 kk 的每一个前缀和后缀，判断其是否为回文串。如果是回文串，我们就查询其剩余部分的翻转是否在给定的字符串序列中出现即可。

注意到空串也是回文串，所以我们可以将 k 拆解为 k + ∅ 或 ∅+k，这样我们就能将情况 1 也解释为特殊的情况 2 或情况 3。

而要实现这些操作，我们只需要设计一个能够在一系列字符串中查询「某个字符串的子串的翻转」是否存在的数据结构，有两种实现方法：

- 我们可以使用字典树存储所有的字符串。在进行查询时，我们将待查询串的子串逆序地在字典树上进行遍历，即可判断其是否存在。

- 我们可以使用哈希表存储所有字符串的翻转串。在进行查询时，我们判断带查询串的子串是否在哈希表中出现，就等价于判断了其翻转是否存在。

**代码**

下面给出的是使用字典树的代码：

```py
# Python3
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        tree = [Node()]

        def insert(s: str, index: int):
            length = len(s)
            add = 0
            for i in range(length):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    tree.append(Node())
                    tree[add].ch[x] = len(tree) - 1
                add = tree[add].ch[x]
            tree[add].flag = index

        def findWord(s: str, left: int, right: int) -> int:
            add = 0
            for i in range(right, left - 1, -1):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    return -1
                add = tree[add].ch[x]
            return tree[add].flag

        def isPalindrome(s: str, left: int, right: int) -> bool:
            length = right - left + 1
            return length < 0 or all(s[left + i] == s[right - i] for i in range(length // 2))

        n = len(words)
        for i, word in enumerate(words):
            insert(word, i)

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret
```

```c++
// C++
class Solution {
public:
    struct node {
        int ch[26];
        int flag;
        node() {
            flag = -1;
            memset(ch, 0, sizeof(ch));
        }
    };

    vector<node> tree;

    void insert(string& s, int id) {
        int len = s.length(), add = 0;
        for (int i = 0; i < len; i++) {
            int x = s[i] - 'a';
            if (!tree[add].ch[x]) {
                tree.emplace_back();
                tree[add].ch[x] = tree.size() - 1;
            }
            add = tree[add].ch[x];
        }
        tree[add].flag = id;
    }

    int findWord(string& s, int left, int right) {
        int add = 0;
        for (int i = right; i >= left; i--) {
            int x = s[i] - 'a';
            if (!tree[add].ch[x]) {
                return -1;
            }
            add = tree[add].ch[x];
        }
        return tree[add].flag;
    }

    bool isPalindrome(string& s, int left, int right) {
        int len = right - left + 1;
        for (int i = 0; i < len / 2; i++) {
            if (s[left + i] != s[right - i]) {
                return false;
            }
        }
        return true;
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        tree.emplace_back(node());
        int n = words.size();
        for (int i = 0; i < n; i++) {
            insert(words[i], i);
        }
        vector<vector<int>> ret;
        for (int i = 0; i < n; i++) {
            int m = words[i].size();
            for (int j = 0; j <= m; j++) {
                if (isPalindrome(words[i], j, m - 1)) {
                    int left_id = findWord(words[i], 0, j - 1);
                    if (left_id != -1 && left_id != i) {
                        ret.push_back({i, left_id});
                    }
                }
                if (j && isPalindrome(words[i], 0, j - 1)) {
                    int right_id = findWord(words[i], j, m - 1);
                    if (right_id != -1 && right_id != i) {
                        ret.push_back({right_id, i});
                    }
                }
            }
        }
        return ret;
    }
};
```

```java
// Java
class Solution {
    class Node {
        int[] ch = new int[26];
        int flag;

        public Node() {
            flag = -1;
        }
    }

    List<Node> tree = new ArrayList<Node>();

    public List<List<Integer>> palindromePairs(String[] words) {
        tree.add(new Node());
        int n = words.length;
        for (int i = 0; i < n; i++) {
            insert(words[i], i);
        }
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) {
            int m = words[i].length();
            for (int j = 0; j <= m; j++) {
                if (isPalindrome(words[i], j, m - 1)) {
                    int leftId = findWord(words[i], 0, j - 1);
                    if (leftId != -1 && leftId != i) {
                        ret.add(Arrays.asList(i, leftId));
                    }
                }
                if (j != 0 && isPalindrome(words[i], 0, j - 1)) {
                    int rightId = findWord(words[i], j, m - 1);
                    if (rightId != -1 && rightId != i) {
                        ret.add(Arrays.asList(rightId, i));
                    }
                }
            }
        }
        return ret;
    }

    public void insert(String s, int id) {
        int len = s.length(), add = 0;
        for (int i = 0; i < len; i++) {
            int x = s.charAt(i) - 'a';
            if (tree.get(add).ch[x] == 0) {
                tree.add(new Node());
                tree.get(add).ch[x] = tree.size() - 1;
            }
            add = tree.get(add).ch[x];
        }
        tree.get(add).flag = id;
    }

    public boolean isPalindrome(String s, int left, int right) {
        int len = right - left + 1;
        for (int i = 0; i < len / 2; i++) {
            if (s.charAt(left + i) != s.charAt(right - i)) {
                return false;
            }
        }
        return true;
    }

    public int findWord(String s, int left, int right) {
        int add = 0;
        for (int i = right; i >= left; i--) {
            int x = s.charAt(i) - 'a';
            if (tree.get(add).ch[x] == 0) {
                return -1;
            }
            add = tree.get(add).ch[x];
        }
        return tree.get(add).flag;
    }
}
```

```golang
// Golang
type Node struct {
    ch [26]int
    flag int
}

var tree []Node

func palindromePairs(words []string) [][]int {
    tree = []Node{Node{[26]int{}, -1}}
    n := len(words)
    for i := 0; i < n; i++ {
        insert(words[i], i)
    }
    ret := [][]int{}
    for i := 0; i < n; i++ {
        word := words[i]
        m := len(word)
        for j := 0; j <= m; j++ {
            if isPalindrome(word, j, m - 1) {
                leftId := findWord(word, 0, j - 1)
                if leftId != -1 && leftId != i {
                    ret = append(ret, []int{i, leftId})
                }
            }
            if j != 0 && isPalindrome(word, 0, j - 1) {
                rightId := findWord(word, j, m - 1)
                if rightId != -1 && rightId != i {
                    ret = append(ret, []int{rightId, i})
                }
            }
        }
    }
    return ret
}

func insert(s string, id int) {
    add := 0
    for i := 0; i < len(s); i++ {
        x := int(s[i] - 'a')
        if tree[add].ch[x] == 0 {
            tree = append(tree, Node{[26]int{}, -1})
            tree[add].ch[x] = len(tree) - 1
        }
        add = tree[add].ch[x]
    }
    tree[add].flag = id
}

func findWord(s string, left, right int) int {
    add := 0
    for i := right; i >= left; i-- {
        x := int(s[i] - 'a')
        if tree[add].ch[x] == 0 {
            return -1
        }
        add = tree[add].ch[x]
    }
    return tree[add].flag
}

func isPalindrome(s string, left, right int) bool {
    for i := 0; i < (right - left + 1) / 2; i++ {
        if s[left + i] != s[right - i] {
            return false
        }
    }
    return true
}
```

```c
// C
struct node {
    int ch[26];
    int flag;
} tree[100001];
int tree_len;

void reset(struct node* p) {
    memset(p->ch, 0, sizeof(int) * 26);
    p->flag = -1;
}

void insert(char* s, int id) {
    int len = strlen(s), add = 0;
    for (int i = 0; i < len; i++) {
        int x = s[i] - 'a';
        if (!tree[add].ch[x]) {
            tree_len++;
            reset(&tree[tree_len - 1]);
            tree[add].ch[x] = tree_len - 1;
        }
        add = tree[add].ch[x];
    }
    tree[add].flag = id;
}

int findWord(char* s, int left, int right) {
    int add = 0;
    for (int i = right; i >= left; i--) {
        int x = s[i] - 'a';
        if (!tree[add].ch[x]) {
            return -1;
        }
        add = tree[add].ch[x];
    }
    return tree[add].flag;
}

bool isPalindrome(char* s, int left, int right) {
    int len = right - left + 1;
    for (int i = 0; i < len / 2; i++) {
        if (s[left + i] != s[right - i]) {
            return false;
        }
    }
    return true;
}

int** palindromePairs(char** words, int wordsSize, int* returnSize, int** returnColumnSizes) {
    reset(&tree[0]);
    tree_len = 1;
    for (int i = 0; i < wordsSize; i++) {
        insert(words[i], i);
    }
    int** ret = malloc(sizeof(int*) * 10001);
    (*returnColumnSizes) = malloc(sizeof(int) * 10001);
    for (int i = 0; i < 10001; i++) {
        ret[i] = malloc(sizeof(int) * 2);
        (*returnColumnSizes)[i] = 2;
    }
    int ret_len = 0;
    for (int i = 0; i < wordsSize; i++) {
        int m = strlen(words[i]);
        for (int j = 0; j <= m; j++) {
            if (isPalindrome(words[i], j, m - 1)) {
                int left_id = findWord(words[i], 0, j - 1);
                if (left_id != -1 && left_id != i) {
                    ret_len++;
                    ret[ret_len - 1][0] = i;
                    ret[ret_len - 1][1] = left_id;
                }
            }
            if (j && isPalindrome(words[i], 0, j - 1)) {
                int right_id = findWord(words[i], j, m - 1);
                if (right_id != -1 && right_id != i) {
                    ret_len++;
                    ret[ret_len - 1][0] = right_id;
                    ret[ret_len - 1][1] = i;
                }
            }
        }
    }
    (*returnSize) = ret_len;
    return ret;
}
```

下面给出的是使用哈希表的代码：

```py
# Python3
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:

        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right+1], -1)

        def isPalindrome(s: str, left: int, right: int) -> bool:
            return (sub := s[left:right+1]) == sub[::-1]

        n = len(words)
        indices = {word[::-1]: i for i, word in enumerate(words)}

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret
```

```c++
// C++
class Solution {
private:
    vector<string> wordsRev;
    unordered_map<string_view, int> indices;

public:
    int findWord(const string_view& s, int left, int right) {
        auto iter = indices.find(s.substr(left, right - left + 1));
        return iter == indices.end() ? -1 : iter->second;
    }

    bool isPalindrome(const string_view& s, int left, int right) {
        int len = right - left + 1;
        for (int i = 0; i < len / 2; i++) {
            if (s[left + i] != s[right - i]) {
                return false;
            }
        }
        return true;
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        int n = words.size();
        for (const string& word: words) {
            wordsRev.push_back(word);
            reverse(wordsRev.back().begin(), wordsRev.back().end());
        }
        for (int i = 0; i < n; ++i) {
            indices.emplace(wordsRev[i], i);
        }

        vector<vector<int>> ret;
        for (int i = 0; i < n; i++) {
            int m = words[i].size();
            if (!m) {
                continue;
            }
            string_view wordView(words[i]);
            for (int j = 0; j <= m; j++) {
                if (isPalindrome(wordView, j, m - 1)) {
                    int left_id = findWord(wordView, 0, j - 1);
                    if (left_id != -1 && left_id != i) {
                        ret.push_back({i, left_id});
                    }
                }
                if (j && isPalindrome(wordView, 0, j - 1)) {
                    int right_id = findWord(wordView, j, m - 1);
                    if (right_id != -1 && right_id != i) {
                        ret.push_back({right_id, i});
                    }
                }
            }
        }
        return ret;
    }
};
```

```java
// Java
class Solution {
    List<String> wordsRev = new ArrayList<String>();
    Map<String, Integer> indices = new HashMap<String, Integer>();

    public List<List<Integer>> palindromePairs(String[] words) {
        int n = words.length;
        for (String word: words) {
            wordsRev.add(new StringBuffer(word).reverse().toString());
        }
        for (int i = 0; i < n; ++i) {
            indices.put(wordsRev.get(i), i);
        }

        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) {
            String word = words[i];
            int m = words[i].length();
            if (m == 0) {
                continue;
            }
            for (int j = 0; j <= m; j++) {
                if (isPalindrome(word, j, m - 1)) {
                    int leftId = findWord(word, 0, j - 1);
                    if (leftId != -1 && leftId != i) {
                        ret.add(Arrays.asList(i, leftId));
                    }
                }
                if (j != 0 && isPalindrome(word, 0, j - 1)) {
                    int rightId = findWord(word, j, m - 1);
                    if (rightId != -1 && rightId != i) {
                        ret.add(Arrays.asList(rightId, i));
                    }
                }
            }
        }
        return ret;
    }

    public boolean isPalindrome(String s, int left, int right) {
        int len = right - left + 1;
        for (int i = 0; i < len / 2; i++) {
            if (s.charAt(left + i) != s.charAt(right - i)) {
                return false;
            }
        }
        return true;
    }

    public int findWord(String s, int left, int right) {
        return indices.getOrDefault(s.substring(left, right + 1), -1);
    }
}
```

```golang
// Golang
func palindromePairs(words []string) [][]int {
    wordsRev := []string{}
    indices := map[string]int{}

    n := len(words)
    for _, word := range words {
        wordsRev = append(wordsRev, reverse(word))
    }
    for i := 0; i < n; i++ {
        indices[wordsRev[i]] = i
    }

    ret := [][]int{}
    for i := 0; i < n; i++ {
        word := words[i]
        m := len(word)
        if m == 0 {
            continue
        }
        for j := 0; j <= m; j++ {
            if isPalindrome(word, j, m - 1) {
                leftId := findWord(word, 0, j - 1, indices)
                if leftId != -1 && leftId != i {
                    ret = append(ret, []int{i, leftId})
                }
            }
            if j != 0 && isPalindrome(word, 0, j - 1) {
                rightId := findWord(word, j, m - 1, indices)
                if rightId != -1 && rightId != i {
                    ret = append(ret, []int{rightId, i})
                }
            }
        }
    }
    return ret
}

func findWord(s string, left, right int, indices map[string]int) int {
    if v, ok := indices[s[left:right+1]]; ok {
        return v
    }
    return -1
}

func isPalindrome(s string, left, right int) bool {
    for i := 0; i < (right - left + 1) / 2; i++ {
        if s[left + i] != s[right - i] {
            return false
        }
    }
    return true
}

func reverse(s string) string {
    n := len(s)
    b := []byte(s)
    for i := 0; i < n/2; i++ {
        b[i], b[n-i-1] = b[n-i-1], b[i]
    }
    return string(b)
}
```

**复杂度分析**

- 时间复杂度：O(n × m^2)，其中 n 是字符串的数量，m 是字符串的平均长度。对于每一个字符串，我们需要 O(m^2) 地判断其所有前缀与后缀是否是回文串，并 O(m^2) 地寻找其所有前缀与后缀是否在给定的字符串序列中出现。

- 空间复杂度：O(n × m)，其中 n 是字符串的数量，m 是字符串的平均长度。为字典树的空间开销。

##### 方法二：字典树 + manacher

**说明**

方法二为竞赛难度，在面试中不作要求。学有余力的读者可以学习在字符串中寻找最长回文串的「manacher 算法」。

**思路及算法**

注意到方法一中，对于每一个字符串 k，我们需要 O(m^2) 地判断 k 的所有前缀与后缀是否是回文串，还需要 O(m^2) 地判断 k 的所有前缀与后缀是否在给定字符串序列中出现。我们可以优化这两部分的时间复杂度。

- 对于判断其所有前缀与后缀是否是回文串：

  - 利用 manacher 算法，可以线性地处理出每一个前后缀是否是回文串。

- 对于判断其所有前缀与后缀是否在给定的字符串序列中出现：

  - 对于给定的字符串序列，分别正向与反向建立字典树，利用正向建立的字典树验证 k 的后缀的翻转，利用反向建立的字典树验证 k 的前缀的翻转。

这样我们就可以快速找出能够和字符串 k 构成回文串的字符串。

注意：因为该解法常数较大，因此在随机数据下的表现并没有方法一优秀。
**代码**

```c++
// C++
struct Trie {
    struct node {
        int ch[26];
        int flag;
        node() {
            flag = -1;
            memset(ch, 0, sizeof(ch));
        }
    };

    vector<node> tree;

    Trie() { tree.emplace_back(); }

    void insert(string& s, int id) {
        int len = s.length(), add = 0;
        for (int i = 0; i < len; i++) {
            int x = s[i] - 'a';
            if (!tree[add].ch[x]) {
                tree.emplace_back();
                tree[add].ch[x] = tree.size() - 1;
            }
            add = tree[add].ch[x];
        }
        tree[add].flag = id;
    }

    vector<int> query(string& s) {
        int len = s.length(), add = 0;
        vector<int> ret(len + 1, -1);
        for (int i = 0; i < len; i++) {
            ret[i] = tree[add].flag;
            int x = s[i] - 'a';
            if (!tree[add].ch[x]) {
                return ret;
            }
            add = tree[add].ch[x];
        }
        ret[len] = tree[add].flag;
        return ret;
    }
};

class Solution {
public:
    vector<pair<int, int>> manacher(string& s) {
        int n = s.length();
        string tmp = "#";
        tmp += s[0];
        for (int i = 1; i < n; i++) {
            tmp += '*';
            tmp += s[i];
        }
        tmp += '!';
        int m = n * 2;
        vector<int> len(m);
        vector<pair<int, int>> ret(n);
        int p = 0, maxn = -1;
        for (int i = 1; i < m; i++) {
            len[i] = maxn >= i ? min(len[2 * p - i], maxn - i) : 0;
            while (tmp[i - len[i] - 1] == tmp[i + len[i] + 1]) {
                len[i]++;
            }
            if (i + len[i] > maxn) {
                p = i, maxn = i + len[i];
            }
            if (i - len[i] == 1) {
                ret[(i + len[i]) / 2].first = 1;
            }
            if (i + len[i] == m - 1) {
                ret[(i - len[i]) / 2].second = 1;
            }
        }
        return ret;
    }

    vector<vector<int>> palindromePairs(vector<string>& words) {
        Trie trie1, trie2;

        int n = words.size();
        for (int i = 0; i < n; i++) {
            trie1.insert(words[i], i);
            string tmp = words[i];
            reverse(tmp.begin(), tmp.end());
            trie2.insert(tmp, i);
        }

        vector<vector<int>> ret;
        for (int i = 0; i < n; i++) {
            const vector<pair<int, int>>& rec = manacher(words[i]);

            const vector<int>& id1 = trie2.query(words[i]);
            reverse(words[i].begin(), words[i].end());
            const vector<int>& id2 = trie1.query(words[i]);

            int m = words[i].size();

            int all_id = id1[m];
            if (all_id != -1 && all_id != i) {
                ret.push_back({i, all_id});
            }
            for (int j = 0; j < m; j++) {
                if (rec[j].first) {
                    int left_id = id2[m - j - 1];
                    if (left_id != -1 && left_id != i) {
                        ret.push_back({left_id, i});
                    }
                }
                if (rec[j].second) {
                    int right_id = id1[j];
                    if (right_id != -1 && right_id != i) {
                        ret.push_back({i, right_id});
                    }
                }
            }
        }
        return ret;
    }
};
```

```java
// Java
class Solution {
    public List<List<Integer>> palindromePairs(String[] words) {
        Trie trie1 = new Trie();
        Trie trie2 = new Trie();

        int n = words.length;
        for (int i = 0; i < n; i++) {
            trie1.insert(words[i], i);
            StringBuffer tmp = new StringBuffer(words[i]);
            tmp.reverse();
            trie2.insert(tmp.toString(), i);
        }

        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        for (int i = 0; i < n; i++) {
            int[][] rec = manacher(words[i]);

            int[] id1 = trie2.query(words[i]);
            words[i] = new StringBuffer(words[i]).reverse().toString();
            int[] id2 = trie1.query(words[i]);

            int m = words[i].length();

            int allId = id1[m];
            if (allId != -1 && allId != i) {
                ret.add(Arrays.asList(i, allId));
            }
            for (int j = 0; j < m; j++) {
                if (rec[j][0] != 0) {
                    int leftId = id2[m - j - 1];
                    if (leftId != -1 && leftId != i) {
                        ret.add(Arrays.asList(leftId, i));
                    }
                }
                if (rec[j][1] != 0) {
                    int rightId = id1[j];
                    if (rightId != -1 && rightId != i) {
                        ret.add(Arrays.asList(i, rightId));
                    }
                }
            }
        }
        return ret;
    }

    public int[][] manacher(String s) {
        int n = s.length();
        StringBuffer tmp = new StringBuffer("#");
        for (int i = 0; i < n; i++) {
            if (i > 0) {
                tmp.append('*');
            }
            tmp.append(s.charAt(i));
        }
        tmp.append('!');
        int m = n * 2;
        int[] len = new int[m];
        int[][] ret = new int[n][2];
        int p = 0, maxn = -1;
        for (int i = 1; i < m; i++) {
            len[i] = maxn >= i ? Math.min(len[2 * p - i], maxn - i) : 0;
            while (tmp.charAt(i - len[i] - 1) == tmp.charAt(i + len[i] + 1)) {
                len[i]++;
            }
            if (i + len[i] > maxn) {
                p = i;
                maxn = i + len[i];
            }
            if (i - len[i] == 1) {
                ret[(i + len[i]) / 2][0] = 1;
            }
            if (i + len[i] == m - 1) {
                ret[(i - len[i]) / 2][1] = 1;
            }
        }
        return ret;
    }
}

class Trie {
    class Node {
        int[] ch = new int[26];
        int flag;

        public Node() {
            flag = -1;
        }
    }

    List<Node> tree = new ArrayList<Node>();

    public Trie() {
        tree.add(new Node());
    }

    public void insert(String s, int id) {
        int len = s.length(), add = 0;
        for (int i = 0; i < len; i++) {
            int x = s.charAt(i) - 'a';
            if (tree.get(add).ch[x] == 0) {
                tree.add(new Node());
                tree.get(add).ch[x] = tree.size() - 1;
            }
            add = tree.get(add).ch[x];
        }
        tree.get(add).flag = id;
    }

    public int[] query(String s) {
        int len = s.length(), add = 0;
        int[] ret = new int[len + 1];
        Arrays.fill(ret, -1);
        for (int i = 0; i < len; i++) {
            ret[i] = tree.get(add).flag;
            int x = s.charAt(i) - 'a';
            if (tree.get(add).ch[x] == 0) {
                return ret;
            }
            add = tree.get(add).ch[x];
        }
        ret[len] = tree.get(add).flag;
        return ret;
    }
}
```

**复杂度分析**

- 时间复杂度：O(n × m)，其中 n 是字符串的数量，m 是字符串的平均长度。对于每一个字符串，我们需要 O(m) 地判断其所有前缀与后缀是否是回文串，并 O(m) 地寻找其所有前缀与后缀是否在给定的字符串序列中出现。

- 空间复杂度：O(n × m)，其中 n 是字符串的数量，m 是字符串的平均长度。为字典树的空间开销。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/palindrome-pairs/solution/hui-wen-dui-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
