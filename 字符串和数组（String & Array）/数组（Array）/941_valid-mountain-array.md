### 941. 有效的山脉数组（简单）

给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。

让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

- A.length >= 3
- 在 0 < i < A.length - 1 条件下，存在 i 使得：
  A[0] < A[1] < ... A[i-1] < A[i]
  A[i] > A[i+1] > ... > A[A.length - 1]

示例 1：

```text
输入：[2,1]
输出：false
```

示例 2：

```text
输入：[3,5,5]
输出：false
```

示例 3：

```text
输入：[0,3,2,1]
输出：true
```

提示：

```text
0 <= A.length <= 10000
0 <= A[i] <= 10000
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数组（String）
```

#### 提交

```py
# Python3
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        n = len(A)
        # 定义指针
        left = 0
        right = n - 1

        # 先处理 left 指针
        # 满足右边的值大于当前值时，往右移动
        # 注意边界
        while left + 1 < n and A[left] < A[left+1]:
            left += 1
        # 处理 right 指针
        # 满足左边的值大于当前值时，往左移动，同样注意边界问题
        while right - 1 > 0 and A[right - 1] > A[right]:
            right -= 1
        # 判断 left 指针是否与 right 指针重合
        # 同时注意，峰顶不能在数组两端
        if left > 0 and right < n - 1 and left == right:
            return True

        return False
```

#### 参考

##### 方法一：线性扫描

按题意模拟即可。我们从数组的最左侧开始向右扫描，直到找到第一个不满足 A[i] < A[i + 1] 的下标 i，那么 i 就是这个数组的最高点的下标。如果 i = 0 或者不存在这样的 i（即整个数组都是单调递增的），那么就返回 false。否则从 i 开始继续向右扫描，判断接下来的的下标 j 是否都满足 A[j] > A[j + 1]，若都满足就返回 true，否则返回 false。

```py
# Python
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # 递增扫描
        while i + 1 < N and A[i] < A[i + 1]:
            i += 1

        # 最高点不能是数组的第一个位置或最后一个位置
        if i == 0 or i == N - 1:
            return False

        # 递减扫描
        while i + 1 < N and A[i] > A[i + 1]:
            i += 1

        return i == N - 1
```

```c++
// C++
class Solution {
public:
    bool validMountainArray(vector<int>& A) {
        int N = A.size();
        int i = 0;

        // 递增扫描
        while (i + 1 < N && A[i] < A[i + 1]) {
            i++;
        }

        // 最高点不能是数组的第一个位置或最后一个位置
        if (i == 0 || i == N - 1) {
            return false;
        }

        // 递减扫描
        while (i + 1 < N && A[i] > A[i + 1]) {
            i++;
        }

        return i == N - 1;
    }
};
```

```java
// Java
class Solution {
    public boolean validMountainArray(int[] A) {
        int N = A.length;
        int i = 0;

        // 递增扫描
        while (i + 1 < N && A[i] < A[i + 1]) {
            i++;
        }

        // 最高点不能是数组的第一个位置或最后一个位置
        if (i == 0 || i == N - 1) {
            return false;
        }

        // 递减扫描
        while (i + 1 < N && A[i] > A[i + 1]) {
            i++;
        }

        return i == N - 1;
    }
}
```

```js
// JavaScript
var validMountainArray = function (A) {
  const N = A.length;
  let i = 0;

  // 递增扫描
  while (i + 1 < N && A[i] < A[i + 1]) {
    i++;
  }

  // 最高点不能是数组的第一个位置或最后一个位置
  if (i === 0 || i === N - 1) {
    return false;
  }

  // 递减扫描
  while (i + 1 < N && A[i] > A[i + 1]) {
    i++;
  }

  return i === N - 1;
};
```

```golang
// Golang
func validMountainArray(a []int) bool {
    i, n := 0, len(a)

    // 递增扫描
    for ; i+1 < n && a[i] < a[i+1]; i++ {
    }

    // 最高点不能是数组的第一个位置或最后一个位置
    if i == 0 || i == n-1 {
        return false
    }

    // 递减扫描
    for ; i+1 < n && a[i] > a[i+1]; i++ {
    }

    return i == n-1
}
```

```c
// C
bool validMountainArray(int* A, int ASize) {
    int i = 0;

    // 递增扫描
    while (i + 1 < ASize && A[i] < A[i + 1]) {
        i++;
    }

    // 最高点不能是数组的第一个位置或最后一个位置
    if (i == 0 || i == ASize - 1) {
        return false;
    }

    // 递减扫描
    while (i + 1 < ASize && A[i] > A[i + 1]) {
        i++;
    }

    return i == ASize - 1;
}
```

**复杂度分析**

- 时间复杂度：O(N)，其中 N 是数组 A 的长度。

- 空间复杂度：O(1)。
