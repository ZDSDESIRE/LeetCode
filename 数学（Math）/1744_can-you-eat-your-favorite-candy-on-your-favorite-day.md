### 1744. 你能在你最喜欢的那天吃到你最喜欢的糖果吗？（中等）

给你一个下标从 0 开始的正整数数组 candiesCount，其中 candiesCount[i]表示你拥有的第 i 类糖果的数目。同时给你一个二维数组 queries，其中 queries[i] = [favoriteType_i, favoriteDay_i, dailyCap_i] 。

你按照如下规则进行一场游戏：

- 你从第 0 天开始吃糖果。
- 你在吃完所有第 i - 1 类糖果之前，不能吃任何一颗第 i 类糖果。
- 在吃完所有糖果之前，你必须每天 至少吃一颗糖果。

请你构建一个布尔型数组 answer，满足 answer.length == queries.length 。answer[i] 为 true 的条件是：在每天吃不超过 dailyCap_i 颗糖果的前提下，你可以在第 favoriteDay_i 天吃到第 favoriteType_i 类糖果；否则 answer[i] 为 false 。注意，只要满足上面 3 条规则中的第二条规则，你就可以在同一天吃不同类型的糖果。

请你返回得到的数组 answer 。

示例 1：

```text
输入：candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
输出：[true,false,true]
提示：
1- 在第 0 天吃 2 颗糖果(类型 0），第 1 天吃 2 颗糖果（类型 0），第 2 天你可以吃到类型 0 的糖果。
2- 每天你最多吃 4 颗糖果。即使第 0 天吃 4 颗糖果（类型 0），第 1 天吃 4 颗糖果（类型 0 和类型 1），你也没办法在第 2 天吃到类型 4 的糖果。换言之，你没法在每天吃 4 颗糖果的限制下在第 2 天吃到第 4 类糖果。
3- 如果你每天吃 1 颗糖果，你可以在第 13 天吃到类型 2 的糖果。
```

示例 2：

```text
输入：candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
输出：[false,true,true,false,false]
```

提示：

- 1 <= candiesCount.length <= 105
- 1 <= candiesCount[i] <= 105
- 1 <= queries.length <= 105
- queries[i].length == 3
- 0 <= favoriteTypei < candiesCount.length
- 0 <= favoriteDayi <= 109
- 1 <= dailyCapi <= 109

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数学（Math）
```

#### 提交

1. 利用前缀和缓存能吃到每种类型的糖果的数量区间；
2. 遍历 queries 数组，得到 favoriteDay 能吃到的糖果数量区间；
3. 将两个区间进行比较，计算是否有交集，有则返回 true。

```js
// JavaScript
var canEat = function (candiesCount, queries) {
  const sum = [0];
  for (let i = 0; i < candiesCount.length; i++) {
    sum.push(sum[i] + candiesCount[i]);
  }

  return queries.map(([type, day, cap]) => {
    const min = sum[type] + 1,
      max = sum[type + 1];
    const left = (day + 1) * 1,
      right = (day + 1) * cap;
    return !(min > right || max < left);
  });
};
```

#### 参考

**前言**
读者需要注意的题目中的一个小陷阱：我们是从第 0 天开始吃糖果。因此对于第 i 个询问，我们可以吃 favoriteDay_i + 1 天的糖果。

##### 方法一：前缀和

**思路与算法**

对于第 i 个询问 (favoriteType_i, favoriteDay_i, dailyCap_i)，我们每天至少吃 1 颗糖果，至多吃 dailyCap_i 颗糖果，因此我们吃的糖果的数量落在区间：

[favoriteDay_i + 1, (favoriteDay_i + 1) × dailyCap_i]

内。那么只要这个区间包含了一颗第 favoriteType_i 种类型的糖果，就可以满足要求了。

因此我们求出糖果数量的前缀和，记录在数组 sum 中，那么第 favoriteType_i 种类型的糖果对应的编号范围为：
[sum[favoriteType_i − 1] + 1, sum[favoriteType_i]]

特别地，如果 favoriteType_i 为 0，那么区间的左端点为 1。

我们只要判断这两个区间是否有交集即可。如果有交集，说明我们可以吃到第 favoriteType_i 类的糖果。判断是否有交集的方法如下：

> 对于区间 [x1, y1] 以及 [x2, y2]，它们没有交集当且仅当 x1 > y2 或者 y1 < x2。

**代码**

```c++
// C++
class Solution {
private:
    using LL = long long;

public:
    vector<bool> canEat(vector<int>& candiesCount, vector<vector<int>>& queries) {
        int n = candiesCount.size();

        // 前缀和
        vector<LL> sum(n);
        sum[0] = candiesCount[0];
        for (int i = 1; i < n; ++i) {
            sum[i] = sum[i - 1] + candiesCount[i];
        }

        vector<bool> ans;
        for (const auto& q: queries) {
            int favoriteType = q[0], favoriteDay = q[1], dailyCap = q[2];

            LL x1 = favoriteDay + 1;
            LL y1 = (LL)(favoriteDay + 1) * dailyCap;
            LL x2 = (favoriteType == 0 ? 1 : sum[favoriteType - 1] + 1);
            LL y2 = sum[favoriteType];

            ans.push_back(!(x1 > y2 || y1 < x2));
        }
        return ans;
    }
};
```

```java
// Java
class Solution {
    public boolean[] canEat(int[] candiesCount, int[][] queries) {
        int n = candiesCount.length;

        // 前缀和
        long[] sum = new long[n];
        sum[0] = candiesCount[0];
        for (int i = 1; i < n; ++i) {
            sum[i] = sum[i - 1] + candiesCount[i];
        }

        int q = queries.length;
        boolean[] ans = new boolean[q];
        for (int i = 0; i < q; ++i) {
            int[] query = queries[i];
            int favoriteType = query[0], favoriteDay = query[1], dailyCap = query[2];

            long x1 = favoriteDay + 1;
            long y1 = (long) (favoriteDay + 1) * dailyCap;
            long x2 = favoriteType == 0 ? 1 : sum[favoriteType - 1] + 1;
            long y2 = sum[favoriteType];

            ans[i] = !(x1 > y2 || y1 < x2);
        }
        return ans;
    }
}
```

```js
// JavaScript
var canEat = function (candiesCount, queries) {
  const n = candiesCount.length;

  // 前缀和
  const sum = new Array(n).fill(0);
  sum[0] = candiesCount[0];
  for (let i = 1; i < n; ++i) {
    sum[i] = sum[i - 1] + candiesCount[i];
  }

  const q = queries.length;
  const ans = new Array(q).fill(0);
  for (let i = 0; i < q; ++i) {
    const query = queries[i];
    const favoriteType = query[0],
      favoriteDay = query[1],
      dailyCap = query[2];

    const x1 = favoriteDay + 1;
    const y1 = (favoriteDay + 1) * dailyCap;
    const x2 = favoriteType == 0 ? 1 : sum[favoriteType - 1] + 1;
    const y2 = sum[favoriteType];

    ans[i] = !(x1 > y2 || y1 < x2);
  }
  return ans;
};
```

```c
// C
bool* canEat(int* candiesCount, int candiesCountSize, int** queries, int queriesSize, int* queriesColSize, int* returnSize) {
    int n = candiesCountSize;

    // 前缀和
    long sum[n];
    sum[0] = candiesCount[0];
    for (int i = 1; i < n; ++i) {
        sum[i] = sum[i - 1] + candiesCount[i];
    }
    bool* ans = malloc(sizeof(bool) * queriesSize);
    *returnSize = queriesSize;
    for (int i = 0; i < queriesSize; i++) {
        int* q = queries[i];
        int favoriteType = q[0], favoriteDay = q[1], dailyCap = q[2];

        long x1 = favoriteDay + 1;
        long y1 = (long)(favoriteDay + 1) * dailyCap;
        long x2 = (favoriteType == 0 ? 1 : sum[favoriteType - 1] + 1);
        long y2 = sum[favoriteType];

        ans[i] = !(x1 > y2 || y1 < x2);
    }
    return ans;
}
```

```c#
// C#
public class Solution {
    public bool[] CanEat(int[] candiesCount, int[][] queries) {
        int n = candiesCount.Length;

        // 前缀和
        long[] sum = new long[n];
        sum[0] = candiesCount[0];
        for (int i = 1; i < n; ++i) {
            sum[i] = sum[i - 1] + candiesCount[i];
        }

        int q = queries.Length;
        bool[] ans = new bool[q];
        for (int i = 0; i < q; ++i) {
            int[] query = queries[i];
            int favoriteType = query[0], favoriteDay = query[1], dailyCap = query[2];

            long x1 = favoriteDay + 1;
            long y1 = (long) (favoriteDay + 1) * dailyCap;
            long x2 = favoriteType == 0 ? 1 : sum[favoriteType - 1] + 1;
            long y2 = sum[favoriteType];

            ans[i] = !(x1 > y2 || y1 < x2);
        }
        return ans;
    }
}
```

```py
# Python3
class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        # 前缀和
        total = list(accumulate(candiesCount))

        ans = list()
        for favoriteType, favoriteDay, dailyCap in queries:
            x1 = favoriteDay + 1
            y1 = (favoriteDay + 1) * dailyCap
            x2 = 1 if favoriteType == 0 else total[favoriteType - 1] + 1
            y2 = total[favoriteType]

            ans.append(not(x1 > y2 or y1 < x2))

        return ans
```

```golang
// Golang
func canEat(candiesCount []int, queries [][]int) []bool {
    n := len(candiesCount)

    // 前缀和
    sum := make([]int, n)
    sum[0] = candiesCount[0]
    for i := 1; i < n; i++ {
        sum[i] = sum[i-1] + candiesCount[i]
    }

    ans := make([]bool, len(queries))
    for i, q := range queries {
        favoriteType, favoriteDay, dailyCap := q[0], q[1], q[2]

        x1 := favoriteDay + 1
        y1 := (favoriteDay + 1) * dailyCap
        x2 := 1
        if favoriteType > 0 {
            x2 = sum[favoriteType-1] + 1
        }
        y2 := sum[favoriteType]

        ans[i] = !(x1 > y2 || y1 < x2)
    }
    return ans
}
```

**复杂度分析**

- 时间复杂度：O(n + q)，其中 n 和 q 分别是数组 candiesCount 和 queries 的长度。我们需要 O(n) 的时间计算前缀和，O(q) 的时间得到所有询问的结果。

- 空间复杂度：O(n)，即为存储前缀和数组需要的空间。注意返回值不计入空间复杂度。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/solution/ni-neng-zai-ni-zui-xi-huan-de-na-tian-ch-boa0/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
