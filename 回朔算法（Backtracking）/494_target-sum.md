### 494. 目标和（中等）

给你一个整数数组 nums 和一个整数 target 。

向数组中的每个整数前添加  '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ：

- 例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。

返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。

示例 1：

```text
输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
```

示例 2：

```text
输入：nums = [1], target = 1
输出：1
```

提示：

- 1 <= nums.length <= 20
- 0 <= nums[i] <= 1000
- 0 <= sum(nums[i]) <= 1000
- -1000 <= target <= 1000

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 回溯算法（Backtracking）  # 动态规划（DP）
```

#### 提交

```js
// JavaScript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var findTargetSumWays = function (nums, target) {
  let count = 0;
  const backTrack = (nums, target, index, sum) => {
    if (index === nums.length) {
      if (sum === target) {
        count++;
      }
    } else {
      backTrack(nums, target, index + 1, sum + nums[index]);
      backTrack(nums, target, index + 1, sum - nums[index]);
    }
  };
  backTrack(nums, target, 0, 0);
  return count;
};
```

**复杂度分析**

- 时间复杂度：O(2^n)，其中 n 是数组 nums 的长度。回溯需要遍历所有不同的表达式，共有 2^n 种不同的表达式，每种表达式计算结果需要 O(1) 的时间，因此总时间复杂度是 O(2^n)。

- 空间复杂度：O(n)，其中 n 是数组 nums 的长度。空间复杂度主要取决于递归调用的栈空间，栈的深度不超过 n。
