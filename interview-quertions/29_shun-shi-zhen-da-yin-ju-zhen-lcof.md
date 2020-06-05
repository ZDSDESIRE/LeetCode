### 面试题 29.顺时针打印矩阵（简单）

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

示例 1：

```text
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
```

示例 2：

```text
输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
```

限制：

- 0 <= matrix.length <= 100
- 0 <= matrix[i].length <= 100
  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 提交

```py
# Python3
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
```

#### 参考
