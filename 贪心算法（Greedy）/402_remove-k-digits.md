### 402.移掉 K 位数字（中等）

给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。

注意:

- num 的长度小于 10002 且  ≥ k。
- num 不会包含任何前导零。
  示例 1 :

```text
输入: num = "1432219", k = 3
输出: "1219"
解释: 移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219。
```

示例 2 :

```text
输入: num = "10200", k = 1
输出: "200"
解释: 移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
```

示例 3 :

```text
输入: num = "10", k = 2
输出: "0"
解释: 从原数字移除所有的数字，剩余为空就是0。
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-k-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 栈（Stack）  # 贪心算法（Greedy）
```

#### 提交

```py
# Python3
# 计数法 + 单调栈
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        while k > 0:
            stack.pop()
            k -= 1

        index = -1
        for l in range(len(stack)):
            if stack[l] != '0':
                index = l
                break
        if index == -1:
            return '0'
        else:
            return ''.join(stack[index:])
# 使用内置函数 lstrip()
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)

        while k > 0:
            stack.pop()
            k -= 1

        return ''.join(stack).lstrip('0') or '0'
```

#### 参考

##### 方法一：贪心 + 单调栈

对于两个相同长度的数字序列，最左边不同的数字决定了这两个数字的大小，例如，对于 A = 1axxx，B = 1bxxx，如果 a > b 则 A > B。

基于此，我们可以知道，若要使得剩下的数字最小，需要保证靠前的数字尽可能小。

![1](https://assets.leetcode-cn.com/solution-static/402/402_fig1.png)

让我们从一个简单的例子开始。给定一个数字序列，例如 425，如果要求我们只删除一个数字，那么从左到右，我们有 4、2 和 5 三个选择。我们将每一个数字和它的左邻居进行比较。从 2 开始，2 小于它的左邻居 4。假设我们保留数字 4，那么所有可能的组合都是以数字 4（即 42，45）开头的。相反，如果移掉 4，留下 2，我们得到的是以 2 开头的组合（即 25），这明显小于任何留下数字 4 的组合。因此我们应该移掉数字 4。如果不移掉数字 4，则之后无论移掉什么数字，都不会得到最小数。

基于上述分析，我们可以得出「删除一个数字」的贪心策略：

给定一个长度为 n 的数字序列 [D_0D_1D_2D_3 ... D_{n-1}]，从左往右找到第一个位置 i（i>0）使得 D*i < D*{i-1}，并删去 D\_{i-1}；如果不存在，说明整个数字序列单调不降，删去最后一个数字即可。

基于此，我们可以每次对整个数字序列执行一次这个策略；删去一个字符后，剩下的 n-1 长度的数字序列就形成了新的子问题，可以继续使用同样的策略，直至删除 k 次。

然而暴力的实现复杂度最差会达到 O(nk)（考虑整个数字序列是单调不降的），因此我们需要加速这个过程。

考虑从左往右增量的构造最后的答案。我们可以用一个栈维护当前的答案序列，栈中的元素代表截止到当前位置，删除不超过 k 次个数字后，所能得到的最小整数。根据之前的讨论：在使用 k 个删除次数之前，栈中的序列从栈底到栈顶单调不降。

因此，对于每个数字，如果该数字小于栈顶元素，我们就不断地弹出栈顶元素，直到

- 栈为空
- 或者新的栈顶元素不大于当前数字
- 或者我们已经删除了 kk 位数字

上述步骤结束后我们还需要针对一些情况做额外的处理：

- 如果我们删除了 m 个数字且 m < k，这种情况下我们需要从序列尾部删除额外的 k − m 个数字。
- 如果最终的数字序列存在前导零，我们要删去前导零。
- 如果最终数字序列为空，我们应该返回 00。
  最终，从栈底到栈顶的答案序列即为最小数。

考虑到栈的特点是后进先出，如果通过栈实现，则需要将栈内元素依次弹出然后进行翻转才能得到最小数。为了避免翻转操作，可以使用双端队列代替栈的实现。

```py
# Python3
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numStack = []

        # 构建单调递增的数字串
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # 如果 K > 0，删除末尾的 K 个字符
        finalStack = numStack[:-k] if k else numStack

        # 抹去前导零
        return "".join(finalStack).lstrip('0') or "0"
```

```c++
// C++
class Solution {
public:
    string removeKdigits(string num, int k) {
        vector<char> stk;
        for (auto& digit: num) {
            while (stk.size() > 0 && stk.back() > digit && k) {
                stk.pop_back();
                k -= 1;
            }
            stk.push_back(digit);
        }

        for (; k > 0; --k) {
            stk.pop_back();
        }

        string ans = "";
        bool isLeadingZero = true;
        for (auto& digit: stk) {
            if (isLeadingZero && digit == '0') {
                continue;
            }
            isLeadingZero = false;
            ans += digit;
        }
        return ans == "" ? "0" : ans;
    }
};
```

```java
// Java
class Solution {
    public String removeKdigits(String num, int k) {
        Deque<Character> deque = new LinkedList<Character>();
        int length = num.length();
        for (int i = 0; i < length; ++i) {
            char digit = num.charAt(i);
            while (!deque.isEmpty() && k > 0 && deque.peekLast() > digit) {
                deque.pollLast();
                k--;
            }
            deque.offerLast(digit);
        }

        for (int i = 0; i < k; ++i) {
            deque.pollLast();
        }

        StringBuilder ret = new StringBuilder();
        boolean leadingZero = true;
        while (!deque.isEmpty()) {
            char digit = deque.pollFirst();
            if (leadingZero && digit == '0') {
                continue;
            }
            leadingZero = false;
            ret.append(digit);
        }
        return ret.length() == 0 ? "0" : ret.toString();
    }
}
```

```js
// JavaScript
var removeKdigits = function (num, k) {
  const stk = [];
  for (const digit of num) {
    while (stk.length > 0 && stk[stk.length - 1] > digit && k) {
      stk.pop();
      k -= 1;
    }
    stk.push(digit);
  }

  for (; k > 0; --k) {
    stk.pop();
  }

  let ans = "";
  let isLeadingZero = true;
  for (const digit of stk) {
    if (isLeadingZero && digit === "0") {
      continue;
    }
    isLeadingZero = false;
    ans += digit;
  }
  return ans === "" ? "0" : ans;
};
```

```golang
// Golang
func removeKdigits(num string, k int) string {
    stack := []byte{}
    for i := range num {
        digit := num[i]
        for k > 0 && len(stack) > 0 && digit < stack[len(stack)-1] {
            stack = stack[:len(stack)-1]
            k--
        }
        stack = append(stack, digit)
    }
    stack = stack[:len(stack)-k]
    ans := strings.TrimLeft(string(stack), "0")
    if ans == "" {
        ans = "0"
    }
    return ans
}
```

```c
// C
char* removeKdigits(char* num, int k) {
    int n = strlen(num), top = 0;
    char* stk = malloc(sizeof(char) * (n + 1));
    for (int i = 0; i < n; i++) {
        while (top > 0 && stk[top] > num[i] && k) {
            top--, k--;
        }
        stk[++top] = num[i];
    }
    top -= k;

    char* ans = malloc(sizeof(char) * (n + 1));
    int ansSize = 0;
    bool isLeadingZero = true;
    for (int i = 1; i <= top; i++) {
        if (isLeadingZero && stk[i] == '0') {
            continue;
        }
        isLeadingZero = false;
        ans[ansSize++] = stk[i];
    }
    if (ansSize == 0) {
        ans[0] = '0', ans[1] = 0;
    } else {
        ans[ansSize] = 0;
    }
    return ans;
}
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 为字符串的长度。尽管存在嵌套循环，但内部循环最多运行 k 次。由于 0 < k ≤ n，主循环的时间复杂度被限制在 2n 以内。对于主循环之外的逻辑，它们的时间复杂度是 O(n)，因此总时间复杂度为 O(n)。

- 空间复杂度：O(n)。栈存储数字需要线性的空间。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/remove-k-digits/solution/yi-diao-kwei-shu-zi-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
