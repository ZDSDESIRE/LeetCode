# 892.三维形体的表面积
'''
在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。
每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
请你返回最终形体的表面积。

示例 1：
输入：[[2]]
输出：10

示例 2：
输入：[[1,2],[3,4]]
输出：34

示例 3：
输入：[[1,0],[0,2]]
输出：16

示例 4：
输入：[[1,1,1],[1,0,1],[1,1,1]]
输出：32

示例 5：
输入：[[2,2,2],[2,1,2],[2,2,2]]
输出：46
 

提示：
1 <= N <= 50
0 <= grid[i][j] <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 优秀源码
'''
方法：分块累加

思路
让我们试着计算 v = grid[i][j] 所贡献的表面积。
当 v > 0 时，顶面和底面的面积之和为 2。
然后，对于列 grid[i][j] 的每一侧（西，北，东，南），值为 nv 的相邻单元意味着这些方块贡献了 max(v - nv, 0) 的面积。
例如，对于 grid = [[1, 5]]，grid[0][1] 贡献的表面积是 2 + 5 + 5 + 5 + 4。其中 2 来自顶部和底部；5 来自北、东、南三面；4 来自西面，其中 1 个单位被邻列覆盖。

算法
对于每个 v = grid[r][c] > 0，计算 ans += 2，对于 grid[r][c] 附近的每个相邻值 nv 还要加上 ans += max(v - nv, 0)。

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

复杂度分析
时间复杂度：O(N^2)，其中 N 是 grid 中的行和列的数目。
空间复杂度：O(1)。

作者：LeetCode
链接：https://leetcode-cn.com/problems/surface-area-of-3d-shapes/solution/san-wei-xing-ti-de-biao-mian-ji-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

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