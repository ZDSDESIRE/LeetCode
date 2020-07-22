### 剑指 Offer 11.旋转数组的最小数字（简单）

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为 1。

示例 1：

```text
输入：[3,4,5,1,2]
输出：1
```

示例 2：

```text
输入：[2,2,2,0,1]
输出：0
```

注意：本题与主站 [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/)相同

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 二分查找（Binary Search） # 数组（String）
```

#### 提交

```py
# Python3
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1

        while l < r:
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[r]:
                r = mid
            else:
                r -= 1
        return numbers[r]
```

#### 参考

**前言**
本题和 [154. 寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/) 完全相同，是 [153. 寻找旋转排序数组中的最小值](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/) 的延伸。读者可以先尝试 153 题，体会在旋转数组中进行二分查找的思路，再来尝试解决本题。

##### 方法一：二分查找

**思路与算法**

一个包含重复元素的升序数组在经过旋转之后，可以得到下面可视化的折线图：
![1](https://assets.leetcode-cn.com/solution-static/jianzhi_11/1.png)

其中横轴表示数组元素的下标，纵轴表示数组元素的值。图中标出了最小值的位置，是我们需要旋转的目标。

我们考虑数组中的最后一个元素 x：在最小值右侧的元素，它们的值一定都小于等于 xx；而在最小值左侧的元素，它们的值一定都大于等于 xx。因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。

在二分查找的每一步中，左边界为 low，右边界为 high，区间的中点为 pivot，最小值就在该区间内。我们将中轴元素 numbers[pivot] 与右边界元素 numbers[high] 进行比较，可能会有以下的三种情况：

第一种情况是 numbers[pivot] < numbers[high]。如下图所示，这说明 numbers[pivot] 是最小值右侧的元素，因此我们可以忽略二分查找区间的右半部分。
![2](https://assets.leetcode-cn.com/solution-static/jianzhi_11/2.png)

第二种情况是 numbers[pivot] > numbers[high]。如下图所示，这说明 numbers[pivot] 是最小值左侧的元素，因此我们可以忽略二分查找区间的左半部分。
![3](https://assets.leetcode-cn.com/solution-static/jianzhi_11/3.png)

第三种情况是 numbers[pivot] == numbers[high]。如下图所示，由于重复元素的存在，我们并不能确定 numbers[pivot] 究竟在最小值的左侧还是右侧，因此我们不能莽撞地忽略某一部分的元素。我们唯一可以知道的是，由于它们的值相同，所以无论 numbers[high] 是不是最小值，都有一个它的「替代品」numbers[pivot]，因此我们可以忽略二分查找区间的右端点。
![4](https://assets.leetcode-cn.com/solution-static/jianzhi_11/4.png)

当二分查找结束时，我们就得到了最小值所在的位置。

```py
# Python3
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]
```

```c++
// C++
class Solution {
public:
    int minArray(vector<int>& numbers) {
        int low = 0;
        int high = numbers.size() - 1;
        while (low < high) {
            int pivot = low + (high - low) / 2;
            if (numbers[pivot] < numbers[high]) {
                high = pivot;
            }
            else if (numbers[pivot] > numbers[high]) {
                low = pivot + 1;
            }
            else {
                high -= 1;
            }
        }
        return numbers[low];
    }
};
```

```java
// Java
class Solution {
    public int minArray(int[] numbers) {
        int low = 0;
        int high = numbers.length - 1;
        while (low < high) {
            int pivot = low + (high - low) / 2;
            if (numbers[pivot] < numbers[high]) {
                high = pivot;
            } else if (numbers[pivot] > numbers[high]) {
                low = pivot + 1;
            } else {
                high -= 1;
            }
        }
        return numbers[low];
    }
}
```

```c
// C
int minArray(int* numbers, int numbersSize) {
    int low = 0;
    int high = numbersSize - 1;
    while (low < high) {
        int pivot = low + (high - low) / 2;
        if (numbers[pivot] < numbers[high]) {
            high = pivot;
        } else if (numbers[pivot] > numbers[high]) {
            low = pivot + 1;
        } else {
            high -= 1;
        }
    }
    return numbers[low];
}
```

```golang
// Golang
func minArray(numbers []int) int {
    low := 0
    high := len(numbers) - 1
    for low < high {
        pivot := low + (high - low) / 2
        if numbers[pivot] < numbers[high] {
            high = pivot
        } else if numbers[pivot] > numbers[high] {
            low = pivot + 1
        } else {
            high--
        }
    }
    return numbers[low]
}
```

**复杂度分析**

- 时间复杂度：平均时间复杂度为 O(log n)，其中 n 是数组 numbers 的长度。如果数组是随机生成的，那么数组中包含相同元素的概率很低，在二分查找的过程中，大部分情况都会忽略一半的区间。而在最坏情况下，如果数组中的元素完全相同，那么 while 循环就需要执行 n 次，每次忽略区间的右端点，时间复杂度为 O(n)。

- 空间复杂度：O(1)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
