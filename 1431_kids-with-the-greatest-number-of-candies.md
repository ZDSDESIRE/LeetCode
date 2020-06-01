### 1431. 拥有最多糖果的孩子（简单）

给你一个数组 candies  和一个整数 extraCandies ，其中 candies[i]  代表第 i 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 extraCandies  个糖果分配给孩子们之后，此孩子有最多的糖果。注意，允许有多个孩子同时拥有最多的糖果数目。

示例 1：

```text
输入：candies = [2,3,5,1,3], extraCandies = 3
输出：[true,true,true,false,true]
解释：
孩子 1 有 2 个糖果，如果他得到所有额外的糖果（3 个），那么他总共有 5 个糖果，他将成为拥有最多糖果的孩子。
孩子 2 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
孩子 3 有 5 个糖果，他已经是拥有最多糖果的孩子。
孩子 4 有 1 个糖果，即使他得到所有额外的糖果，他也只有 4 个糖果，无法成为拥有糖果最多的孩子。
孩子 5 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
```

示例 2：

```text
输入：candies = [4,2,1,1,2], extraCandies = 1
输出：[true,false,false,false,false]
解释：只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。
```

示例 3：

```text
输入：candies = [12,1,12], extraCandies = 10
输出：[true,false,true]
```

提示：

- 2 <= candies.length <= 100
- 1 <= candies[i] <= 100
- 1 <= extraCandies <= 50

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

#### 提交

```py
# Python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_ = max(candies)
        return [candy + extraCandies >= max_ for candy in candies]
```

#### 参考

##### 方法一：枚举

**思路**

如果我们希望某个小朋友拥有的糖果最多，那么最优的方案当然是把额外的所有糖果都分给这个小朋友。因此，我们可以枚举每一个小朋友，并将额外的所有糖果都分给这个小朋友，然后再用 O(n) 的时间遍历其余的小朋友，就可以判断这个小朋友是否拥有最多的糖果。

上述方法的时间复杂度为 O(n^2)，然而我们可以将其优化为 O(n)。事实上，对于每一个小朋友，只要这个小朋友「拥有的糖果数目」加上「额外的糖果数目」大于等于所有小朋友拥有的糖果数目最大值，那么这个小朋友就可以拥有最多的糖果。

**证明**

设某个小朋友的糖果数为 x，其余小朋友拥有的糖果数目最大值为 y，额外的糖果数为 e。这个小朋友可以拥有最多的糖果，当且仅当

```text
x + e ≥ y
```

由于 x + e ≥ x 显然成立，那么我们有

```text
x + e ≥ max(x, y)
```

而 max(x, y) 就是所有小朋友拥有的糖果数目最大值。因此我们可以预处理出这个值，随后枚举每一个小朋友，只要这个小朋友「拥有的糖果数目」加上「额外的糖果数目」大于等于这个值，就可以满足要求。

```py
# Python3
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        ret = [candy + extraCandies >= maxCandies for candy in candies]
        return ret
```

```c++
// C++
class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int n = candies.size();
        int maxCandies = *max_element(candies.begin(), candies.end());
        vector<bool> ret;
        for (int i = 0; i < n; ++i) {
            ret.push_back(candies[i] + extraCandies >= maxCandies);
        }
        return ret;
    }
};
```

```java
// Java
class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int n = candies.length;
        int maxCandies = 0;
        for (int i = 0; i < n; ++i) {
            maxCandies = Math.max(maxCandies, candies[i]);
        }
        List<Boolean> ret = new ArrayList<Boolean>();
        for (int i = 0; i < n; ++i) {
            ret.add(candies[i] + extraCandies >= maxCandies);
        }
        return ret;
    }
}
```

```Golang
// Golang
func kidsWithCandies(candies []int, extraCandies int) []bool {
    n := len(candies)
    maxCandies := 0
    for i := 0; i < n; i++ {
        maxCandies = max(maxCandies, candies[i])
    }
    ret := make([]bool, n)
    for i := 0; i < n; i++ {
        ret[i] = candies[i] + extraCandies >= maxCandies
    }
    return ret
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}
```

**复杂度分析**

假设小朋友的总数为 n。

- 时间复杂度：我们首先使用 O(n) 的时间预处理出所有小朋友拥有的糖果数目最大值。对于每一个小朋友，我们需要 O(1) 的时间判断这个小朋友是否可以拥有最多的糖果，故渐进时间复杂度为 O(n)。

- 空间复杂度：这里只用了常数个变量作为辅助空间，与 n 的规模无关，故渐进空间复杂度为 O(1)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies/solution/yong-you-zui-duo-tang-guo-de-hai-zi-by-leetcode-so/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
