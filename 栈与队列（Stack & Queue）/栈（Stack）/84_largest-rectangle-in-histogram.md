### 84. 柱状图中的最大矩形（困难）

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
![histogram](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram.png)

以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为  [2,1,5,6,2,3]。
![histogram_area](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/histogram_area.png)

图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

示例:

```text
输入: [2,1,5,6,2,3]
输出: 10
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 栈（Stack）  # 数组（Array）
```

#### 提交

**伪代码**

```py
# Python3
    def largestRectangleArea(heights: List[int]) -> int:
        # 创建栈
        stack <- []
        # 遍历heights
        for i in range(length):
            # 满足while条件表明找到局部驼峰
            while stack is not empty and heights[i] smaller than stack top:
                # 逐次出栈
                p <- stack.pop(-1)
                # 找到一个可行解
                height, width <- heights[p], i-1-stack[-1]
                s <- max(s, width*height)
            # 不满足while条件，即要么stack为空，要么大于stack top
            stack.append(i)

        return s
```

**完整代码**

```py
# Python3
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 0:
            return 0

        stack, s = [], 0

        # 两头各插入1个哨兵
        heights.insert(0, 0)
        heights.append(0)
        length += 2

        for i in range(length):
            # 满足 while 意味着找到一个驼峰
            length_S = len(stack)
            while length_S != 0 and heights[i] < heights[stack[-1]]:
                p = stack.pop(-1)
                width = i - stack[-1] - 1
                height = heights[p]
                s = max(s, width * height)

            # 正在形成驼峰左侧
            stack.append(i)

        return s
```

#### 参考
