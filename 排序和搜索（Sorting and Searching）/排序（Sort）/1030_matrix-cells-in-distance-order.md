### 1030.距离顺序排列矩阵单元格（简单）

给出 R 行 C 列的矩阵，其中的单元格的整数坐标为(r, c)，满足 0 <= r < R 且 0 <= c < C。

另外，我们在该矩阵中给出了一个坐标为  (r0, c0) 的单元格。

返回矩阵中的所有单元格的坐标，并按到 (r0, c0) 的距离从最小到最大的顺序排，其中，两单元格(r1, c1) 和 (r2, c2) 之间的距离是曼哈顿距离，|r1 - r2| + |c1 - c2|。（你可以按任何满足此条件的顺序返回答案。）

示例 1：

```text
输入：R = 1, C = 2, r0 = 0, c0 = 0
输出：[[0,0],[0,1]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1]
```

示例 2：

```text
输入：R = 2, C = 2, r0 = 0, c0 = 1
输出：[[0,1],[0,0],[1,1],[1,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。
```

示例 3：

```text
输入：R = 2, C = 3, r0 = 1, c0 = 2
输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。
```

提示：

- 1 <= R <= 100
- 1 <= C <= 100
- 0 <= r0 < R
- 0 <= c0 < C

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-cells-in-distance-order
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 排序（Sort）
```

#### 提交

```js
// 直接排序
/**
 * @param {number} R
 * @param {number} C
 * @param {number} r0
 * @param {number} c0
 * @return {number[][]}
 */
var allCellsDistOrder = function (R, C, r0, c0) {
  let res = [];
  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      res.push([i, j]);
    }
  }
  return res.sort(
    (a, b) =>
      Math.abs(a[0] - r0) +
      Math.abs(a[1] - c0) -
      (Math.abs(b[0] - r0) + Math.abs(b[1] - c0))
  );
};
```

```js
// 使用 Array.prototype.flat 扁平化处理二维数组
/**
 * @param {number} R
 * @param {number} C
 * @param {number} r0
 * @param {number} c0
 * @return {number[][]}
 */
var allCellsDistOrder = function (R, C, r0, c0) {
  let _result = [];
  for (let i = 0; i < R; i++) {
    for (let j = 0; j < C; j++) {
      const val = Math.abs(i - r0) + Math.abs(j - c0);
      if (_result[val]) {
        _result[val].push([i, j]);
      } else {
        _result[val] = [[i, j]];
      }
    }
  }
  return _result.flat();
};
```

#### 参考

##### 方法一：直接排序

**思路及解法**

最容易想到的方法是首先存储矩阵内所有的点，然后将其按照哈曼顿距离直接排序。

**代码**

```c++
// C++
class Solution {
public:
    vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
        vector<vector<int>> ret;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                ret.push_back({i, j});
            }
        }
        sort(ret.begin(), ret.end(), [=](vector<int>& a, vector<int>& b) {
            return abs(a[0] - r0) + abs(a[1] - c0) < abs(b[0] - r0) + abs(b[1] - c0);
        });
        return ret;
    }
};
```

```java
// Java
class Solution {
    public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
        int[][] ret = new int[R * C][];
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                ret[i * C + j] = new int[]{i, j};
            }
        }
        Arrays.sort(ret, new Comparator<int[]>() {
            public int compare(int[] a, int[] b) {
                return (Math.abs(a[0] - r0) + Math.abs(a[1] - c0)) - (Math.abs(b[0] - r0) + Math.abs(b[1] - c0));
            }
        });
        return ret;
    }
}
```

```py
# Python3
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        ret = [(i, j) for i in range(R) for j in range(C)]
        ret.sort(key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
        return ret
```

```golang
// Golang
func allCellsDistOrder(n, m, r0, c0 int) [][]int {
    ans := make([][]int, 0, n*m)
    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            ans = append(ans, []int{i, j})
        }
    }
    sort.Slice(ans, func(i, j int) bool {
        a, b := ans[i], ans[j]
        return abs(a[0]-r0)+abs(a[1]-c0) < abs(b[0]-r0)+abs(b[1]-c0)
    })
    return ans
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

```c
// C
int R0, C0;

int cmp(void* _a, void* _b) {
    int *a = *(int**)_a, *b = *(int**)_b;
    return fabs(a[0] - R0) + fabs(a[1] - C0) - fabs(b[0] - R0) - fabs(b[1] - C0);
}

int** allCellsDistOrder(int R, int C, int r0, int c0, int* returnSize, int** returnColumnSizes) {
    R0 = r0, C0 = c0;
    int** ret = malloc(sizeof(int*) * R * C);
    *returnColumnSizes = malloc(sizeof(int) * R * C);
    for (int i = 0; i < R * C; i++) {
        (*returnColumnSizes)[i] = 2;
        ret[i] = malloc(sizeof(int) * 2);
    }
    *returnSize = 0;
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            ret[*returnSize][0] = i;
            ret[*returnSize][1] = j;
            (*returnSize)++;
        }
    }
    qsort(ret, R * C, sizeof(int*), cmp);
    return ret;
}
```

**复杂度分析**

- 时间复杂度：O(RC log(RC))，存储所有点时间复杂度 O(RC)，排序时间复杂度 O(RC log(RC))。

- 空间复杂度：O(log(RC))，即为排序需要使用的栈空间，不考虑返回值的空间占用。

##### 方法二：桶排序

**思路及解法**

注意到方法一中排序的时间复杂度太高。实际在枚举所有点时，我们可以直接按照哈曼顿距离分桶。这样我们就可以实现线性的桶排序。

```c++
// C++
class Solution {
public:
    int dist(int r1, int c1, int r2, int c2) {
        return abs(r1 - r2) + abs(c1 - c2);
    }

    vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
        int maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0);
        vector<vector<vector<int>>> bucket(maxDist + 1);

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                int d = dist(i, j, r0, c0);
                vector<int> tmp = {i, j};
                bucket[d].push_back(move(tmp));
            }
        }
        vector<vector<int>> ret;
        for (int i = 0; i <= maxDist; i++) {
            for (auto &it : bucket[i]) {
                ret.push_back(it);
            }
        }
        return ret;
    }
};
```

```java
// Java
class Solution {
    public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
        int maxDist = Math.max(r0, R - 1 - r0) + Math.max(c0, C - 1 - c0);
        List<List<int[]>> bucket = new ArrayList<List<int[]>>();
        for (int i = 0; i <= maxDist; i++) {
            bucket.add(new ArrayList<int[]>());
        }

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                int d = dist(i, j, r0, c0);
                bucket.get(d).add(new int[]{i, j});
            }
        }
        int[][] ret = new int[R * C][];
        int index = 0;
        for (int i = 0; i <= maxDist; i++) {
            for (int[] it : bucket.get(i)) {
                ret[index++] = it;
            }
        }
        return ret;
    }

    public int dist(int r1, int c1, int r2, int c2) {
        return Math.abs(r1 - r2) + Math.abs(c1 - c2);
    }
}
```

```golang
// Golang
func allCellsDistOrder(n, m, r0, c0 int) [][]int {
    maxDist := max(r0, n-1-r0) + max(c0, m-1-c0)
    buckets := make([][][]int, maxDist+1)

    for i := 0; i < n; i++ {
        for j := 0; j < m; j++ {
            dist := abs(i-r0) + abs(j-c0)
            buckets[dist] = append(buckets[dist], []int{i, j})
        }
    }

    ans := make([][]int, 0, n*m)
    for _, bucket := range buckets {
        ans = append(ans, bucket...)
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}
```

```py
# Python3
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        bucket = collections.defaultdict(list)
        dist = lambda r1, c1, r2, c2: abs(r1 - r2) + abs(c1 - c2)

        for i in range(R):
            for j in range(C):
                bucket[dist(i, j, r0, c0)].append([i, j])

        ret = list()
        for i in range(maxDist + 1):
            ret.extend(bucket[i])

        return ret
```

```c
// C
int dist(int r1, int c1, int r2, int c2) {
    return fabs(r1 - r2) + fabs(c1 - c2);
}

int** allCellsDistOrder(int R, int C, int r0, int c0, int* returnSize, int** returnColumnSizes) {
    int maxDist = fmax(r0, R - 1 - r0) + fmax(c0, C - 1 - c0);
    int* bucket[maxDist + 1][2 * (R + C)];
    int bucketSize[maxDist + 1];
    memset(bucketSize, 0, sizeof(bucketSize));
    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            int d = dist(i, j, r0, c0);
            int* tmp = malloc(sizeof(int) * 2);
            tmp[0] = i, tmp[1] = j;
            bucket[d][bucketSize[d]++] = tmp;
        }
    }

    int** ret = malloc(sizeof(int*) * R * C);
    *returnColumnSizes = malloc(sizeof(int) * R * C);
    for (int i = 0; i < R * C; i++) {
        (*returnColumnSizes)[i] = 2;
    }
    *returnSize = 0;
    for (int i = 0; i <= maxDist; i++) {
        for (int j = 0; j < bucketSize[i]; j++) {
            ret[(*returnSize)++] = bucket[i][j];
        }
    }
    return ret;
}
```

**复杂度分析**

- 时间复杂度：O(RC)，存储所有点时间复杂度 O(RC)，桶排序时间复杂度 O(RC)。

- 空间复杂度：O(RC)，需要存储矩阵内所有点。

##### 方法三：几何法

**思路及解法**

我们也可以直接变换枚举矩阵的顺序，直接按照曼哈顿距离遍历该矩形即可。

注意到曼哈顿距离相同的位置恰好构成一个斜着的正方形边框，因此我们可以从小到大枚举曼哈顿距离，并使用循环来直接枚举该距离对应的边框。我们每次从该正方形边框的上顶点出发，依次经过右顶点、下顶点和左顶点，最后回到上顶点。这样即可完成当前层的遍历。
![1](https://assets.leetcode-cn.com/solution-static/1030/1.png)
注意正方形边框中的部分点不一定落在矩阵中，所以我们需要做好边界判断。

**代码**

```c++
// C++
class Solution {
public:
    const int dr[4] = {1, 1, -1, -1};
    const int dc[4] = {1, -1, -1, 1};

    vector<vector<int>> allCellsDistOrder(int R, int C, int r0, int c0) {
        int maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0);
        vector<vector<int>> ret;
        int row = r0, col = c0;
        ret.push_back({row, col});
        for (int dist = 1; dist <= maxDist; dist++) {
            row--;
            for (int i = 0; i < 4; i++) {
                while ((i % 2 == 0 && row != r0) || (i % 2 != 0 && col != c0)) {
                    if (row >= 0 && row < R && col >= 0 && col < C) {
                        ret.push_back({row, col});
                    }
                    row += dr[i];
                    col += dc[i];
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
    int[] dr = {1, 1, -1, -1};
    int[] dc = {1, -1, -1, 1};

    public int[][] allCellsDistOrder(int R, int C, int r0, int c0) {
        int maxDist = Math.max(r0, R - 1 - r0) + Math.max(c0, C - 1 - c0);
        int[][] ret = new int[R * C][];
        int row = r0, col = c0;
        int index = 0;
        ret[index++] = new int[]{row, col};
        for (int dist = 1; dist <= maxDist; dist++) {
            row--;
            for (int i = 0; i < 4; i++) {
                while ((i % 2 == 0 && row != r0) || (i % 2 != 0 && col != c0)) {
                    if (row >= 0 && row < R && col >= 0 && col < C) {
                        ret[index++] = new int[]{row, col};
                    }
                    row += dr[i];
                    col += dc[i];
                }
            }
        }
        return ret;
    }
}
```

```golang
// Golang
var dir4 = [][2]int{{1, 1}, {1, -1}, {-1, -1}, {-1, 1}}

func allCellsDistOrder(n, m, r0, c0 int) [][]int {
    ans := make([][]int, 1, n*m)
    ans[0] = []int{r0, c0}
    maxDist := max(r0, n-1-r0) + max(c0, m-1-c0)
    row, col := r0, c0
    for dist := 1; dist <= maxDist; dist++ {
        row--
        for i, dir := range dir4 {
            for i%2 == 0 && row != r0 || i%2 == 1 && col != c0 {
                if 0 <= row && row < n && 0 <= col && col < m {
                    ans = append(ans, []int{row, col})
                }
                row += dir[0]
                col += dir[1]
            }
        }
    }
    return ans
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

```py
# Python3
class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        maxDist = max(r0, R - 1 - r0) + max(c0, C - 1 - c0)
        row, col = r0, c0
        ret = [[row, col]]
        for dist in range(1, maxDist + 1):
            row -= 1
            for i, (dr, dc) in enumerate(dirs):
                while (i % 2 == 0 and row != r0) or (i % 2 != 0 and col != c0):
                    if 0 <= row < R and 0 <= col < C:
                        ret.append([row, col])
                    row += dr
                    col += dc
        return ret
```

```c
// C
const int dr[4] = {1, 1, -1, -1};
const int dc[4] = {1, -1, -1, 1};

int** allCellsDistOrder(int R, int C, int r0, int c0, int* returnSize, int** returnColumnSizes) {
    int maxDist = fmax(r0, R - 1 - r0) + fmax(c0, C - 1 - c0);

    int** ret = malloc(sizeof(int*) * R * C);
    *returnColumnSizes = malloc(sizeof(int) * R * C);
    for (int i = 0; i < R * C; i++) {
        (*returnColumnSizes)[i] = 2;
    }

    int row = r0, col = c0;
    *returnSize = 0;
    int* tmp = malloc(sizeof(int) * 2);
    tmp[0] = row, tmp[1] = col;
    ret[(*returnSize)++] = tmp;
    for (int dist = 1; dist <= maxDist; dist++) {
        row--;
        for (int i = 0; i < 4; i++) {
            while ((i % 2 == 0 && row != r0) || (i % 2 != 0 && col != c0)) {
                if (row >= 0 && row < R && col >= 0 && col < C) {
                    int* tmps = malloc(sizeof(int) * 2);
                    tmps[0] = row, tmps[1] = col;
                    ret[(*returnSize)++] = tmps;
                }
                row += dr[i];
                col += dc[i];
            }
        }
    }
    return ret;
}
```

**复杂度分析**

- 时间复杂度：O((R+C)^2)，我们需要遍历矩阵内所有点，同时也会遍历部分超过矩阵部分的点。在最坏情况下，给定的单元格位于矩阵的一个角，例如 (0,0)，此时最大的曼哈顿距离为 R+C-2，需要遍历的点数为 2(R+C-2)(R+C-1)+1，因此时间复杂度为 O((R+C)^2)。

- 空间复杂度：O(1)，不考虑返回值的空间占用。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/matrix-cells-in-distance-order/solution/ju-chi-shun-xu-pai-lie-ju-zhen-dan-yuan-ge-by-leet/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
