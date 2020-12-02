### 321.拼接最大数(困难)

给定长度分别为 m 和 n 的两个数组，其元素由 0-9 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 k (k <= m + n)  个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 k 的数组。

说明: 请尽可能地优化你算法的时间和空间复杂度。

示例  1:

```text
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
```

示例 2:

```text
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
```

示例 3:

```text
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/create-maximum-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 贪心算法(Greedy)  # 动态规划(DP)
```

#### 提交

```py
# Python3(贪心算法 + 单调栈 + 字典序)
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        # 找到数组中长度为k且字典序最大的集合
        def findKth(k, nums):
            nn = len(nums)
            stack = [] # 单调栈，存储字典序最大的集合
            for i, num in enumerate(nums):
                # 必须保证栈中元素和剩下元素总长度之和不小于 k
                while stack and stack[-1] < num and len(stack) - 1 + nn - i >= k:
                    stack.pop()
                stack.append(num)
            return stack[:k]

        # 根据字典序合并两个数组
        def merge(a, b):
            m_, n_ = len(a), len(b)
            res = [] # 构造出的长度为 k 的数组
            i, j = 0, 0
            # 比较字典序
            while i < m_ and j < n_:
                if a[i:] > b[j:]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
            if i < m_:
                res.extend(a[i:])
            if j < n_:
                res.extend(b[j:])
            return res

        # 遍历两个数组
        ans = []
        for i in range(m+1):
            if 0 <= k - i <= n:
                ans = max(ans, merge(findKth(i, nums1), findKth(k-i, nums2)))
        return ans
```

**复杂度分析**

- 时间复杂度：O(k \* (m + n + k^2))
- 空间复杂度：O(k)

#### 参考

##### 方法一：单调栈

为了找到长度为 k 的最大数，需要从两个数组中分别选出最大的子序列，这两个子序列的长度之和为 k，然后将这两个子序列合并得到最大数。两个子序列的长度最小为 0，最大不能超过 k 且不能超过对应的数组长度。

令数组 nums1
的长度为 m，数组 nums2 的长度为 n，则需要从数组 nums1 中选出长度为 x 的子序列，以及从数组 nums2 中选出长度为 y 的子序列，其中 x + y = k，且满足 0 ≤ x ≤ m 和 0 ≤ y ≤ n。需要遍历所有可能的 x 和 y 的值，对于每一组 x 和 y 的值，得到最大数。在整个过程中维护可以通过拼接得到的最大数。

对于每一组 x 和 y 的值，得到最大数的过程分成两步，第一步是分别从两个数组中得到指定长度的最大子序列，第二步是将两个最大子序列合并。

第一步可以通过单调栈实现。单调栈满足从栈底到栈顶的元素单调递减，从左到右遍历数组，遍历过程中维护单调栈内的元素，需要保证遍历结束之后单调栈内的元素个数等于指定的最大子序列的长度。遍历结束之后，将从栈底到栈顶的元素依次拼接，即得到最大子序列。

第二步需要自定义比较方法。首先比较两个子序列的当前元素，如果两个当前元素不同，则选其中较大的元素作为下一个合并的元素，否则需要比较后面的所有元素才能决定选哪个元素作为下一个合并的元素。

```c++
// C++
class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        int m = nums1.size(), n = nums2.size();
        vector<int> maxSubsequence(k, 0);
        int start = max(0, k - n), end = min(k, m);
        for (int i = start; i <= end; i++) {
            vector<int> subsequence1(MaxSubsequence(nums1, i));
            vector<int> subsequence2(MaxSubsequence(nums2, k - i));
            vector<int> curMaxSubsequence(merge(subsequence1, subsequence2));
            if (compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0) {
                maxSubsequence.swap(curMaxSubsequence);
            }
        }
        return maxSubsequence;
    }

    vector<int> MaxSubsequence(vector<int>& nums, int k) {
        int length = nums.size();
        vector<int> stack(k, 0);
        int top = -1;
        int remain = length - k;
        for (int i = 0; i < length; i++) {
            int num = nums[i];
            while (top >= 0 && stack[top] < num && remain > 0) {
                top--;
                remain--;
            }
            if (top < k - 1) {
                stack[++top] = num;
            } else {
                remain--;
            }
        }
        return stack;
    }

    vector<int> merge(vector<int>& subsequence1, vector<int>& subsequence2) {
        int x = subsequence1.size(), y = subsequence2.size();
        if (x == 0) {
            return subsequence2;
        }
        if (y == 0) {
            return subsequence1;
        }
        int mergeLength = x + y;
        vector<int> merged(mergeLength);
        int index1 = 0, index2 = 0;
        for (int i = 0; i < mergeLength; i++) {
            if (compare(subsequence1, index1, subsequence2, index2) > 0) {
                merged[i] = subsequence1[index1++];
            } else {
                merged[i] = subsequence2[index2++];
            }
        }
        return merged;
    }

    int compare(vector<int>& subsequence1, int index1, vector<int>& subsequence2, int index2) {
        int x = subsequence1.size(), y = subsequence2.size();
        while (index1 < x && index2 < y) {
            int difference = subsequence1[index1] - subsequence2[index2];
            if (difference != 0) {
                return difference;
            }
            index1++;
            index2++;
        }
        return (x - index1) - (y - index2);
    }
};
```

```java
class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        int m = nums1.length, n = nums2.length;
        int[] maxSubsequence = new int[k];
        int start = Math.max(0, k - n), end = Math.min(k, m);
        for (int i = start; i <= end; i++) {
            int[] subsequence1 = maxSubsequence(nums1, i);
            int[] subsequence2 = maxSubsequence(nums2, k - i);
            int[] curMaxSubsequence = merge(subsequence1, subsequence2);
            if (compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0) {
                System.arraycopy(curMaxSubsequence, 0, maxSubsequence, 0, k);
            }
        }
        return maxSubsequence;
    }

    public int[] maxSubsequence(int[] nums, int k) {
        int length = nums.length;
        int[] stack = new int[k];
        int top = -1;
        int remain = length - k;
        for (int i = 0; i < length; i++) {
            int num = nums[i];
            while (top >= 0 && stack[top] < num && remain > 0) {
                top--;
                remain--;
            }
            if (top < k - 1) {
                stack[++top] = num;
            } else {
                remain--;
            }
        }
        return stack;
    }

    public int[] merge(int[] subsequence1, int[] subsequence2) {
        int x = subsequence1.length, y = subsequence2.length;
        if (x == 0) {
            return subsequence2;
        }
        if (y == 0) {
            return subsequence1;
        }
        int mergeLength = x + y;
        int[] merged = new int[mergeLength];
        int index1 = 0, index2 = 0;
        for (int i = 0; i < mergeLength; i++) {
            if (compare(subsequence1, index1, subsequence2, index2) > 0) {
                merged[i] = subsequence1[index1++];
            } else {
                merged[i] = subsequence2[index2++];
            }
        }
        return merged;
    }

    public int compare(int[] subsequence1, int index1, int[] subsequence2, int index2) {
        int x = subsequence1.length, y = subsequence2.length;
        while (index1 < x && index2 < y) {
            int difference = subsequence1[index1] - subsequence2[index2];
            if (difference != 0) {
                return difference;
            }
            index1++;
            index2++;
        }
        return (x - index1) - (y - index2);
    }
}
```

```js
// JavaScript
var maxNumber = function (nums1, nums2, k) {
  const m = nums1.length,
    n = nums2.length;
  const maxSubsequence = new Array(k).fill(0);
  let start = Math.max(0, k - n),
    end = Math.min(k, m);
  for (let i = start; i <= end; i++) {
    const subsequence1 = new MaxSubsequence(nums1, i);
    const subsequence2 = new MaxSubsequence(nums2, k - i);
    const curMaxSubsequence = merge(subsequence1, subsequence2);
    if (compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0) {
      maxSubsequence.splice(0, k, ...curMaxSubsequence);
    }
  }
  return maxSubsequence;
};

var MaxSubsequence = function (nums, k) {
  const length = nums.length;
  const stack = new Array(k).fill(0);
  let top = -1;
  let remain = length - k;
  for (let i = 0; i < length; i++) {
    const num = nums[i];
    while (top >= 0 && stack[top] < num && remain > 0) {
      top--;
      remain--;
    }
    if (top < k - 1) {
      stack[++top] = num;
    } else {
      remain--;
    }
  }
  return stack;
};

const merge = (subsequence1, subsequence2) => {
  const x = subsequence1.length,
    y = subsequence2.length;
  if (x === 0) {
    return subsequence2;
  }
  if (y === 0) {
    return subsequence1;
  }
  const mergeLength = x + y;
  const merged = new Array(mergeLength).fill(0);
  let index1 = 0,
    index2 = 0;
  for (let i = 0; i < mergeLength; i++) {
    if (compare(subsequence1, index1, subsequence2, index2) > 0) {
      merged[i] = subsequence1[index1++];
    } else {
      merged[i] = subsequence2[index2++];
    }
  }
  return merged;
};

const compare = (subsequence1, index1, subsequence2, index2) => {
  const x = subsequence1.length,
    y = subsequence2.length;
  while (index1 < x && index2 < y) {
    const difference = subsequence1[index1] - subsequence2[index2];
    if (difference !== 0) {
      return difference;
    }
    index1++;
    index2++;
  }
  return x - index1 - (y - index2);
};
```

```py
# Python3
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m, n = len(nums1), len(nums2)
        maxSubsequence = [0] * k
        start, end = max(0, k - n), min(k, m)

        for i in range(start, end + 1):
            subsequence1 = self.getMaxSubsequence(nums1, i)
            subsequence2 = self.getMaxSubsequence(nums2, k - i)
            curMaxSubsequence = self.merge(subsequence1, subsequence2)
            if self.compare(curMaxSubsequence, 0, maxSubsequence, 0) > 0:
                maxSubsequence = curMaxSubsequence

        return maxSubsequence

    def getMaxSubsequence(self, nums: List[int], k: int) -> int:
        stack = [0] * k
        top = -1
        remain = len(nums) - k

        for i, num in enumerate(nums):
            while top >= 0 and stack[top] < num and remain > 0:
                top -= 1
                remain -= 1
            if top < k - 1:
                top += 1
                stack[top] = num
            else:
                remain -= 1

        return stack

    def merge(self, subsequence1: List[int], subsequence2: List[int]) -> List[int]:
        x, y = len(subsequence1), len(subsequence2)
        if x == 0:
            return subsequence2
        if y == 0:
            return subsequence1

        mergeLength = x + y
        merged = list()
        index1 = index2 = 0

        for _ in range(mergeLength):
            if self.compare(subsequence1, index1, subsequence2, index2) > 0:
                merged.append(subsequence1[index1])
                index1 += 1
            else:
                merged.append(subsequence2[index2])
                index2 += 1

        return merged

    def compare(self, subsequence1: List[int], index1: int, subsequence2: List[int], index2: int) -> int:
        x, y = len(subsequence1), len(subsequence2)
        while index1 < x and index2 < y:
            difference = subsequence1[index1] - subsequence2[index2]
            if difference != 0:
                return difference
            index1 += 1
            index2 += 1

        return (x - index1) - (y - index2)
```

```golang
// Golang
func maxSubsequence(a []int, k int) (s []int) {
    for i, v := range a {
        for len(s) > 0 && len(s)+len(a)-1-i >= k && v > s[len(s)-1] {
            s = s[:len(s)-1]
        }
        if len(s) < k {
            s = append(s, v)
        }
    }
    return
}

func lexicographicalLess(a, b []int) bool {
    for i := 0; i < len(a) && i < len(b); i++ {
        if a[i] != b[i] {
            return a[i] < b[i]
        }
    }
    return len(a) < len(b)
}

func merge(a, b []int) []int {
    merged := make([]int, len(a)+len(b))
    for i := range merged {
        if lexicographicalLess(a, b) {
            merged[i], b = b[0], b[1:]
        } else {
            merged[i], a = a[0], a[1:]
        }
    }
    return merged
}

func maxNumber(nums1, nums2 []int, k int) (res []int) {
    start := 0
    if k > len(nums2) {
        start = k - len(nums2)
    }
    for i := start; i <= k && i <= len(nums1); i++ {
        s1 := maxSubsequence(nums1, i)
        s2 := maxSubsequence(nums2, k-i)
        merged := merge(s1, s2)
        if lexicographicalLess(res, merged) {
            res = merged
        }
    }
    return
}
```

```c
// C
int compare(int* subseq1, int subseq1Size, int index1, int* subseq2, int subseq2Size, int index2) {
    while (index1 < subseq1Size && index2 < subseq2Size) {
        int difference = subseq1[index1] - subseq2[index2];
        if (difference != 0) {
            return difference;
        }
        index1++;
        index2++;
    }
    return (subseq1Size - index1) - (subseq2Size - index2);
}

int* merge(int* subseq1, int subseq1Size, int* subseq2, int subseq2Size) {
    if (subseq1Size == 0) {
        return subseq2;
    }
    if (subseq2Size == 0) {
        return subseq1;
    }
    int mergeLength = subseq1Size + subseq2Size;
    int* merged = malloc(sizeof(int) * (subseq1Size + subseq2Size));
    int index1 = 0, index2 = 0;
    for (int i = 0; i < mergeLength; i++) {
        if (compare(subseq1, subseq1Size, index1, subseq2, subseq2Size, index2) > 0) {
            merged[i] = subseq1[index1++];
        } else {
            merged[i] = subseq2[index2++];
        }
    }
    return merged;
}

int* MaxSubsequence(int* nums, int numsSize, int k) {
    int* stack = malloc(sizeof(int) * k);
    memset(stack, 0, sizeof(int) * k);
    int top = -1;
    int remain = numsSize - k;
    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        while (top >= 0 && stack[top] < num && remain > 0) {
            top--;
            remain--;
        }
        if (top < k - 1) {
            stack[++top] = num;
        } else {
            remain--;
        }
    }
    return stack;
}

void swap(int** a, int** b) {
    int* tmp = *a;
    *a = *b, *b = tmp;
}

int* maxNumber(int* nums1, int nums1Size, int* nums2, int nums2Size, int k, int* returnSize) {
    int* maxSubsequence = malloc(sizeof(int) * k);
    memset(maxSubsequence, 0, sizeof(int) * k);
    *returnSize = k;
    int start = fmax(0, k - nums2Size), end = fmin(k, nums1Size);
    for (int i = start; i <= end; i++) {
        int* subseq1 = MaxSubsequence(nums1, nums1Size, i);
        int* subseq2 = MaxSubsequence(nums2, nums2Size, k - i);
        int* curMaxSubsequence = merge(subseq1, i, subseq2, k - i);
        if (compare(curMaxSubsequence, k, 0, maxSubsequence, k, 0) > 0) {
            swap(&curMaxSubsequence, &maxSubsequence);
        }
    }
    return maxSubsequence;
}
```

**复杂度分析**

- 时间复杂度：O(k(m+n+k^2))，其中 m 和 n 分别是数组 nums1 和 nums2 的长度，k 是拼接最大数的长度。
  两个子序列的长度之和为 k，最多有 k 种不同的长度组合。对于每一种长度组合，需要首先得到两个最大子序列，然后进行合并。
  得到两个最大子序列的时间复杂度为线性，即 O(m+n)。
  合并两个最大子序列，需要进行 k 次合并，每次合并需要进行比较，最坏情况下，比较的时间复杂度为 O(k)，因此合并操作的时间复杂度为 O(k^2)。
  因此对于每一种长度组合，时间复杂度为 O(m+n+k^2)，总时间复杂度为 O(k(m+n+k^2))。

- 空间复杂度：O(k)，其中 k 是拼接最大数的长度。每次从两个数组得到两个子序列，两个子序列的长度之和为 k。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/create-maximum-number/solution/pin-jie-zui-da-shu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
