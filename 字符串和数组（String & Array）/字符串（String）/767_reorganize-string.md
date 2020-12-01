### 767.重构字符串（中等）

给定一个字符串 S，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

示例  1:

```text
输入: S = "aab"
输出: "aba"
```

示例 2:

```text
输入: S = "aaab"
输出: ""
```

注意:

- S 只包含小写字母并且长度在[1, 500]区间内。

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorganize-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 字符串（String）  # 堆（Heap）  # 贪心算法（Greedy）  # 排序（Sort）
```

#### 提交

```js
// JavaScript
/**
 * @param {string} S
 * @return {string}
 */
var reorganizeString = function (S) {
  let len = S.length;
  let map = new Map();
  let arr = [];
  for (let i = 0; i <= len - 1; i++) {
    map.set(S[i], map.get(S[i]) ? map.get(S[i]) + 1 : 1); // 统计每个字符出现的次数
    if (map.get(S[i]) > (len % 2 == 0 ? len / 2 : (len + 1) / 2)) return ""; // 若字符次数超过字符串长度的一半，则返回“”。
  }
  let odd = -1;
  let even = -2;
  map.forEach((index, str) => {
    let j = index;
    while (j--) {
      arr[index <= len / 2 && odd < len - 2 ? (odd += 2) : (even += 2)] = str;  // 插入字符
    }
  });
  return arr.join("");
};

/**
 * @param {string} S
 * @return {string}
 */
var reorganizeString = function (S) {
  // 字符串拆成数组
  let arr = S.split("");
  // 定义map 统计每个字母出现的次数
  let map = new Map();
  for (let i of arr) {
    let value = map.get(i) || 0;
    map.set(i, value + 1);
  }
  // 把map提取为array 然后根据次数从高到低排序
  let sort_arr = Array.from(map);
  sort_arr.sort((a, b) => b[1] - a[1]);
  // 如果出现次数最多的字母的次数 的空隙 (出现次数减一) 大于 剩下的字母数量 说明没有可行解 直接return
  if (sort_arr[0][1] - 1 > arr.length - sort_arr[0][1]) return "";

  // 清空arr 根据排序后的统计结果 生成 新的arr
  arr = [];
  for (let [char, count] of sort_arr) {
    arr = arr.concat(new Array(count).fill(char));
  }

  // 将arr拆为前后两端 把第二段插入第一段的间隙中 实现可行解
  let i = 1;
  let j = Math.ceil(arr.length / 2);
  while (j < arr.length) {
    let char = arr.splice(j, 1)[0];
    arr.splice(i, 0, char);
    i += 2;
    j++;
  }
  return arr.join("");
};
```

```py
# Python3
class Solution:
    def reorganizeString(self, S: str) -> str:
        res = ""
        counter = collections.Counter(S)
        # 边界条件
        if max(counter.values()) > (len(S) + 1) // 2:
            return res

        # 将字母添加到堆中
        pq = []
        for key, val in counter.items():
            heapq.heappush(pq, (-val, key))

        prev = (0, None)

        # 开始重构字符串
        while pq:
            v,k = heapq.heappop(pq)
            res += k
            if prev[0] < 0:
                heapq.heappush(pq, prev)
            prev = (v + 1, k)

        return res
```

#### 参考

**前言**
这道题是典型的贪心算法的题。重构字符串时，需要根据每个字母在字符串中出现的次数处理每个字母放置的位置。如果出现次数最多的字母可以在重新排布之后不相邻，则可以重新排布字母使得相邻的字母都不相同。如果出现次数最多的字母过多，则无法重新排布字母使得相邻的字母都不相同。

假设字符串的长度为 n，如果可以重新排布成相邻的字母都不相同的字符串，每个字母最多出现多少次？

当 n 是偶数时，有 n/2 个偶数下标和 n/2 个奇数下标，因此每个字母的出现次数都不能超过 n/2 次，否则出现次数最多的字母一定会出现相邻。

当 n 是奇数时，由于共有 (n+1)/2 个偶数下标，因此每个字母的出现次数都不能超过 (n+1)/2 次，否则出现次数最多的字母一定会出现相邻。

由于当 n 是偶数时，在整数除法下满足 n/2 和 (n+1)/2 相等，因此可以合并 n 是偶数与 n 是奇数的情况：如果可以重新排布成相邻的字母都不相同的字符串，每个字母最多出现 (n+1)/2 次。

因此首先遍历字符串并统计每个字母的出现次数，如果存在一个字母的出现次数大于 (n+1)/2，则无法重新排布字母使得相邻的字母都不相同，返回空字符串。如果所有字母的出现次数都不超过 (n+1)/2，则考虑如何重新排布字母。

以下提供两种使用贪心算法的方法，分别基于最大堆和计数。

##### 方法一：基于最大堆的贪心算法

维护最大堆存储字母，堆顶元素为出现次数最多的字母。首先统计每个字母的出现次数，然后将出现次数大于 0 的字母加入最大堆。

当最大堆的元素个数大于 1 时，每次从最大堆取出两个字母，拼接到重构的字符串，然后将两个字母的出现次数分别减 1，并将剩余出现次数大于 0 的字母重新加入最大堆。由于最大堆中的元素都是不同的，因此取出的两个字母一定也是不同的，将两个不同的字母拼接到重构的字符串，可以确保相邻的字母都不相同。

如果最大堆变成空，则已经完成字符串的重构。如果最大堆剩下 1 个元素，则取出最后一个字母，拼接到重构的字符串。

对于长度为 n 的字符串，共有 n/2 次每次从最大堆取出两个字母的操作，当 n 是奇数时，还有一次从最大堆取出一个字母的操作，因此重构的字符串的长度一定是 n。

当 n 是奇数时，是否可能出现重构的字符串的最后两个字母相同的情况？如果最后一个字母在整个字符串中至少出现了 2 次，则在最后一次从最大堆取出两个字母时，该字母会先被选出，因此不会成为重构的字符串的倒数第二个字母，也不可能出现重构的字符串最后两个字母相同的情况。

因此，在重构字符串可行的情况下，基于最大堆的贪心算法可以确保得到正确答案。

**代码**

```c++
// C++
class Solution {
public:
    string reorganizeString(string S) {
        if (S.length() < 2) {
            return S;
        }
        vector<int> counts(26, 0);
        int maxCount = 0;
        int length = S.length();
        for (int i = 0; i < length; i++) {
            char c = S[i];
            counts[c - 'a']++;
            maxCount = max(maxCount, counts[c - 'a']);
        }
        if (maxCount > (length + 1) / 2) {
            return "";
        }
        auto cmp = [&](const char& letter1, const char& letter2) {
            return counts[letter1 - 'a']  < counts[letter2 - 'a'];
        };
        priority_queue<char, vector<char>,  decltype(cmp)> queue{cmp};
        for (char c = 'a'; c <= 'z'; c++) {
            if (counts[c - 'a'] > 0) {
                queue.push(c);
            }
        }
        string sb = "";
        while (queue.size() > 1) {
            char letter1 = queue.top(); queue.pop();
            char letter2 = queue.top(); queue.pop();
            sb += letter1;
            sb += letter2;
            int index1 = letter1 - 'a', index2 = letter2 - 'a';
            counts[index1]--;
            counts[index2]--;
            if (counts[index1] > 0) {
                queue.push(letter1);
            }
            if (counts[index2] > 0) {
                queue.push(letter2);
            }
        }
        if (queue.size() > 0) {
            sb += queue.top();
        }
        return sb;
    }
};
```

```java
// Java
class Solution {
    public String reorganizeString(String S) {
        if (S.length() < 2) {
            return S;
        }
        int[] counts = new int[26];
        int maxCount = 0;
        int length = S.length();
        for (int i = 0; i < length; i++) {
            char c = S.charAt(i);
            counts[c - 'a']++;
            maxCount = Math.max(maxCount, counts[c - 'a']);
        }
        if (maxCount > (length + 1) / 2) {
            return "";
        }
        PriorityQueue<Character> queue = new PriorityQueue<Character>(new Comparator<Character>() {
            public int compare(Character letter1, Character letter2) {
                return counts[letter2 - 'a'] - counts[letter1 - 'a'];
            }
        });
        for (char c = 'a'; c <= 'z'; c++) {
            if (counts[c - 'a'] > 0) {
                queue.offer(c);
            }
        }
        StringBuffer sb = new StringBuffer();
        while (queue.size() > 1) {
            char letter1 = queue.poll();
            char letter2 = queue.poll();
            sb.append(letter1);
            sb.append(letter2);
            int index1 = letter1 - 'a', index2 = letter2 - 'a';
            counts[index1]--;
            counts[index2]--;
            if (counts[index1] > 0) {
                queue.offer(letter1);
            }
            if (counts[index2] > 0) {
                queue.offer(letter2);
            }
        }
        if (queue.size() > 0) {
            sb.append(queue.poll());
        }
        return sb.toString();
    }
}
```

```py
# Python3
class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2:
            return S

        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ""

        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        ans = list()

        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            ans.extend([letter1, letter2])
            counts[letter1] -= 1
            counts[letter2] -= 1
            if counts[letter1] > 0:
                heapq.heappush(queue, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heapq.heappush(queue, (-counts[letter2], letter2))

        if queue:
            ans.append(queue[0][1])

        return "".join(ans)
```

```js
// JavaScript
var reorganizeString = function (S) {
  if (S.length < 2) {
    return S;
  }

  const length = S.length;
  const counts = _.countBy(S);
  const maxCount = Math.max(...Object.values(counts));
  if (maxCount > Math.floor((length + 1) / 2)) {
    return "";
  }

  const queue = new MaxPriorityQueue();
  Object.keys(counts).forEach((x) => queue.enqueue(x, counts[x]));
  let ans = new Array();

  while (queue.size() > 1) {
    const letter1 = queue.dequeue()["element"];
    const letter2 = queue.dequeue()["element"];
    ans = ans.concat(letter1, letter2);
    counts[letter1]--;
    counts[letter2]--;
    if (counts[letter1] > 0) {
      queue.enqueue(letter1, counts[letter1]);
    }
    if (counts[letter2] > 0) {
      queue.enqueue(letter2, counts[letter2]);
    }
  }

  if (queue.size()) {
    ans.push(queue.dequeue()["element"]);
  }

  return ans.join("");
};
```

```golang
// Golang
var cnt [26]int

type hp struct{ sort.IntSlice }

func (h hp) Less(i, j int) bool  { return cnt[h.IntSlice[i]] > cnt[h.IntSlice[j]] }
func (h *hp) Push(v interface{}) { h.IntSlice = append(h.IntSlice, v.(int)) }
func (h *hp) Pop() interface{}   { a := h.IntSlice; v := a[len(a)-1]; h.IntSlice = a[:len(a)-1]; return v }
func (h *hp) push(v int)         { heap.Push(h, v) }
func (h *hp) pop() int           { return heap.Pop(h).(int) }

func reorganizeString(s string) string {
    n := len(s)
    if n <= 1 {
        return s
    }

    cnt = [26]int{}
    maxCnt := 0
    for _, ch := range s {
        ch -= 'a'
        cnt[ch]++
        if cnt[ch] > maxCnt {
            maxCnt = cnt[ch]
        }
    }
    if maxCnt > (n+1)/2 {
        return ""
    }

    h := &hp{}
    for i, c := range cnt[:] {
        if c > 0 {
            h.IntSlice = append(h.IntSlice, i)
        }
    }
    heap.Init(h)

    ans := make([]byte, 0, n)
    for len(h.IntSlice) > 1 {
        i, j := h.pop(), h.pop()
        ans = append(ans, byte('a'+i), byte('a'+j))
        if cnt[i]--; cnt[i] > 0 {
            h.push(i)
        }
        if cnt[j]--; cnt[j] > 0 {
            h.push(j)
        }
    }
    if len(h.IntSlice) > 0 {
        ans = append(ans, byte('a'+h.IntSlice[0]))
    }
    return string(ans)
}
```

**复杂度分析**

- 时间复杂度：O(n log∣Σ∣+∣Σ∣)，其中 n 是字符串的长度，Σ 是字符集，在本题中字符集为所有小写字母，∣Σ∣=26。
  遍历字符串并统计每个字母的出现次数，时间复杂度是 O(n)。
  将每个字母加入最大堆，字母个数最多为 ∣Σ∣，这里设真正出现的小写字母数量为 ∣Σ′∣，那么时间复杂度是 O(∣Σ∣) 加上 O(∣Σ′∣log∣Σ′∣) 或 O(∣Σ′∣)。前者是对数组进行遍历的时间复杂度 O(∣Σ∣)，而后者取决于是将每个字母依次加入最大堆，时间复杂度为 O(∣Σ′∣log∣Σ′∣)；还是直接使用一次堆的初始化操作，时间复杂度为 O(∣Σ′∣)。
  重构字符串需要对最大堆进行取出元素和添加元素的操作，取出元素和添加元素的次数都不会超过 nn 次，每次操作的时间复杂度是 O(log∣Σ′∣)，因此总时间复杂度是 O(n log∣Σ′∣)。由于真正出现的小写字母数量为 ∣Σ′∣ 一定小于等于字符串的长度 n，因此上面的时间复杂度中 O(n)，O(∣Σ′∣log∣Σ′∣) 和 O(∣Σ′∣) 在渐进意义下均小于 O(nlog∣Σ′∣)，只需要保留 O(∣Σ∣)。由于 ∣Σ′∣≤∣Σ∣，为了不引入额外符号，可以将时间复杂度 O(n log∣Σ′∣) 写成 O(n log∣Σ∣)。
  总时间复杂度是 O(n log∣Σ∣+∣Σ∣)。

- 空间复杂度：O(|Σ|)，其中 Σ 是字符集，在本题中字符集为所有小写字母，∣Σ∣=26。这里不计算存储最终答案字符串需要的空间（以及由于语言特性，在构造字符串时需要的额外缓存空间），空间复杂度主要取决于统计每个字母出现次数的数组和优先队列。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/reorganize-string/solution/zhong-gou-zi-fu-chuan-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
