### 659.分割数组为连续子序列（中等）

给你一个按升序排序的整数数组 num（可能包含重复数字），请你将它们分割成一个或多个子序列，其中每个子序列都由连续整数组成且长度至少为 3 。

如果可以完成上述分割，则返回 true ；否则，返回 false 。

示例 1：

```text
输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3
3, 4, 5
```

示例 2：

```text
输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 :
1, 2, 3, 4, 5
3, 4, 5
```

示例 3：

```text
输入: [1,2,3,4,4,5]
输出: False
```

提示：

- 输入的数组长度范围为 [1, 10000]

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 堆（Heap）  # 贪心算法（Greedy）
```

#### 提交

```js
// JavaScript
var isPossible = function qiefen(nums) {
  var dp1 = 0,
    dp2 = 0,
    dp3 = 0,
    i = 0;
  while (i < nums.length) {
    var start = i,
      left;
    while (i < nums.length && nums[i] === nums[++i]) {}
    if (start > 0 && nums[start - 1] + 1 < nums[start]) {
      if (dp1 || dp2) return false;
      (dp1 = i - start), (dp3 = 0);
    } else {
      if ((left = i - start - dp1 - dp2) < 0) return false;
      var _dp2 = dp2;
      dp2 = dp1;
      if (left > dp3) {
        dp1 = left - dp3;
        dp3 = dp3 + _dp2;
      } else {
        dp1 = 0;
        dp3 = left + _dp2;
      }
    }
  }
  return dp1 === 0 && dp2 === 0;
};
```

#### 参考
