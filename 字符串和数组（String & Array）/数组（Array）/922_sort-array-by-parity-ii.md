### 922.按奇偶排序数组 II（简单）

给定一个非负整数数组 A，A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i]为奇数时，i 也是奇数；当  A[i]为偶数时，i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

示例：

```text
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
```

提示：

- 2 <= A.length <= 20000
- A.length % 2 == 0
- 0 <= A[i] <= 1000

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数组（Array）  # 排序（Sort）
```

#### 提交

```py
# Python3
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        B = []
        C = []
        for i in range(len(A)):
            if i % 2 and A[i] % 2 == 0: B.append(i)
            elif i % 2 == 0 and A[i] % 2: C.append(i)
        for i in range(len(B)):
            A[B[i]], A[C[i]] = A[C[i]], A[B[i]]
        return A
```

#### 参考

##### 方法一： 两次遍历

**思路和算法**

遍历一遍数组把所有的偶数放进 ans[0]，ans[2]，ans[4]，依次类推。

再遍历一遍数组把所有的奇数依次放进 ans[1]，ans[3]，ans[5]，依次类推。

```c++
// C++
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        int n = A.size();
        vector<int> ans(n);

        int i = 0;
        for (int x: A) {
            if (x % 2 == 0) {
                ans[i] = x;
                i += 2;
            }
        }
        i = 1;
        for (int x: A) {
            if (x % 2 == 1) {
                ans[i] = x;
                i += 2;
            }
        }
        return ans;
    }
};
```

```java
// Java
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int n = A.length;
        int[] ans = new int[n];

        int i = 0;
        for (int x : A) {
            if (x % 2 == 0) {
                ans[i] = x;
                i += 2;
            }
        }
        i = 1;
        for (int x : A) {
            if (x % 2 == 1) {
                ans[i] = x;
                i += 2;
            }
        }
        return ans;
    }
}
```

```c
// C
int* sortArrayByParityII(int* A, int ASize, int* returnSize) {
    int* ans = malloc(sizeof(int) * ASize);
    int add = 0;
    for (int i = 0; i < ASize; i++) {
        if (A[i] % 2 == 0) {
            ans[add] = A[i];
            add += 2;
        }
    }
    add = 1;
    for (int i = 0; i < ASize; i++) {
        if (A[i] % 2 == 1) {
            ans[add] = A[i];
            add += 2;
        }
    }
    *returnSize = ASize;
    return ans;
}
```

```js
// JavaScript
var sortArrayByParityII = function (A) {
  const n = A.length;
  const ans = new Array(n);
  let i = 0;
  for (const x of A) {
    if (!(x & 1)) {
      ans[i] = x;
      i += 2;
    }
  }

  i = 1;
  for (const x of A) {
    if (x & 1) {
      ans[i] = x;
      i += 2;
    }
  }

  return ans;
};
```

```golang
// Golang
func sortArrayByParityII(a []int) []int {
    ans := make([]int, len(a))
    i := 0
    for _, v := range a {
        if v%2 == 0 {
            ans[i] = v
            i += 2
        }
    }
    i = 1
    for _, v := range a {
        if v%2 == 1 {
            ans[i] = v
            i += 2
        }
    }
    return ans
}
```

**复杂度分析**

- 时间复杂度：O(N)，其中 N 是数组 A 的长度。

- 空间复杂度：O(1)。注意在这里我们不考虑输出数组的空间占用。

##### 方法二： 双指针

**思路与算法**

如果原数组可以修改，则可以使用就地算法求解。

为数组的偶数下标部分和奇数下标部分分别维护指针 i, j。随后，在每一步中，如果 A[i] 为奇数，则不断地向前移动 j（每次移动两个单位），直到遇见下一个偶数。此时，可以直接将 A[i] 与 A[j] 交换。我们不断进行这样的过程，最终能够将所有的整数放在正确的位置上。

```c++
// C++
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        int n = A.size();
        int j = 1;
        for (int i = 0; i < n; i += 2) {
            if (A[i] % 2 == 1) {
                while (A[j] % 2 == 1) {
                    j += 2;
                }
                swap(A[i], A[j]);
            }
        }
        return A;
    }
};
```

```java
// Java
class Solution {
    public int[] sortArrayByParityII(int[] A) {
        int n = A.length;
        int j = 1;
        for (int i = 0; i < n; i += 2) {
            if (A[i] % 2 == 1) {
                while (A[j] % 2 == 1) {
                    j += 2;
                }
                swap(A, i, j);
            }
        }
        return A;
    }

    public void swap(int[] A, int i, int j) {
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
    }
}
```

```c
// C
void swap(int* a, int* b) {
    int t = *a;
    *a = *b, *b = t;
}

int* sortArrayByParityII(int* A, int ASize, int* returnSize) {
    int j = 1;
    for (int i = 0; i < ASize; i += 2) {
        if (A[i] % 2 == 1) {
            while (A[j] % 2 == 1) {
                j += 2;
            }
            swap(A + i, A + j);
        }
    }
    *returnSize = ASize;
    return A;
}
```

```js
// JavaScript
const swap = (A, i, j) => {
  const temp = A[i];
  A[i] = A[j];
  A[j] = temp;
};
var sortArrayByParityII = function (A) {
  const n = A.length;
  let j = 1;
  for (let i = 0; i < n; i += 2) {
    if (A[i] & 1) {
      while (A[j] & 1) {
        j += 2;
      }
      swap(A, i, j);
    }
  }
  return A;
};
```

```golang
// Golang
func sortArrayByParityII(a []int) []int {
    for i, j := 0, 1; i < len(a); i += 2 {
        if a[i]%2 == 1 {
            for a[j]%2 == 1 {
                j += 2
            }
            a[i], a[j] = a[j], a[i]
        }
    }
    return a
}
```

**复杂度分析**

- 时间复杂度：O(N)，其中 N 是数组 A 的长度。

- 空间复杂度：O(1)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sort-array-by-parity-ii/solution/an-qi-ou-pai-xu-shu-zu-ii-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
