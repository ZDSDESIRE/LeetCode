### 152. 乘积最大子数组（中等）

给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

示例 1:

```text
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
```

示例 2:

```text
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数组（Array）  # 动态规划（DP）
```

#### 提交

#### 参考

##### 方法一：动态规划

**思路和算法**

如果我们用 f_max(i) 开表示以第 i 个元素结尾的乘积最大子数组的乘积，a 表示输入参数 nums，那么根据「[53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/)」的经验，我们很容易推导出这样的状态转移方程：

```text
            n
f_max(i) = max { f(i - 1) × a_i, a_i}
           i=1
```

它表示以第 i 个元素结尾的乘积最大子数组的乘积可以考虑 a_i 加入前面的 f_max(i - 1) 对应的一段，或者单独成为一段，这里两种情况下取最大值。求出所有的 f_max(i) 之后选取最大的一个作为答案。

**可是在这里，这样做是错误的。为什么呢？**

因为这里的定义并不满足「最优子结构」。具体地讲，如果 a = { 5, 6, -3, 4, -3 }，那么此时 f_max 对应的序列是 { 5, 30, -3, 4, -3 }，按照前面的算法我们可以得到答案为 30，即前两个数的乘积，而实际上答案应该是全体数字的乘积。我们来想一想问题出在哪里呢？问题出在最后一个 -3−3 所对应的 f_max
的值既不是 -3，也不是 4 × (−3)，而是 5 × 30 × (−3) × 4 ×(−3)。所以我们得到了一个结论：当前位置的最优解未必是由前一个位置的最优解转移得到的。

**我们可以根据正负性进行分类讨论。**

考虑当前位置如果是一个负数的话，那么我们希望以它前一个位置结尾的某个段的积也是个负数，这样就可以负负得正，并且我们希望这个积尽可能「负得更多」，即尽可能小。如果当前位置是一个正数的话，我们更希望以它前一个位置结尾的某个段的积也是个正数，并且希望它尽可能地大。于是这里我们可以再维护一个 f_min(i)，它表示以第 i 个元素结尾的乘积最小子数组的乘积，那么我们可以得到这样的动态规划转移方程：

```text
            n
f_max(i) = max { f_max(i - 1) × a_i, f_min(i - 1) × a_i, a_i}
           i=1
            n
f_min(i) = min { f_max(i - 1) × a_i, f_min(i - 1) × a_i, a_i}
           i=1
```

它代表第 i 个元素结尾的乘积最大子数组的乘积 f_max(i)，可以考虑把 a_i 加入第 i - 1 个元素结尾的乘积最大或最小的子数组的乘积中，二者加上 a_i，三者取大，就是第 i 个元素结尾的乘积最大子数组的乘积。第 i 个元素结尾的乘积最小子数组的乘积 f_min(i) 同理。

不难给出这样的实现：

```c++
// C++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector <int> maxF(nums), minF(nums);
        for (int i = 1; i < nums.size(); ++i) {
            maxF[i] = max(maxF[i - 1] * nums[i], max(nums[i], minF[i - 1] * nums[i]));
            minF[i] = min(minF[i - 1] * nums[i], min(nums[i], maxF[i - 1] * nums[i]));
        }
        return *max_element(maxF.begin(), maxF.end());
    }
};
```

易得这里的渐进时间复杂度和渐进空间复杂度都是 O(n)。

**考虑优化空间**。

由于第 i 个状态只和第 i - 1 个状态相关，根据「滚动数组」思想，我们可以只用两个变量来维护 i - 1 时刻的状态，一个维护 f_max，一个维护 f_min。细节参见代码。

```c++
// C++
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxF = nums[0], minF = nums[0], ans = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int mx = maxF, mn = minF;
            maxF = max(mx * nums[i], max(nums[i], mn * nums[i]));
            minF = min(mn * nums[i], min(nums[i], mx * nums[i]));
            ans = max(maxF, ans);
        }
        return ans;
    }
};
```

```golang
// Golang
func maxProduct(nums []int) int {
    maxF, minF, ans := nums[0], nums[0], nums[0]
    for i := 1; i < len(nums); i++ {
        mx, mn := maxF, minF
        maxF = max(mx * nums[i], max(nums[i], mn * nums[i]))
        minF = min(mn * nums[i], min(nums[i], mx * nums[i]))
        ans = max(maxF, ans)
    }
    return ans
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
```

**复杂度分析**

记 nums 元素个数为 n。

- 时间复杂度：程序一次循环遍历了 nums，故渐进时间复杂度为 O(n)。

- 空间复杂度：优化后只使用常数个临时变量作为辅助空间，与 n 无关，故渐进空间复杂度为 O(1)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/maximum-product-subarray/solution/cheng-ji-zui-da-zi-shu-zu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
