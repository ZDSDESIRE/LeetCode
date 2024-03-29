### 852. 山脉数组的峰顶索引（简单）

符合下列属性的数组 arr 称为 山脉数组 ：

- arr.length >= 3
- 存在 i（0 < i < arr.length - 1）使得：
  - arr[0] < arr[1] < ... arr[i-1] < arr[i]
  - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

给你由整数组成的山脉数组 arr ，返回任何满足 arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1] 的下标 i 。

示例 1：

```text
输入：arr = [0,1,0]
输出：1
```

示例 2：

```text
输入：arr = [0,2,1,0]
输出：1
```

示例 3：

```text
输入：arr = [0,10,5,2]
输出：1
```

示例 4：

```text
输入：arr = [3,4,5,1]
输出：2
```

示例 5：

```text
输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2
```

提示：

- 3 <= arr.length <= 104
- 0 <= arr[i] <= 106
- 题目数据保证 arr 是一个山脉数组

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/peak-index-in-a-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 二分查找（Binary Search）
```

### 提交

```py
# Python3
# 枚举 —— 时间复杂度O(n)，空间复杂度O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        ans = -1

        for i in range(1, n - 1):
            if arr[i] > arr[i + 1]:
                ans = i
                break

        return ans
```

```js
// JavaScript
// 二分查找 —— 时间复杂度O(log n)，空间复杂度O(1)
/**
 * @param {number[]} arr
 * @return {number}
 */
var peakIndexInMountainArray = function (arr) {
  let left = 0,
    right = arr.length - 1,
    ans = -1;

  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] < arr[mid + 1]) {
      left = mid + 1;
    } else {
      right = mid - 1;
      ans = mid;
    }
  }
  return ans;
};
```
