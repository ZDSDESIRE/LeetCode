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

##### 方法二：单调栈 + 常数优化

```c++
// C++
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n), right(n, n);

        stack<int> mono_stack;
        for (int i = 0; i < n; ++i) {
            while (!mono_stack.empty() && heights[mono_stack.top()] >= heights[i]) {
                right[mono_stack.top()] = i;
                mono_stack.pop();
            }
            left[i] = (mono_stack.empty() ? -1 : mono_stack.top());
            mono_stack.push(i);
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = max(ans, (right[i] - left[i] - 1) * heights[i]);
        }
        return ans;
    }
};
```

```java
// Java
class Solution {
    public int largestRectangleArea(int[] heights) {
        int n = heights.length;
        int[] left = new int[n];
        int[] right = new int[n];
        Arrays.fill(right, n);

        Stack<Integer> mono_stack = new Stack<Integer>();
        for (int i = 0; i < n; ++i) {
            while (!mono_stack.isEmpty() && heights[mono_stack.peek()] >= heights[i]) {
                right[mono_stack.peek()] = i;
                mono_stack.pop();
            }
            left[i] = (mono_stack.isEmpty() ? -1 : mono_stack.peek());
            mono_stack.push(i);
        }

        int ans = 0;
        for (int i = 0; i < n; ++i) {
            ans = Math.max(ans, (right[i] - left[i] - 1) * heights[i]);
        }
        return ans;
    }
}
```

```Py
# Python3
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [0] * n, [n] * n

        mono_stack = list()
        for i in range(n):
            while mono_stack and heights[mono_stack[-1]] >= heights[i]:
                right[mono_stack[-1]] = i
                mono_stack.pop()
            left[i] = mono_stack[-1] if mono_stack else -1
            mono_stack.append(i)

        ans = max((right[i] - left[i] - 1) * heights[i] for i in range(n)) if n > 0 else 0
        return ans
```

```golang
// Golang
func largestRectangleArea(heights []int) int {
    n := len(heights)
    left, right := make([]int, n), make([]int, n)
    for i := 0; i < n; i++ {
        right[i] = n
    }
    mono_stack := []int{}
    for i := 0; i < n; i++ {
        for len(mono_stack) > 0 && heights[mono_stack[len(mono_stack)-1]] >= heights[i] {
            right[mono_stack[len(mono_stack)-1]] = i
            mono_stack = mono_stack[:len(mono_stack)-1]
        }
        if len(mono_stack) == 0 {
            left[i] = -1
        } else {
            left[i] = mono_stack[len(mono_stack)-1]
        }
        mono_stack = append(mono_stack, i)
    }
    ans := 0
    for i := 0; i < n; i++ {
        ans = max(ans, (right[i] - left[i] - 1) * heights[i])
    }
    return ans
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
```

**复杂度分析**

- 时间复杂度：O(N)。

- 空间复杂度：O(N)。

**注**
作者：LeetCode-SolutionF
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/zhu-zhuang-tu-zhong-zui-da-de-ju-xing-by-leetcode-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
