### 127.单词接龙（中等）

给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。转换需遵循如下规则：

每次转换只能改变一个字母。
转换过程中的中间单词必须是字典中的单词。
说明:

如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例  1:

```text
输入:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

输出: 5

解释: 一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog",
     返回它的长度 5。
```

示例 2:

```text
输入:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

输出: 0

解释: endWord "cog" 不在字典中，所以无法进行转换。
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-ladder
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 广度优先搜索（BFS）
```

#### 提交

```py
# Python3
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordict = set(wordList)
        s1 = { beginWord }
        s2 = { endWord }
        n = len(beginWord)
        step = 0
        wordict.remove(endWord)
        while s1 and s2:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1
            s = set()
            for word in s1:
                nextword = [word[:i] + chr(j) + word[i + 1:] for j in range(97, 123) for i in range(n)]
                for w in nextword:
                    if w in s2:
                        return step + 1
                    if w not in wordict: continue
                    wordict.remove(w)
                    s.add(w)
            s1 = s
        return 0
```

#### 参考

##### 方法一：广度优先搜索 + 优化建图

**思路**

本题要求的是最短转换序列的长度，看到最短首先想到的就是广度优先搜索。想到广度优先搜索自然而然的就能想到图，但是本题并没有直截了当的给出图的模型，因此我们需要把它抽象成图的模型。

我们可以把每个单词都抽象为一个点，如果两个单词可以只改变一个字母进行转换，那么说明他们之间有一条双向边。因此我们只需要把满足转换条件的点相连，就形成了一张图。

基于该图，我们以 beginWord 为图的起点，以 endWord 为终点进行广度优先搜索，寻找 beginWord 到 endWord 的最短路径。
![1](https://assets.leetcode-cn.com/solution-static/127/1.png)
**算法**

基于上面的思路我们考虑如何编程实现。

首先为了方便表示，我们先给每一个单词标号，即给每个单词分配一个 id。创建一个由单词 word 到 id 对应的映射 wordId，并将 beginWord 与 wordList 中所有的单词都加入这个映射中。之后我们检查 endWord 是否在该映射内，若不存在，则输入无解。我们可以使用哈希表实现上面的映射关系。

然后我们需要建图，依据朴素的思路，我们可以枚举每一对单词的组合，判断它们是否恰好相差一个字符，以判断这两个单词对应的节点是否能够相连。但是这样效率太低，我们可以优化建图。

具体地，我们可以创建虚拟节点。对于单词 hit，我们创建三个虚拟节点 \*it、h\*t、hi\*，并让 hit 向这三个虚拟节点分别连一条边即可。如果一个单词能够转化为 hit，那么该单词必然会连接到这三个虚拟节点之一。对于每一个单词，我们枚举它连接到的虚拟节点，把该单词对应的 id 与这些虚拟节点对应的 id 相连即可。

最后我们将起点加入队列开始广度优先搜索，当搜索到终点时，我们就找到了最短路径的长度。注意因为添加了虚拟节点，所以我们得到的距离为实际最短路径长度的两倍。同时我们并未计算起点对答案的贡献，所以我们应当返回距离的一半再加一的结果。

**代码**

```py
# Python3
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        return 0
```

```c++
// C++
class Solution {
public:
    unordered_map<string, int> wordId;
    vector<vector<int>> edge;
    int nodeNum = 0;

    void addWord(string& word) {
        if (!wordId.count(word)) {
            wordId[word] = nodeNum++;
            edge.emplace_back();
        }
    }

    void addEdge(string& word) {
        addWord(word);
        int id1 = wordId[word];
        for (char& it : word) {
            char tmp = it;
            it = '*';
            addWord(word);
            int id2 = wordId[word];
            edge[id1].push_back(id2);
            edge[id2].push_back(id1);
            it = tmp;
        }
    }

    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        for (string& word : wordList) {
            addEdge(word);
        }
        addEdge(beginWord);
        if (!wordId.count(endWord)) {
            return 0;
        }
        vector<int> dis(nodeNum, INT_MAX);
        int beginId = wordId[beginWord], endId = wordId[endWord];
        dis[beginId] = 0;

        queue<int> que;
        que.push(beginId);
        while (!que.empty()) {
            int x = que.front();
            que.pop();
            if (x == endId) {
                return dis[endId] / 2 + 1;
            }
            for (int& it : edge[x]) {
                if (dis[it] == INT_MAX) {
                    dis[it] = dis[x] + 1;
                    que.push(it);
                }
            }
        }
        return 0;
    }
};
```

```java
// Java
class Solution {
    Map<String, Integer> wordId = new HashMap<String, Integer>();
    List<List<Integer>> edge = new ArrayList<List<Integer>>();
    int nodeNum = 0;

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        for (String word : wordList) {
            addEdge(word);
        }
        addEdge(beginWord);
        if (!wordId.containsKey(endWord)) {
            return 0;
        }
        int[] dis = new int[nodeNum];
        Arrays.fill(dis, Integer.MAX_VALUE);
        int beginId = wordId.get(beginWord), endId = wordId.get(endWord);
        dis[beginId] = 0;

        Queue<Integer> que = new LinkedList<Integer>();
        que.offer(beginId);
        while (!que.isEmpty()) {
            int x = que.poll();
            if (x == endId) {
                return dis[endId] / 2 + 1;
            }
            for (int it : edge.get(x)) {
                if (dis[it] == Integer.MAX_VALUE) {
                    dis[it] = dis[x] + 1;
                    que.offer(it);
                }
            }
        }
        return 0;
    }

    public void addEdge(String word) {
        addWord(word);
        int id1 = wordId.get(word);
        char[] array = word.toCharArray();
        int length = array.length;
        for (int i = 0; i < length; ++i) {
            char tmp = array[i];
            array[i] = '*';
            String newWord = new String(array);
            addWord(newWord);
            int id2 = wordId.get(newWord);
            edge.get(id1).add(id2);
            edge.get(id2).add(id1);
            array[i] = tmp;
        }
    }

    public void addWord(String word) {
        if (!wordId.containsKey(word)) {
            wordId.put(word, nodeNum++);
            edge.add(new ArrayList<Integer>());
        }
    }
}
```

```golang
func ladderLength(beginWord string, endWord string, wordList []string) int {
    wordId := map[string]int{}
    graph := [][]int{}
    addWord := func(word string) int {
        id, has := wordId[word]
        if !has {
            id = len(wordId)
            wordId[word] = id
            graph = append(graph, []int{})
        }
        return id
    }
    addEdge := func(word string) int {
        id1 := addWord(word)
        s := []byte(word)
        for i, b := range s {
            s[i] = '*'
            id2 := addWord(string(s))
            graph[id1] = append(graph[id1], id2)
            graph[id2] = append(graph[id2], id1)
            s[i] = b
        }
        return id1
    }

    for _, word := range wordList {
        addEdge(word)
    }
    beginId := addEdge(beginWord)
    endId, has := wordId[endWord]
    if !has {
        return 0
    }

    const inf int = math.MaxInt64
    dist := make([]int, len(wordId))
    for i := range dist {
        dist[i] = inf
    }
    dist[beginId] = 0
    queue := []int{beginId}
    for len(queue) > 0 {
        v := queue[0]
        queue = queue[1:]
        if v == endId {
            return dist[endId]/2 + 1
        }
        for _, w := range graph[v] {
            if dist[w] == inf {
                dist[w] = dist[v] + 1
                queue = append(queue, w)
            }
        }
    }
    return 0
}
```

```c
struct Trie {
    int ch[27];
    int val;
} trie[50001];

int size, nodeNum;

void insert(char* s, int num) {
    int sSize = strlen(s), add = 0;
    for (int i = 0; i < sSize; ++i) {
        int x = s[i] - '`';
        if (trie[add].ch[x] == 0) {
            trie[add].ch[x] = ++size;
            memset(trie[size].ch, 0, sizeof(trie[size].ch));
            trie[size].val = -1;
        }
        add = trie[add].ch[x];
    }
    trie[add].val = num;
}

int find(char* s) {
    int sSize = strlen(s), add = 0;
    for (int i = 0; i < sSize; ++i) {
        int x = s[i] - '`';
        if (trie[add].ch[x] == 0) {
            return -1;
        }
        add = trie[add].ch[x];
    }
    return trie[add].val;
}

int addWord(char* word) {
    if (find(word) == -1) {
        insert(word, nodeNum++);
    }
    return find(word);
}

int edge[30001][26];

int edgeSize[30001];

void addEdge(char* word) {
    int wordSize = strlen(word), id1 = addWord(word);
    for (int i = 0; i < wordSize; ++i) {
        char tmp = word[i];
        word[i] = '`';
        int id2 = addWord(word);
        edge[id1][edgeSize[id1]++] = id2;
        edge[id2][edgeSize[id2]++] = id1;
        word[i] = tmp;
    }
}

int ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) {
    size = nodeNum = 0;
    memset(trie[size].ch, 0, sizeof(trie[size].ch));
    trie[size].val = -1;
    memset(edgeSize, 0, sizeof(edgeSize));
    for (int i = 0; i < wordListSize; ++i) {
        addEdge(wordList[i]);
    }
    addEdge(beginWord);
    int beginId = find(beginWord), endId = find(endWord);
    if (endId == -1) {
        return 0;
    }

    int dis[nodeNum];
    memset(dis, -1, sizeof(dis));
    dis[beginId] = 0;

    int que[nodeNum];
    int left = 0, right = 0;
    que[right++] = beginId;
    while (left < right) {
        int x = que[left++];
        for (int i = 0; i < edgeSize[x]; ++i) {
            if (dis[edge[x][i]] == -1) {
                dis[edge[x][i]] = dis[x] + 1;
                if (edge[x][i] == endId) {
                    return dis[edge[x][i]] / 2 + 1;
                }
                que[right++] = edge[x][i];
            }
        }
    }
    return 0;
}
```

**复杂度分析**

- 时间复杂度：O(N ✖ C^2)。其中 N 为 wordList 的长度，C 为列表中单词的平均长度。

  - 建图过程中，对于每一个单词，我们需要枚举它连接到的所有虚拟节点，时间复杂度为 O(C)，将这些单词加入到哈希表中，时间复杂度为 O(N ✖ C)，因此总时间复杂度为 O(N ✖ C)。

  - 广度优先搜索的时间复杂度最坏情况下是 O(N ✖ C)O(N×C)。每一个单词需要拓展出 O(C) 个虚拟节点，因此节点数 O(N ✖ C)。

- 空间复杂度：O(N ✖ C^2)。其中 N 为 wordList 的长度，C 为列表中单词的平均长度。哈希表中包含 O(N ✖ C) 个节点，每个节点占用空间 O(C)，因此总的空间复杂度为 O(N ✖ C^2)。

##### 方法二：双向广度优先搜索

**思路及解法**

根据给定字典构造的图可能会很大，而广度优先搜索的搜索空间大小依赖于每层节点的分支数量。假如每个节点的分支数量相同，搜索空间会随着层数的增长指数级的增加。考虑一个简单的二叉树，每一层都是满二叉树的扩展，节点的数量会以 22 为底数呈指数增长。

如果使用两个同时进行的广搜可以有效地减少搜索空间。一边从 beginWord 开始，另一边从 endWord 开始。我们每次从两边各扩展一层节点，当发现某一时刻两边都访问过同一顶点时就停止搜索。这就是双向广度优先搜索，它可以可观地减少搜索空间大小，从而提高代码运行效率。
![2](https://assets.leetcode-cn.com/solution-static/127/2.png)
**代码**

```py
# Python3
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        disBegin = [float("inf")] * nodeNum
        beginId = wordId[beginWord]
        disBegin[beginId] = 0
        queBegin = collections.deque([beginId])

        disEnd = [float("inf")] * nodeNum
        endId = wordId[endWord]
        disEnd[endId] = 0
        queEnd = collections.deque([endId])

        while queBegin or queEnd:
            queBeginSize = len(queBegin)
            for _ in range(queBeginSize):
                nodeBegin = queBegin.popleft()
                if disEnd[nodeBegin] != float("inf"):
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) // 2 + 1
                for it in edge[nodeBegin]:
                    if disBegin[it] == float("inf"):
                        disBegin[it] = disBegin[nodeBegin] + 1
                        queBegin.append(it)

            queEndSize = len(queEnd)
            for _ in range(queEndSize):
                nodeEnd = queEnd.popleft()
                if disBegin[nodeEnd] != float("inf"):
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) // 2 + 1
                for it in edge[nodeEnd]:
                    if disEnd[it] == float("inf"):
                        disEnd[it] = disEnd[nodeEnd] + 1
                        queEnd.append(it)

        return 0
```

```c++
// C++
class Solution {
public:
    unordered_map<string, int> wordId;
    vector<vector<int>> edge;
    int nodeNum = 0;

    void addWord(string& word) {
        if (!wordId.count(word)) {
            wordId[word] = nodeNum++;
            edge.emplace_back();
        }
    }

    void addEdge(string& word) {
        addWord(word);
        int id1 = wordId[word];
        for (char& it : word) {
            char tmp = it;
            it = '*';
            addWord(word);
            int id2 = wordId[word];
            edge[id1].push_back(id2);
            edge[id2].push_back(id1);
            it = tmp;
        }
    }

    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        for (string& word : wordList) {
            addEdge(word);
        }
        addEdge(beginWord);
        if (!wordId.count(endWord)) {
            return 0;
        }

        vector<int> disBegin(nodeNum, INT_MAX);
        int beginId = wordId[beginWord];
        disBegin[beginId] = 0;
        queue<int> queBegin;
        queBegin.push(beginId);

        vector<int> disEnd(nodeNum, INT_MAX);
        int endId = wordId[endWord];
        disEnd[endId] = 0;
        queue<int> queEnd;
        queEnd.push(endId);

        while (!queBegin.empty() && !queEnd.empty()) {
            int queBeginSize = queBegin.size();
            for (int i = 0; i < queBeginSize; ++i) {
                int nodeBegin = queBegin.front();
                queBegin.pop();
                if (disEnd[nodeBegin] != INT_MAX) {
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) / 2 + 1;
                }
                for (int& it : edge[nodeBegin]) {
                    if (disBegin[it] == INT_MAX) {
                        disBegin[it] = disBegin[nodeBegin] + 1;
                        queBegin.push(it);
                    }
                }
            }

            int queEndSize = queEnd.size();
            for (int i = 0; i < queEndSize; ++i) {
                int nodeEnd = queEnd.front();
                queEnd.pop();
                if (disBegin[nodeEnd] != INT_MAX) {
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) / 2 + 1;
                }
                for (int& it : edge[nodeEnd]) {
                    if (disEnd[it] == INT_MAX) {
                        disEnd[it] = disEnd[nodeEnd] + 1;
                        queEnd.push(it);
                    }
                }
            }
        }
        return 0;
    }
};
```

```java
// Java
class Solution {
    Map<String, Integer> wordId = new HashMap<String, Integer>();
    List<List<Integer>> edge = new ArrayList<List<Integer>>();
    int nodeNum = 0;

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {
        for (String word : wordList) {
            addEdge(word);
        }
        addEdge(beginWord);
        if (!wordId.containsKey(endWord)) {
            return 0;
        }

        int[] disBegin = new int[nodeNum];
        Arrays.fill(disBegin, Integer.MAX_VALUE);
        int beginId = wordId.get(beginWord);
        disBegin[beginId] = 0;
        Queue<Integer> queBegin = new LinkedList<Integer>();
        queBegin.offer(beginId);

        int[] disEnd = new int[nodeNum];
        Arrays.fill(disEnd, Integer.MAX_VALUE);
        int endId = wordId.get(endWord);
        disEnd[endId] = 0;
        Queue<Integer> queEnd = new LinkedList<Integer>();
        queEnd.offer(endId);

        while (!queBegin.isEmpty() && !queEnd.isEmpty()) {
            int queBeginSize = queBegin.size();
            for (int i = 0; i < queBeginSize; ++i) {
                int nodeBegin = queBegin.poll();
                if (disEnd[nodeBegin] != Integer.MAX_VALUE) {
                    return (disBegin[nodeBegin] + disEnd[nodeBegin]) / 2 + 1;
                }
                for (int it : edge.get(nodeBegin)) {
                    if (disBegin[it] == Integer.MAX_VALUE) {
                        disBegin[it] = disBegin[nodeBegin] + 1;
                        queBegin.offer(it);
                    }
                }
            }

            int queEndSize = queEnd.size();
            for (int i = 0; i < queEndSize; ++i) {
                int nodeEnd = queEnd.poll();
                if (disBegin[nodeEnd] != Integer.MAX_VALUE) {
                    return (disBegin[nodeEnd] + disEnd[nodeEnd]) / 2 + 1;
                }
                for (int it : edge.get(nodeEnd)) {
                    if (disEnd[it] == Integer.MAX_VALUE) {
                        disEnd[it] = disEnd[nodeEnd] + 1;
                        queEnd.offer(it);
                    }
                }
            }
        }
        return 0;
    }

    public void addEdge(String word) {
        addWord(word);
        int id1 = wordId.get(word);
        char[] array = word.toCharArray();
        int length = array.length;
        for (int i = 0; i < length; ++i) {
            char tmp = array[i];
            array[i] = '*';
            String newWord = new String(array);
            addWord(newWord);
            int id2 = wordId.get(newWord);
            edge.get(id1).add(id2);
            edge.get(id2).add(id1);
            array[i] = tmp;
        }
    }

    public void addWord(String word) {
        if (!wordId.containsKey(word)) {
            wordId.put(word, nodeNum++);
            edge.add(new ArrayList<Integer>());
        }
    }
}
```

```golang
// Golang
func ladderLength(beginWord string, endWord string, wordList []string) int {
    wordId := map[string]int{}
    graph := [][]int{}
    addWord := func(word string) int {
        id, has := wordId[word]
        if !has {
            id = len(wordId)
            wordId[word] = id
            graph = append(graph, []int{})
        }
        return id
    }
    addEdge := func(word string) int {
        id1 := addWord(word)
        s := []byte(word)
        for i, b := range s {
            s[i] = '*'
            id2 := addWord(string(s))
            graph[id1] = append(graph[id1], id2)
            graph[id2] = append(graph[id2], id1)
            s[i] = b
        }
        return id1
    }

    for _, word := range wordList {
        addEdge(word)
    }
    beginId := addEdge(beginWord)
    endId, has := wordId[endWord]
    if !has {
        return 0
    }

    const inf int = math.MaxInt64
    distBegin := make([]int, len(wordId))
    for i := range distBegin {
        distBegin[i] = inf
    }
    distBegin[beginId] = 0
    queueBegin := []int{beginId}

    distEnd := make([]int, len(wordId))
    for i := range distEnd {
        distEnd[i] = inf
    }
    distEnd[endId] = 0
    queueEnd := []int{endId}

    for len(queueBegin) > 0 && len(queueEnd) > 0 {
        q := queueBegin
        queueBegin = nil
        for _, v := range q {
            if distEnd[v] < inf {
                return (distBegin[v]+distEnd[v])/2 + 1
            }
            for _, w := range graph[v] {
                if distBegin[w] == inf {
                    distBegin[w] = distBegin[v] + 1
                    queueBegin = append(queueBegin, w)
                }
            }
        }

        q = queueEnd
        queueEnd = nil
        for _, v := range q {
            if distBegin[v] < inf {
                return (distBegin[v]+distEnd[v])/2 + 1
            }
            for _, w := range graph[v] {
                if distEnd[w] == inf {
                    distEnd[w] = distEnd[v] + 1
                    queueEnd = append(queueEnd, w)
                }
            }
        }
    }
    return 0
}
```

```c
// C
struct Trie {
    int ch[27];
    int val;
} trie[50001];

int size, nodeNum;

void insert(char* s, int num) {
    int sSize = strlen(s), add = 0;
    for (int i = 0; i < sSize; ++i) {
        int x = s[i] - '`';
        if (trie[add].ch[x] == 0) {
            trie[add].ch[x] = ++size;
            memset(trie[size].ch, 0, sizeof(trie[size].ch));
            trie[size].val = -1;
        }
        add = trie[add].ch[x];
    }
    trie[add].val = num;
}

int find(char* s) {
    int sSize = strlen(s), add = 0;
    for (int i = 0; i < sSize; ++i) {
        int x = s[i] - '`';
        if (trie[add].ch[x] == 0) {
            return -1;
        }
        add = trie[add].ch[x];
    }
    return trie[add].val;
}

int addWord(char* word) {
    if (find(word) == -1) {
        insert(word, nodeNum++);
    }
    return find(word);
}

int edge[30001][26];

int edgeSize[30001];

void addEdge(char* word) {
    int wordSize = strlen(word), id1 = addWord(word);
    for (int i = 0; i < wordSize; ++i) {
        char tmp = word[i];
        word[i] = '`';
        int id2 = addWord(word);
        edge[id1][edgeSize[id1]++] = id2;
        edge[id2][edgeSize[id2]++] = id1;
        word[i] = tmp;
    }
}

int ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) {
    size = nodeNum = 0;
    memset(trie[size].ch, 0, sizeof(trie[size].ch));
    trie[size].val = -1;
    memset(edgeSize, 0, sizeof(edgeSize));
    for (int i = 0; i < wordListSize; ++i) {
        addEdge(wordList[i]);
    }
    addEdge(beginWord);
    int beginId = find(beginWord), endId = find(endWord);
    if (endId == -1) {
        return 0;
    }

    int disBegin[nodeNum];
    memset(disBegin, -1, sizeof(disBegin));
    disBegin[beginId] = 0;
    int queBegin[nodeNum];
    int leftBegin = 0, rightBegin = 0;
    queBegin[rightBegin++] = beginId;

    int disEnd[nodeNum];
    memset(disEnd, -1, sizeof(disEnd));
    disEnd[endId] = 0;
    int queEnd[nodeNum];
    int leftEnd = 0, rightEnd = 0;
    queEnd[rightEnd++] = endId;

    while (leftBegin < rightBegin && leftEnd < rightEnd) {
        int queBeginSize = rightBegin - leftBegin;
        for (int i = 0; i < queBeginSize; ++i) {
            int nodeBegin = queBegin[leftBegin++];
            if (disEnd[nodeBegin] != -1) {
                return (disBegin[nodeBegin] + disEnd[nodeBegin]) / 2 + 1;
            }
            for (int j = 0; j < edgeSize[nodeBegin]; ++j) {
                if (disBegin[edge[nodeBegin][j]] == -1) {
                    disBegin[edge[nodeBegin][j]] = disBegin[nodeBegin] + 1;
                    queBegin[rightBegin++] = edge[nodeBegin][j];
                }
            }
        }
        int queEndSize = rightEnd - leftEnd;
        for (int i = 0; i < queEndSize; ++i) {
            int nodeEnd = queEnd[leftEnd++];
            if (disBegin[nodeEnd] != -1) {
                return (disBegin[nodeEnd] + disEnd[nodeEnd]) / 2 + 1;
            }
            for (int j = 0; j < edgeSize[nodeEnd]; ++j) {
                if (disEnd[edge[nodeEnd][j]] == -1) {
                    disEnd[edge[nodeEnd][j]] = disEnd[nodeEnd] + 1;
                    queEnd[rightEnd++] = edge[nodeEnd][j];
                }
            }
        }
    }
    return 0;
}
```

**复杂度分析**

- 时间复杂度：O(N ✖ C^2)。其中 N 为 wordList 的长度，C 为列表中单词的平均长度。

  - 建图过程中，对于每一个单词，我们需要枚举它连接到的所有虚拟节点，时间复杂度为 O(C)，将这些单词加入到哈希表中，时间复杂度为 O(N ✖ C)O，因此总时间复杂度为 O(N ✖ C)。

  - 双向广度优先搜索的时间复杂度最坏情况下是 O(N ✖ C)。每一个单词需要拓展出 O(C) 个虚拟节点，因此节点数 O(N ✖ C)。

- 空间复杂度：O(N ✖ C^2)。其中 N 为 wordList 的长度，C 为列表中单词的平均长度。哈希表中包含 O(N ✖ C) 个节点，每个节点占用空间 O(C)，因此总的空间复杂度为 O(N ✖ C^2)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/word-ladder/solution/dan-ci-jie-long-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
