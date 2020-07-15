# 892.三维形体的表面积（简单）

在 N * N 的网格上，我们放置一些 1 * 1 \* 1 的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

示例 1：

```text
输入：[[2]]
输出：10
```

示例 2：

```text
输入：[[1,2],[3,4]]
输出：34
```

示例 3：

```text
输入：[[1,0],[0,2]]
输出：16
```

示例 4：

```text
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32
```

示例  5：

```text
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46
```

提示：

```text
1 <= N <= 50
0 <= grid[i][j] <= 50
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数学（Math)
```

#### 提交

```py
# Python3
# 解题思路：
1、每个正方体有六个面（n*6）
2、上下重叠的两个正方体会减少两个接触面
3、而左右重叠的则减少一个接触面

class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        L = len(grid)
        n = dec = 0
        for i in range(L):
            for j in range(L):
                n += grid[i][j]
                if grid[i][j] > 1:
                    dec += (grid[i][j] - 1) * 2
                if i - 1 >= 0:
                    dec += min(grid[i][j], grid[i-1][j])
                if i + 1 < L:
                    dec += min(grid[i][j], grid[i+1][j])
                if j - 1 >= 0:
                    dec += min(grid[i][j], grid[i][j-1])
                if j + 1 < L:
                    dec += min(grid[i][j], grid[i][j+1])
        return n * 6 - dec
```

#### 参考

##### 方法一：分块累加

**思路**

让我们试着计算 v = grid[i][j] 所贡献的表面积，再将所有的 v 值相加就能得到最终形体的表面积：

- 对于四个侧面的表面积，只有在相邻位置的高度小于 v 时，对应的那个侧面才会贡献表面积，且贡献的数量为 v - nv，其中 nv 是相邻位置的高度。我们可以将其写成 max(v - nv, 0)。

举一个例子，对于网格

```text
1 5
6 7
```

而言，位置 grid[0][1] 的高度为 5：

- 因为 5 > 0，所以贡献了 2 的顶面和底面表面积；

- 该位置的上方和右侧没有单元格，可以看成高度为 0，所以分别贡献了 max(5 - 0, 0) = 5 的表面积；

- 该位置的左侧高度为 1，所以贡献了 max(5 - 1, 0) = 4 的表面积；

- 该位置的下方高度为 7，所以贡献了 max(5 - 7, 0) = 0 的表面积。

因此 grid[0][1] 贡献的表面积总和为 2 + 5 + 5 + 4 + 0 = 16。

算法
对于每个 v = grid[r][c] > 0，计算 ans += 2，对于 grid[r][c] 附近的每个相邻值 nv 还要加上 ans += max(v - nv, 0)。

```py
# Python3
class Solution(object):
    def surfaceArea(self, grid):
        N = len(grid)
        ans = 0
        for r in xrange(N):
            for c in xrange(N):
                if grid[r][c]:
                    ans += 2
                    for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r,c+1)):
                        if 0 <= nr < N and 0 <= nc < N:
                            nval = grid[nr][nc]
                        else:
                            nval = 0

                        ans += max(grid[r][c] - nval, 0)
        return ans
```

```c++
// C++
class Solution {
public:
    int surfaceArea(vector<vector<int>>& grid) {
        int dr[]{0, 1, 0, -1};
        int dc[]{1, 0, -1, 0};

        int N = grid.size();
        int ans = 0;

        for (int r = 0; r < N; ++r)
            for (int c = 0; c < N; ++c)
                if (grid[r][c] > 0) {
                    ans += 2;
                    for (int k = 0; k < 4; ++k) {
                        int nr = r + dr[k];
                        int nc = c + dc[k];
                        int nv = 0;
                        if (0 <= nr && nr < N && 0 <= nc && nc < N)
                            nv = grid[nr][nc];

                        ans += max(grid[r][c] - nv, 0);
                    }
                }

        return ans;
    }
};
```

```java
// Java
class Solution {
    public int surfaceArea(int[][] grid) {
        int[] dr = new int[]{0, 1, 0, -1};
        int[] dc = new int[]{1, 0, -1, 0};

        int N = grid.length;
        int ans = 0;

        for (int r = 0; r < N; ++r)
            for (int c = 0; c < N; ++c)
                if (grid[r][c] > 0) {
                    ans += 2;
                    for (int k = 0; k < 4; ++k) {
                        int nr = r + dr[k];
                        int nc = c + dc[k];
                        int nv = 0;
                        if (0 <= nr && nr < N && 0 <= nc && nc < N)
                            nv = grid[nr][nc];

                        ans += Math.max(grid[r][c] - nv, 0);
                    }
                }

        return ans;
    }
}
```

```js
// JavaScript
var surfaceArea = function (grid) {
  const dr = [0, 1, 0, -1]
  const dc = [1, 0, -1, 0]

  const N = grid.length
  let ans = 0

  for (let r = 0; r < N; ++r) {
    for (let c = 0; c < N; ++c) {
      if (grid[r][c] > 0) {
        ans += 2
        for (let k = 0; k < 4; ++k) {
          const nr = r + dr[k]
          const nc = c + dc[k]
          let nv = 0
          if (0 <= nr && nr < N && 0 <= nc && nc < N) {
            nv = grid[nr][nc]
          }

          ans += Math.max(grid[r][c] - nv, 0)
        }
      }
    }
  }

  return ans
}
```

**复杂度分析**

- 时间复杂度：O(N^2)，其中 N 是 grid 中的行和列的数目。
- 空间复杂度：O(1)。

**注**

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes/solution/san-wei-xing-ti-de-biao-mian-ji-by-leetcode-soluti/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''
