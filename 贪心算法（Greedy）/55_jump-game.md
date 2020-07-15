### 55.跳跃游戏（中等）

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。

示例 1:

```text
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
```

示例 2:

```text
输入: [3,2,1,0,4]
输出: false
解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数组（Array）  # 贪心算法（Greedy）
```

#### 提交

```py
# Python3
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        max_len = 1
        while i < max_len:
            max_len = max(max_len, i + nums[i] + 1)
            if max_len >= len(nums):
                return True
            i += 1
        return False
```

#### 参考

##### 方法一：贪心

我们可以用贪心的方法解决这个问题。

设想一下，对于数组中的任意一个位置 y，我们如何判断它是否可以到达？根据题目的描述，只要存在一个位置 x，它本身可以到达，并且它跳跃的最大长度为 x + nums[x]，这个值大于等于 y，即 x + nums[x] ≥ y，那么位置 y 也可以到达。

换句话说，对于每一个可以到达的位置 x，它是的 x + 1, x + 2, ⋯, x + nums[x] 这些连续的位置都可以到达。

这样以来，我们依次遍历数组中的每一个位置，并实时维护最远可以到达的位置。对于当前遍历到的位置 x，如果它在 最远可以到达的位置的范围内，那么我们就可以从起点通过若干次跳跃到达该位置，因此我们可以用 x + nums[x] 更新最远可以到达的位置。

在遍历的过程中，如果最远可以到达的位置大于等于数组中的最后一个位置，那就说明最后一个位置可达，我们就可以直接返回 True 作为答案。反之，如果在遍历结束后，最后一个位置仍然不可达，我们就返回 False 作为答案。

以题目中的示例一 [2, 3, 1, 1, 4] 为例：

我们一开始在位置 0，可以跳跃的最大长度为 2，因此最远可以到达的位置被更新为 2；

我们遍历到位置 1，由于 1 ≤ 2，因此位置 1 可达。我们用 1 加上它可以跳跃的最大长度 3，将最远可以到达的位置更新为 4。由于 4 大于等于最后一个位置 4，因此我们直接返回 True。

我们再来看看题目中的示例二 [3, 2, 1, 0, 4]：

我们一开始在位置 00，可以跳跃的最大长度为 3，因此最远可以到达的位置被更新为 3；

我们遍历到位置 1，由于 1 ≤ 3，因此位置 1 可达，加上它可以跳跃的最大长度 2 得到 3，没有超过最远可以到达的位置；

位置 2、位置 3 同理，最远可以到达的位置不会被更新；

我们遍历到位置 4，由于 4 > 3，因此位置 4 不可达，我们也就不考虑它可以跳跃的最大长度了。

在遍历完成之后，位置 4 仍然不可达，因此我们返回 False。

```py
# Python3
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False
```

```c++
// C++
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int rightmost = 0;
        for (int i = 0; i < n; ++i) {
            if (i <= rightmost) {
                rightmost = max(rightmost, i + nums[i]);
                if (rightmost >= n - 1) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

```java
// Java
public class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        int rightmost = 0;
        for (int i = 0; i < n; ++i) {
            if (i <= rightmost) {
                rightmost = Math.max(rightmost, i + nums[i]);
                if (rightmost >= n - 1) {
                    return true;
                }
            }
        }
        return false;
    }
}
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 为数组的大小。只需要访问 nums 数组一遍，共 n 个位置。

- 空间复杂度：O(1)，不需要额外的空间开销。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/jump-game/solution/tiao-yue-you-xi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
