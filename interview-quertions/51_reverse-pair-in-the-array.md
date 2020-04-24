### 面试题 51. 数组中的逆序对（困难）

在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。

示例 1:

```text
输入: [7,5,6,4]
输出: 5
```

限制：

```text
0 <= 数组长度 <= 50000
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 提交
```py
# Python3
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt, tmp = 0, []
        for num in nums[::-1]:
            cnt += bisect_left(tmp, num) # 二分插入，计算已有列表(后面的先插入)比num小的数字
            insort(tmp, num)
        return cnt
```

#### 参考

##### 方法一：归并排序
**预备知识**

「归并排序」是分治思想的典型应用，它包含这样三个步骤：

- 分解： 待排序的区间为 [l, r]，令 m = ⌊l+r/2⌋，我们把 [l, r] 分成 [l, m] 和 [m + 1, r]
- 解决： 使用归并排序递归地排序两个子序列
- 合并： 把两个已经排好序的子序列 [l, m][l,m] 和 [m + 1, r][m+1,r] 合并起来

在待排序序列长度为 1 的时候，递归开始「回升」，因为我们默认长度为 1 的序列是排好序的。

**思路**

那么求逆序对和归并排序又有什么关系呢？关键就在于「归并」当中「并」的过程。我们通过一个实例来看看。假设我们有两个已排序的序列等待合并，分别是 L = {8, 12, 16, 22, 100} 和 R = { 9, 26, 55, 64, 91 }。一开始我们用指针 lPtr = 0 指向 L 的首部，rPtr = 0 指向 R 的头部。记已经合并好的部分为 M。

```text
L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = []
     |                          |
   lPtr                       rPtr
```

我们发现 lPtr 指向的元素小于 rPtr 指向的元素，于是把 lPtr 指向的元素放入答案，并把 lPtr 后移一位。

```text
L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8]
        |                       |
      lPtr                     rPtr
```

这个时候我们把左边的 8 加入了答案，我们发现右边没有数比 8 小，所以 8 对逆序对总数的「贡献」为 0。

接着我们继续合并，把 9 加入了答案，此时 lPtr 指向 12，rPtr 指向 26。

```text
L = [8, 12, 16, 22, 100]   R = [9, 26, 55, 64, 91]  M = [8, 9]
        |                          |
       lPtr                       rPtr
```

此时 lPtr 比 rPtr 小，把 lPtr 对应的数加入答案，并考虑它对逆序对总数的贡献为 rPtr 相对 R 首位置的偏移 1（即右边只有一个数比 12 小，所以只有它和 12 构成逆序对），以此类推。

我们发现用这种「算贡献」的思想在合并的过程中计算逆序对的数量的时候，只在 lPtr 右移的时候计算，是基于这样的事实：当前 lPtr 指向的数字比 rPtr 小，但是比 RR 中 [0 ... rPtr - 1] 的其他数字大，[0 ... rPtr - 1] 的其他数字本应当排在 lPtr 对应数字的左边，但是它排在了右边，所以这里就贡献了 rPtr 个逆序对。

利用这个思路，我们可以写出如下代码：

```py
# Python3
class Solution:
    def mergeSort(self, nums, tmp, l, r):
        if l >= r:
            return 0

        mid = (l + r) // 2
        inv_count = self.mergeSort(nums, tmp, l, mid) + self.mergeSort(nums, tmp, mid + 1, r)
        i, j, pos = l, mid + 1, l
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                tmp[pos] = nums[i]
                i += 1
                inv_count += (j - (mid + 1))
            else:
                tmp[pos] = nums[j]
                j += 1
            pos += 1
        for k in range(i, mid + 1):
            tmp[pos] = nums[k]
            inv_count += (j - (mid + 1))
            pos += 1
        for k in range(j, r + 1):
            tmp[pos] = nums[k]
            pos += 1
        nums[l:r+1] = tmp[l:r+1]
        return inv_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = [0] * n
        return self.mergeSort(nums, tmp, 0, n - 1)
```

```c++
// C++
class Solution {
public:
    int mergeSort(vector<int>& nums, vector<int>& tmp, int l, int r) {
        if (l >= r) {
            return 0;
        }

        int mid = (l + r) / 2;
        int inv_count = mergeSort(nums, tmp, l, mid) + mergeSort(nums, tmp, mid + 1, r);
        int i = l, j = mid + 1, pos = l;
        while (i <= mid && j <= r) {
            if (nums[i] <= nums[j]) {
                tmp[pos] = nums[i];
                ++i;
                inv_count += (j - (mid + 1));
            }
            else {
                tmp[pos] = nums[j];
                ++j;
            }
            ++pos;
        }
        for (int k = i; k <= mid; ++k) {
            tmp[pos++] = nums[k];
            inv_count += (j - (mid + 1));
        }
        for (int k = j; k <= r; ++k) {
            tmp[pos++] = nums[k];
        }
        copy(tmp.begin() + l, tmp.begin() + r + 1, nums.begin() + l);
        return inv_count;
    }

    int reversePairs(vector<int>& nums) {
        int n = nums.size();
        vector<int> tmp(n);
        return mergeSort(nums, tmp, 0, n - 1);
    }
};
```

```java
// Java
public class Solution {

    public int reversePairs(int[] nums) {
        int len = nums.length;

        if (len < 2) {
            return 0;
        }

        int[] copy = new int[len];
        for (int i = 0; i < len; i++) {
            copy[i] = nums[i];
        }

        int[] temp = new int[len];
        return reversePairs(copy, 0, len - 1, temp);
    }

    /**
     * nums[left..right] 计算逆序对个数并且排序
     *
     * @param nums
     * @param left
     * @param right
     * @param temp
     * @return
     */
    private int reversePairs(int[] nums, int left, int right, int[] temp) {
        if (left == right) {
            return 0;
        }

        int mid = left + (right - left) / 2;
        int leftPairs = reversePairs(nums, left, mid, temp);
        int rightPairs = reversePairs(nums, mid + 1, right, temp);

        if (nums[mid] <= nums[mid + 1]) {
            return leftPairs + rightPairs;
        }

        int crossPairs = mergeAndCount(nums, left, mid, right, temp);
        return leftPairs + rightPairs + crossPairs;
    }

    /**
     * nums[left..mid] 有序，nums[mid + 1..right] 有序
     *
     * @param nums
     * @param left
     * @param mid
     * @param right
     * @param temp
     * @return
     */
    private int mergeAndCount(int[] nums, int left, int mid, int right, int[] temp) {
        for (int i = left; i <= right; i++) {
            temp[i] = nums[i];
        }

        int i = left;
        int j = mid + 1;

        int count = 0;
        for (int k = left; k <= right; k++) {

            if (i == mid + 1) {
                nums[k] = temp[j];
                j++;
            } else if (j == right + 1) {
                nums[k] = temp[i];
                i++;
            } else if (temp[i] <= temp[j]) {
                nums[k] = temp[i];
                i++;
            } else {
                nums[k] = temp[j];
                j++;
                count += (mid - i + 1);
            }
        }
        return count;
    }
}
```

```golang
// Golang
func reversePairs(nums []int) int {
    return mergeSort(nums, 0, len(nums)-1)
}

func mergeSort(nums []int, start, end int) int {
    if start >= end {
        return 0
    }
    mid := start + (end - start)/2
    cnt := mergeSort(nums, start, mid) + mergeSort(nums, mid + 1, end)
    tmp := []int{}
    i, j := start, mid + 1
    for i <= mid && j <= end {
        if nums[i] <= nums[j] {
            tmp = append(tmp, nums[i])
            cnt += j - (mid + 1)
            i++
        } else {
            tmp = append(tmp, nums[j])
            j++
        }
    }
    for ; i <= mid; i++ {
        tmp = append(tmp, nums[i])
        cnt += end - (mid + 1) + 1
    }
    for ; j <= end; j++ {
        tmp = append(tmp, nums[j])
    }
    for i := start; i <= end; i++ {
        nums[i] = tmp[i - start]
    }
    return cnt
}
```

**复杂度**

记序列长度为 n。

- 时间复杂度：同归并排序 O(n log n)。
- 空间复杂度：同归并排序 O(n)，因为归并排序需要用到一个临时数组。

##### 方法二：离散化树状数组

**预备知识**

「树状数组」是一种可以动态维护序列前缀和的数据结构，它的功能是：

单点更新 update(i, v)： 把序列 ii 位置的数加上一个值 v，这题 v = 1
区间查询 query(i)： 查询序列 [1 ⋯ i] 区间的区间和，即 i 位置的前缀和
修改和查询的时间代价都是 O(\log n)，其中 n 为需要维护前缀和的序列的长度。

**思路**

记题目给定的序列为 a，我们规定 a_i 的取值集合为 aa 的「值域」。我们用桶来表示值域中的每一个数，桶中记录这些数字出现的次数。假设a = {5, 5, 2, 3, 6}，那么遍历这个序列得到的桶是这样的：
