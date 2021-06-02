### 523. 连续的子数组和（中等）

给你一个整数数组 nums 和一个整数  k ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：

- 子数组大小 至少为 2 ，且
- 子数组元素总和为 k 的倍数。

如果存在，返回 true ；否则，返回 false 。

如果存在一个整数 n ，令整数 x 符合 x = n \* k ，则称 x 是 k 的一个倍数。

示例 1：

```text
输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
```

示例 2：

```text
输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。
```

示例 3：

```text
输入：nums = [23,2,6,4,7], k = 13
输出：false
```

提示：

- 1 <= nums.length <= 105
- 0 <= nums[i] <= 109
- 0 <= sum(nums[i]) <= 231 - 1
- 1 <= k <= 231 - 1

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/continuous-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 数学（Math）  # 动态规划（DP）
```

#### 提交

```py
# Python3
# 暴力法（超时）
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
         amount = len(nums)
         if amount < 2:
             return False

         for i in range(amount):
             res = 0
             for index, t in enumerate(nums[i:]):
                 res += t
                 if index > 0 and res % k == 0:
                     return True
         return False
# 前缀和 + 哈希表
class Solution:
    def checkSubarraySum(self, nums, k):
        if len(nums) < 2: return False
        tag  = {0: -1}
        pre = 0
        for index, num in enumerate(nums):
            pre += num
            rem = pre % k
            i = tag .get(rem, index)
            if i == index:
                tag [rem] = index
            elif i <= index - 2:
                return True
        return False
```

#### 参考

##### 方法一：前缀和 + 哈希表

朴素的思路是遍历数组 nums 的每个大小至少为 2 的子数组并计算每个子数组的元素和，判断是否存在一个子数组的元素和为 kk 的倍数。当数组 nums 的长度为 mm 时，上述思路需要用 O(m^2) 的时间遍历全部子数组，对于每个子数组需要 O(m) 的时间计算元素和，因此时间复杂度是 O(m^3)，会超出时间限制，因此必须优化。

如果事先计算出数组 nums 的前缀和数组，则对于任意一个子数组，都可以在 O(1) 的时间内得到其元素和。用 prefixSums[i] 表示数组 nums 从下标 0 到下标 i 的前缀和，则 nums 从下标 p + 1 到下标 q（其中 p < q）的子数组的长度为 q − p，该子数组的元素和为 prefixSums[q] − prefixSums[p]。

如果 prefixSums[q] − prefixSums[p] 为 k 的倍数，且 q − p ≥ 2，则上述子数组即满足大小至少为 2 且元素和为 k 的倍数。

当 prefixSums[q] − prefixSums[p] 为 k 的倍数时，prefixSums[p] 和 prefixSums[q] 除以 k 的余数相同。因此只需要计算每个下标对应的前缀和除以 k 的余数即可，使用哈希表存储每个余数第一次出现的下标。

规定空的前缀的结束下标为 -1，由于空的前缀的元素和为 0，因此在哈希表中存入键值对 (0, -1)。对于 0 ≤ i < m，从小到大依次遍历每个 i，计算每个下标对应的前缀和除以 k 的余数，并维护哈希表：

如果当前余数在哈希表中已经存在，则取出该余数在哈希表中对应的下标 prevIndex，nums 从下标 prevIndex + 1 到下标 i 的子数组的长度为 i − prevIndex，该子数组的元素和为 k 的倍数，如果 i − prevIndex ≥ 2，则找到了一个大小至少为 2 且元素和为 k 的倍数的子数组，返回 true；

如果当前余数在哈希表中不存在，则将当前余数和当前下标 i 的键值对存入哈希表中。

由于哈希表存储的是每个余数第一次出现的下标，因此当遇到重复的余数时，根据当前下标和哈希表中存储的下标计算得到的子数组长度是以当前下标结尾的子数组中满足元素和为 k 的倍数的子数组长度中的最大值。只要最大长度至少为 2，即存在符合要求的子数组。

```c++
// C++
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int m = nums.size();
        if (m < 2) {
            return false;
        }
        unordered_map<int, int> mp;
        mp[0] = -1;
        int remainder = 0;
        for (int i = 0; i < m; i++) {
            remainder = (remainder + nums[i]) % k;
            if (mp.count(remainder)) {
                int prevIndex = mp[remainder];
                if (i - prevIndex >= 2) {
                    return true;
                }
            } else {
                mp[remainder] = i;
            }
        }
        return false;
    }
};
```

```js
// JavaScript
var checkSubarraySum = function (nums, k) {
  const m = nums.length;
  if (m < 2) {
    return false;
  }
  const map = new Map();
  map.set(0, -1);
  let remainder = 0;
  for (let i = 0; i < m; i++) {
    remainder = (remainder + nums[i]) % k;
    if (map.has(remainder)) {
      const prevIndex = map.get(remainder);
      if (i - prevIndex >= 2) {
        return true;
      }
    } else {
      map.set(remainder, i);
    }
  }
  return false;
};
```

```java
// Java
class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        int m = nums.length;
        if (m < 2) {
            return false;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(0, -1);
        int remainder = 0;
        for (int i = 0; i < m; i++) {
            remainder = (remainder + nums[i]) % k;
            if (map.containsKey(remainder)) {
                int prevIndex = map.get(remainder);
                if (i - prevIndex >= 2) {
                    return true;
                }
            } else {
                map.put(remainder, i);
            }
        }
        return false;
    }
}
```

```c#
// C#
public class Solution {
    public bool CheckSubarraySum(int[] nums, int k) {
        int m = nums.Length;
        if (m < 2) {
            return false;
        }
        Dictionary<int, int> dictionary = new Dictionary<int, int>();
        dictionary.Add(0, -1);
        int remainder = 0;
        for (int i = 0; i < m; i++) {
            remainder = (remainder + nums[i]) % k;
            if (dictionary.ContainsKey(remainder)) {
                int prevIndex = dictionary[remainder];
                if (i - prevIndex >= 2) {
                    return true;
                }
            } else {
                dictionary.Add(remainder, i);
            }
        }
        return false;
    }
}
```

```c
// C
struct HashTable {
    int key, val;
    UT_hash_handle hh;
};

bool checkSubarraySum(int* nums, int numsSize, int k) {
    int m = numsSize;
    if (m < 2) {
        return false;
    }
    struct HashTable* hashTable = NULL;
    struct HashTable* tmp = malloc(sizeof(struct HashTable));
    tmp->key = 0, tmp->val = -1;
    HASH_ADD_INT(hashTable, key, tmp);
    int remainder = 0;
    for (int i = 0; i < m; i++) {
        remainder = (remainder + nums[i]) % k;
        HASH_FIND_INT(hashTable, &remainder, tmp);
        if (tmp != NULL) {
            int prevIndex = tmp->val;
            if (i - prevIndex >= 2) {
                return true;
            }
        } else {
            tmp = malloc(sizeof(struct HashTable));
            tmp->key = remainder, tmp->val = i;
            HASH_ADD_INT(hashTable, key, tmp);
        }
    }
    return false;
}
```

```golang
// Golang
func checkSubarraySum(nums []int, k int) bool {
    m := len(nums)
    if m < 2 {
        return false
    }
    mp := map[int]int{0: -1}
    remainder := 0
    for i, num := range nums {
        remainder = (remainder + num) % k
        if prevIndex, has := mp[remainder]; has {
            if i-prevIndex >= 2 {
                return true
            }
        } else {
            mp[remainder] = i
        }
    }
    return false
}
```

**复杂度分析**

- 时间复杂度：O(m)，其中 m 是数组 nums 的长度。需要遍历数组一次。

- 空间复杂度：O(min(m, k))，其中 m 是数组 nums 的长度。空间复杂度主要取决于哈希表，哈希表中存储每个余数第一次出现的下标，最多有 min(m, k) 个余数。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/continuous-subarray-sum/solution/lian-xu-de-zi-shu-zu-he-by-leetcode-solu-rdzi/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
