### 1356.根据数字二进制下 1 的数目排序（简单）

给你一个整数数组 arr。请你将数组中的元素按照其二进制表示中数字 1 的数目升序排序。

如果存在多个数字二进制中 1 的数目相同，则必须将它们按照数值大小升序排列。

请你返回排序后的数组。

示例 1：

```text
输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]
```

示例 2：

```text
输入：arr = [1024,512,256,128,64,32,16,8,4,2,1]
输出：[1,2,4,8,16,32,64,128,256,512,1024]
解释：数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。
```

示例 3：

```text
输入：arr = [10000,10000]
输出：[10000,10000]
```

示例 4：

```text
输入：arr = [2,3,5,7,11,13,17,19]
输出：[2,3,5,17,7,11,13,19]
```

示例 5：

```text
输入：arr = [10,100,1000,10000]
输出：[10,100,10000,1000]
```

提示：

- 1 <= arr.length <= 500
- 0 <= arr[i] <= 10^4

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 排序（Sort）  # 位运算（Bit Manipulate）
```

#### 提交

```py
# Python3
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key = lambda x: (bin(x).count("1"),x))
        return arr
```

#### 参考

**前言**
题目本身很简单，只要调用系统自带的排序函数，然后自己改写一下排序规则即可，所以这里主要讲讲如何计算数字二进制下 11 的个数 。

##### 方法一：暴力

对每个十进制的数转二进制的时候统计一下 1 的个数即可。

```c++
// C++
class Solution {
public:
    int get(int x){
        int res = 0;
        while (x) {
            res += (x % 2);
            x /= 2;
        }
        return res;
    }
    vector<int> sortByBits(vector<int>& arr) {
        vector<int> bit(10001, 0);
        for (auto x: arr) {
            bit[x] = get(x);
        }
        sort(arr.begin(),arr.end(),[&](int x,int y){
            if (bit[x] < bit[y]) {
                return true;
            }
            if (bit[x] > bit[y]) {
                return false;
            }
            return x < y;
        });
        return arr;
    }
};
```

```java
// Java
class Solution {
    public int[] sortByBits(int[] arr) {
        int[] bit = new int[10001];
        List<Integer> list = new ArrayList<Integer>();
        for (int x : arr) {
            list.add(x);
            bit[x] = get(x);
        }
        Collections.sort(list, new Comparator<Integer>() {
            public int compare(Integer x, Integer y) {
                if (bit[x] != bit[y]) {
                    return bit[x] - bit[y];
                } else {
                    return x - y;
                }
            }
        });
        for (int i = 0; i < arr.length; ++i) {
            arr[i] = list.get(i);
        }
        return arr;
    }

    public int get(int x) {
        int res = 0;
        while (x != 0) {
            res += x % 2;
            x /= 2;
        }
        return res;
    }
}
```

```golang
// Golang
func onesCount(x int) (c int) {
    for ; x > 0; x /= 2 {
        c += x % 2
    }
    return
}

func sortByBits(a []int) []int {
    sort.Slice(a, func(i, j int) bool {
        x, y := a[i], a[j]
        cx, cy := onesCount(x), onesCount(y)
        return cx < cy || cx == cy && x < y
    })
    return a
}
```

```c
// C
int* bit;

int get(int x) {
    int res = 0;
    while (x) {
        res += (x % 2);
        x /= 2;
    }
    return res;
}

int cmp(void* _x, void* _y) {
    int x = *(int*)_x, y = *(int*)_y;
    return bit[x] == bit[y] ? x - y : bit[x] - bit[y];
}

int* sortByBits(int* arr, int arrSize, int* returnSize) {
    bit = malloc(sizeof(int) * 10001);
    memset(bit, 0, sizeof(int) * 10001);
    for (int i = 0; i < arrSize; ++i) {
        bit[arr[i]] = get(arr[i]);
    }
    qsort(arr, arrSize, sizeof(int), cmp);
    free(bit);
    *returnSize = arrSize;
    return arr;
}
```

**复杂度分析**

- 时间复杂度：O(n log n)，其中 n 为整数数组 arr 的长度。

- 空间复杂度：O(n)，其中 n 为整数数组 arr 的长度。

##### 方法二：递推预处理

我们定义 bit[i] 为数字 i 二进制表示下数字 1 的个数，则可以列出递推式：

```text
bit[i] = bit[i>>1] + (i&1)
```

所以我们线性预处理 bit 数组然后去排序即可。

```c++
// C++
class Solution {
public:
    vector<int> sortByBits(vector<int>& arr) {
        vector<int> bit(10001, 0);
        for (int i = 1;i <= 10000; ++i) {
            bit[i] = bit[i>>1] + (i & 1);
        }
        sort(arr.begin(),arr.end(),[&](int x,int y){
            if (bit[x] < bit[y]) {
                return true;
            }
            if (bit[x] > bit[y]) {
                return false;
            }
            return x < y;
        });
        return arr;
    }
};
```

```java
// Java
class Solution {
    public int[] sortByBits(int[] arr) {
        List<Integer> list = new ArrayList<Integer>();
        for (int x : arr) {
            list.add(x);
        }
        int[] bit = new int[10001];
        for (int i = 1; i <= 10000; ++i) {
            bit[i] = bit[i >> 1] + (i & 1);
        }
        Collections.sort(list, new Comparator<Integer>() {
            public int compare(Integer x, Integer y) {
                if (bit[x] != bit[y]) {
                    return bit[x] - bit[y];
                } else {
                    return x - y;
                }
            }
        });
        for (int i = 0; i < arr.length; ++i) {
            arr[i] = list.get(i);
        }
        return arr;
    }
}
```

```golang
// Golang
var bit = [1e4 + 1]int{}

func init() {
    for i := 1; i <= 1e4; i++ {
        bit[i] = bit[i>>1] + i&1
    }
}

func sortByBits(a []int) []int {
    sort.Slice(a, func(i, j int) bool {
        x, y := a[i], a[j]
        cx, cy := bit[x], bit[y]
        return cx < cy || cx == cy && x < y
    })
    return a
}
```

```c
// C
int* bit;

int cmp(void* _x, void* _y) {
    int x = *(int*)_x, y = *(int*)_y;
    return bit[x] == bit[y] ? x - y : bit[x] - bit[y];
}

int* sortByBits(int* arr, int arrSize, int* returnSize) {
    bit = malloc(sizeof(int) * 10001);
    memset(bit, 0, sizeof(int) * 10001);
    for (int i = 1; i <= 10000; ++i) {
        bit[i] = bit[i >> 1] + (i & 1);
    }
    qsort(arr, arrSize, sizeof(int), cmp);
    free(bit);
    *returnSize = arrSize;
    return arr;
}
```

**复杂度分析**

- 时间复杂度：O(n log n)O，其中 n 为整数数组 arr 的长度。

- 空间复杂度：O(n)，其中 n 为整数数组 arr 的长度。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/solution/gen-ju-shu-zi-er-jin-zhi-xia-1-de-shu-mu-pai-xu-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
