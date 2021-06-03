### 525. 连续数组（中等）

给定一个二进制数组 nums , 找到含有相同数量的 0 和 1 的最长连续子数组，并返回该子数组的长度。

示例 1:

```text
输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量0和1的最长连续子数组。
```

示例 2:

```text
输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
```

提示：

- 1 <= nums.length <= 105
- nums[i] 不是 0 就是 1

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contiguous-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 哈希表（Hash Table）
```

#### 提交

```py
# Python3
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        pre = 0
        dic = {0: -1}
        ans = 0
        for i in range(n):
            if nums[i] == 0:
                pre += -1
            else:
                pre += nums[i]
            if pre not in dic:
                dic[pre] = i
            else:
                tmp = i - dic[pre]
                if tmp > ans:
                    ans = tmp
        return ans
```

#### 参考

##### 方法一：前缀和 + 哈希表

由于「0 和 1 的数量相同」等价于「1 的数量减去 0 的数量等于 0」，我们可以将数组中的 0 视作 -1，则原问题转换成「求最长的连续子数组，其元素和为 0」。

设数组 nums 的长度为 n，将数组 nums 进行转换得到长度相等的新数组 newNums：对于 0 ≤ i < n，当 nums[i] = 1 时 newNums[i] = 1，当 nums[i] = 0 时 newNums[i] = −1。

为了快速计算 newNums 的子数组的元素和，需要首先计算 newNums 的前缀和。用 prefixSums[i] 表示 newNums 从下标 0 到下标 i 的前缀和，则 newNums 从下标 j + 1 到下标 k（其中 j < k）的子数组的元素和为 prefixSums[k] − prefixSums[j]，该子数组的长度为 k - j。

当 prefixSums[k] − prefixSums[j] = 0 时，即得到 newNums 的一个长度为 k - j 的子数组元素和为 0，对应 nums 的一个长度为 k - j 的子数组中有相同数量的 0 和 1。

实现方面，不需要创建数组 newNums 和 prefixSums，只需要维护一个变量 counter 存储 newNums 的前缀和即可。具体做法是，遍历数组 nums，当遇到元素 1 时将 counter 的值加 1，当遇到元素 0 时将 counter 的值减 1，遍历过程中使用哈希表存储每个前缀和第一次出现的下标。

规定空的前缀的结束下标为 -1，由于空的前缀的元素和为 0，因此在遍历之前，首先在哈希表中存入键值对 (0, −1)。遍历过程中，对于每个下标 i，进行如下操作：

- 如果 counter 的值在哈希表中已经存在，则取出 counter 在哈希表中对应的下标 prevIndex，nums 从下标 prevIndex + 1 到下标 i 的子数组中有相同数量的 0 和 1，该子数组的长度为 i - prevIndex，使用该子数组的长度更新最长连续子数组的长度；
- 如果 counter 的值在哈希表中不存在，则将当前余数和当前下标 i 的键值对存入哈希表中。

由于哈希表存储的是 counter 的每个取值第一次出现的下标，因此当遇到重复的前缀和时，根据当前下标和哈希表中存储的下标计算得到的子数组长度是以当前下标结尾的子数组中满足有相同数量的 0 和 1 的最长子数组的长度。遍历结束时，即可得到 nums 中的有相同数量的 0 和 1 的最长子数组的长度。

```c++
// C++
class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int maxLength = 0;
        unordered_map<int, int> mp;
        int counter = 0;
        mp[counter] = -1;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (num == 1) {
                counter++;
            } else {
                counter--;
            }
            if (mp.count(counter)) {
                int prevIndex = mp[counter];
                maxLength = max(maxLength, i - prevIndex);
            } else {
                mp[counter] = i;
            }
        }
        return maxLength;
    }
};
```

```java
// Java
class Solution {
    public int findMaxLength(int[] nums) {
        int maxLength = 0;
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        int counter = 0;
        map.put(counter, -1);
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (num == 1) {
                counter++;
            } else {
                counter--;
            }
            if (map.containsKey(counter)) {
                int prevIndex = map.get(counter);
                maxLength = Math.max(maxLength, i - prevIndex);
            } else {
                map.put(counter, i);
            }
        }
        return maxLength;
    }
}
```

```js
// JavaScript
var findMaxLength = function (nums) {
  let maxLength = 0;
  const map = new Map();
  let counter = 0;
  map.set(counter, -1);
  const n = nums.length;
  for (let i = 0; i < n; i++) {
    const num = nums[i];
    if (num == 1) {
      counter++;
    } else {
      counter--;
    }
    if (map.has(counter)) {
      const prevIndex = map.get(counter);
      maxLength = Math.max(maxLength, i - prevIndex);
    } else {
      map.set(counter, i);
    }
  }
  return maxLength;
};
```

```c#
// C#
public class Solution {
    public int FindMaxLength(int[] nums) {
        int maxLength = 0;
        Dictionary<int, int> dictionary = new Dictionary<int, int>();
        int counter = 0;
        dictionary.Add(counter, -1);
        int n = nums.Length;
        for (int i = 0; i < n; i++) {
            int num = nums[i];
            if (num == 1) {
                counter++;
            } else {
                counter--;
            }
            if (dictionary.ContainsKey(counter)) {
                int prevIndex = dictionary[counter];
                maxLength = Math.Max(maxLength, i - prevIndex);
            } else {
                dictionary.Add(counter, i);
            }
        }
        return maxLength;
    }
}
```

```c
// C
struct HashTable {
    int key, val;
    UT_hash_handle hh;
};

int findMaxLength(int* nums, int numsSize) {
    int maxLength = 0;
    struct HashTable* hashTable = NULL;
    struct HashTable* tmp = malloc(sizeof(struct HashTable));
    tmp->key = 0, tmp->val = -1;
    HASH_ADD_INT(hashTable, key, tmp);
    int counter = 0;
    int n = numsSize;
    for (int i = 0; i < n; i++) {
        int num = nums[i];
        if (num == 1) {
            counter++;
        } else {
            counter--;
        }
        HASH_FIND_INT(hashTable, &counter, tmp);
        if (tmp != NULL) {
            int prevIndex = tmp->val;
            maxLength = fmax(maxLength, i - prevIndex);
        } else {
            tmp = malloc(sizeof(struct HashTable));
            tmp->key = counter, tmp->val = i;
            HASH_ADD_INT(hashTable, key, tmp);
        }
    }
    return maxLength;
}
```

```golang
// Golang
func findMaxLength(nums []int) (maxLength int) {
    mp := map[int]int{0: -1}
    counter := 0
    for i, num := range nums {
        if num == 1 {
            counter++
        } else {
            counter--
        }
        if prevIndex, has := mp[counter]; has {
            maxLength = max(maxLength, i-prevIndex)
        } else {
            mp[counter] = i
        }
    }
    return
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 是数组 nums 的长度。需要遍历数组一次。

- 空间复杂度：O(n)，其中 n 是数组 nums 的长度。空间复杂度主要取决于哈希表，哈希表中存储的不同的 counter 的值不超过 n 个。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/contiguous-array/solution/lian-xu-shu-zu-by-leetcode-solution-mvnm/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
