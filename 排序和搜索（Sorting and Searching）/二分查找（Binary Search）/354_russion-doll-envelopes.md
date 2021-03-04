### 354.俄罗斯套娃信封问题（困难）

给你一个二维整数数组 envelopes ，其中 envelopes[i] = [wi, hi]，表示第 i 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算最多能有多少个信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

**注意**：不允许旋转信封。

示例 1：

```text
输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
```

示例 2：

```text
输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1
```

提示：

- 1 <= envelopes.length <= 5000
- envelopes[i].length == 2
- 1 <= wi, hi <= 104

**注**：
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/russian-doll-envelopes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 二分查找（Binary Search）  # 动态规划（DP）
```

#### 提交

```js
/**
 * @param {number[][]} envelopes
 * @return {number}
 */
var maxEnvelopes = function (envelopes) {
  let len = envelopes.length;
  if (!len) return 0;
  envelopes.sort((a, b) => (a[0] === b[0] ? a[1] - b[1] : a[0] - b[0]));
  const dp = new Array(len).fill(1);
  for (let i = 1; i < len; i++) {
    for (let j = 0; j < i; j++) {
      if (
        envelopes[i][1] > envelopes[j][1] &&
        envelopes[i][0] !== envelopes[j][0]
      ) {
        dp[i] = Math.max(dp[i], dp[j] + 1);
      }
    }
  }
  return Math.max(...dp);
};
```

#### 参考

##### 方法一：基于二分查找的动态规划

**思路与算法**

设 f[j] 表示 h 的前 i 个元素可以组成的长度为 j 的最长严格递增子序列的末尾元素的最小值，如果不存在长度为 j 的最长严格递增子序列，对应的 f 值无定义。在定义范围内，可以看出 f 值是严格单调递增的，因为越长的子序列的末尾元素显然越大。

在进行状态转移时，我们考虑当前的元素 h_i：

- 如果 h_i 大于 f 中的最大值，那么 h_i 就可以接在 f 中的最大值之后，形成一个长度更长的严格递增子序列；

- 否则我们找出 f 中比 h_i 严格小的最大的元素 f[j_0]，即 f[j_0] < h_i ≤ f[j_0+1]，那么 h_i 可以接在 f[j_0] 之后，形成一个长度为 j_0+1 的严格递增子序列，因此需要对 f[j_0+1]进行更新：

```text
f[j_0+1] = h_i
```

我们可以在 f 上进行二分查找，找出满足要求的 j_0。

在遍历所有的 h_i 之后，f 中最后一个有定义的元素的下标增加 1（下标从 0 开始）即为最长严格递增子序列的长度。

**代码**

```c++
// C++
class Solution {
public:
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        if (envelopes.empty()) {
            return 0;
        }

        int n = envelopes.size();
        sort(envelopes.begin(), envelopes.end(), [](const auto& e1, const auto& e2) {
            return e1[0] < e2[0] || (e1[0] == e2[0] && e1[1] > e2[1]);
        });

        vector<int> f = {envelopes[0][1]};
        for (int i = 1; i < n; ++i) {
            if (int num = envelopes[i][1]; num > f.back()) {
                f.push_back(num);
            }
            else {
                auto it = lower_bound(f.begin(), f.end(), num);
                *it = num;
            }
        }
        return f.size();
    }
};
```

```java
// Java
class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if (envelopes.length == 0) {
            return 0;
        }

        int n = envelopes.length;
        Arrays.sort(envelopes, new Comparator<int[]>() {
            public int compare(int[] e1, int[] e2) {
                if (e1[0] != e2[0]) {
                    return e1[0] - e2[0];
                } else {
                    return e2[1] - e1[1];
                }
            }
        });

        List<Integer> f = new ArrayList<Integer>();
        f.add(envelopes[0][1]);
        for (int i = 1; i < n; ++i) {
            int num = envelopes[i][1];
            if (num > f.get(f.size() - 1)) {
                f.add(num);
            } else {
                int index = binarySearch(f, num);
                f.set(index, num);
            }
        }
        return f.size();
    }

    public int binarySearch(List<Integer> f, int target) {
        int low = 0, high = f.size() - 1;
        while (low < high) {
            int mid = (high - low) / 2 + low;
            if (f.get(mid) < target) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }
}
```

```py
# Python3
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            if (num := envelopes[i][1]) > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num

        return len(f)
```

```js
// JavaScript
var maxEnvelopes = function (envelopes) {
  if (envelopes.length === 0) {
    return 0;
  }

  const n = envelopes.length;
  envelopes.sort((e1, e2) => {
    if (e1[0] - e2[0]) {
      return e1[0] - e2[0];
    } else {
      return e2[1] - e1[1];
    }
  });

  const f = [envelopes[0][1]];
  for (let i = 1; i < n; ++i) {
    const num = envelopes[i][1];
    if (num > f[f.length - 1]) {
      f.push(num);
    } else {
      const index = binarySearch(f, num);
      f[index] = num;
    }
  }
  return f.length;
};

const binarySearch = (f, target) => {
  let low = 0,
    high = f.length - 1;
  while (low < high) {
    const mid = Math.floor((high - low) / 2) + low;
    if (f[mid] < target) {
      low = mid + 1;
    } else {
      high = mid;
    }
  }
  return low;
};
```

```golang
// Golang
func maxEnvelopes(envelopes [][]int) int {
    sort.Slice(envelopes, func(i, j int) bool {
        a, b := envelopes[i], envelopes[j]
        return a[0] < b[0] || a[0] == b[0] && a[1] > b[1]
    })

    f := []int{}
    for _, e := range envelopes {
        h := e[1]
        if i := sort.SearchInts(f, h); i < len(f) {
            f[i] = h
        } else {
            f = append(f, h)
        }
    }
    return len(f)
}
```

```c
// C
int cmp(int** a, int** b) {
    return (*a)[0] == (*b)[0] ? (*b)[1] - (*a)[1] : (*a)[0] - (*b)[0];
}

int lower_bound(int* arr, int arrSize, int val) {
    int left = 0, right = arrSize - 1;
    while (left <= right) {
        int mid = (left + right) >> 1;
        if (val < arr[mid]) {
            right = mid - 1;
        } else if (val > arr[mid]) {
            left = mid + 1;
        } else {
            return mid;
        }
    }
    if (arr[left] >= val) {
        return left;
    }
    return -1;
}

int maxEnvelopes(int** envelopes, int envelopesSize, int* envelopesColSize) {
    if (envelopesSize == 0) {
        return 0;
    }

    qsort(envelopes, envelopesSize, sizeof(int*), cmp);

    int n = envelopesSize;
    int f[n], fSize = 0;
    f[fSize++] = envelopes[0][1];
    for (int i = 1; i < n; ++i) {
        int num = envelopes[i][1];
        if (num > f[fSize - 1]) {
            f[fSize++] = num;
        } else {
            f[lower_bound(f, fSize, num)] = num;
        }
    }
    return fSize;
}
```

**复杂度分析**

- 时间复杂度：O(nlogn)，其中 n 是数组 envelopes 的长度，排序需要的时间复杂度为 O(nlogn)，动态规划需要的时间复杂度同样为 O(nlogn)。

= 空间复杂度：O(n)，即为数组 f 需要的空间。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/russian-doll-envelopes/solution/e-luo-si-tao-wa-xin-feng-wen-ti-by-leetc-wj68/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
