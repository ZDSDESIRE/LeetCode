### 154.寻找旋转排序数组中的最小值 II（困难）

假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组  [0,1,2,4,5,6,7] 可能变为  [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

注意数组中可能存在重复的元素。

示例 1：

```text
输入: [1,3,5]
输出: 1
```

示例  2：

```text
输入: [2,2,2,0,1]
输出: 0
```

说明：

- 这道题是 [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/) 的延伸题目。
- 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 二分查找（Binary Search） # 数组（String）
```

#### 提交

```py
# Python3
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[r]
```

#### 参考

同 [剑指 Offer 11. 旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)
