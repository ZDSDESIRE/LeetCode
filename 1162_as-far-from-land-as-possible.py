# 1162.地图分析
'''
你现在手里有一份大小为 N x N 的『地图』（网格） grid，上面的每个『区域』（单元格）都用 0 和 1 标记好了。其中 0 代表海洋，1 代表陆地，你知道距离陆地区域最远的海洋区域是是哪一个吗？请返回该海洋区域到离它最近的陆地区域的距离。
我们这里说的距离是『曼哈顿距离』（ Manhattan Distance）：(x0, y0) 和 (x1, y1) 这两个区域之间的距离是 |x0 - x1| + |y0 - y1| 。
如果我们的地图上只有陆地或者海洋，请返回 -1。

示例 1：
输入：[[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释： 
海洋区域 (1, 1) 和所有陆地区域之间的距离都达到最大，最大距离为 2。

示例 2：
输入：[[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释： 
海洋区域 (2, 2) 和所有陆地区域之间的距离都达到最大，最大距离为 4。
 
提示：
1 <= grid.length == grid[0].length <= 100
grid[i][j] 不是 0 就是 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

# 优秀源码
'''
解题思路
1.Try to find the location of each island
2.if there is no land or water in this grid, return -1
3.we just use while loop till all elements would be droped off
4.inside the while loop, we could use for loop to look though all directions and redefine these values
 
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        result = []
        for i in range(m):
            for w in range(n):
                if grid[i][w] == 1:
                    result.append((i,w))
                else:
                    grid[i][w] = 0      
        if len(result) == 0 or len(result) == m * n:
            return -1
        count = 0
        while result:
            count += 1  
            for i in range(len(result)):
                x, y = result.pop(0)
                if x + 1 < m and grid[x+1][y] == 0:
                    result.append((x+1, y))
                    grid[x+1][y] = -1
                if x - 1 >= 0 and grid[x-1][y] == 0:
                    result.append((x-1, y))
                    grid[x-1][y] = -1
                if y + 1 < n and grid[x][y+1] == 0:
                    result.append((x, y+1))
                    grid[x][y+1] = -1
                if y - 1 >= 0 and grid[x][y-1] == 0:
                    result.append((x, y-1))
                    grid[x][y-1] = -1
        return count - 1

作者：leetcode_cnnn
链接：https://leetcode-cn.com/problems/as-far-from-land-as-possible/solution/jue-dui-de-yi-kan-jiu-dong-easy-version-by-leetcod/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        steps = -1
        queue = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]
        if len(queue) == 0 or len(queue) == n ** 2: return steps
        while len(queue) > 0:
            for _ in range(len(queue)): 
                x, y = queue.pop(0)
                for xi, yj in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                    if xi >= 0 and xi < n and yj >= 0 and yj < n and grid[xi][yj] == 0:
                        queue.append((xi, yj))
                        grid[xi][yj] = -1
            steps += 1
                
        return steps
