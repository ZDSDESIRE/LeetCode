### 227.基本计算器 II（中等）

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。

示例 1：

```text
输入：s = "3+2*2"
输出：7
```

示例 2：

```text
输入：s = " 3/2 "
输出：1
```

示例 3：

```text
输入：s = " 3+5 / 2 "
输出：5
```

提示：

- 1 <= s.length <= 3 \* 105
- s 由整数和算符 ('+', '-', '\*', '/') 组成，中间由一些空格隔开
- s 表示一个 有效表达式
- 表达式中的所有整数都是非负整数，且在范围 [0, 231 - 1] 内
- 题目数据保证答案是一个 32-bit 整数

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 字符串（String）  # 栈（Stack）
```

#### 提交

```js
// JavaScript
/**
 * @param {string} s
 * @return {number}
 */
var calculate = function (s) {
  var q = [],
    n = "",
    f = "+";
  for (var i = 0; i < s.length || n; i++) {
    if (s[i] === " ") continue;
    if (/\D/.test(s[i])) {
      switch (f) {
        case "+":
          q.push(n);
          break;
        case "-":
          q.push(-n);
          break;
        case "*":
          q.push(q.pop() * n);
          break;
        case "/":
          q.push((q.pop() / n) | 0);
      }
      (f = s[i]), (n = "");
    } else n += s[i];
  }
  return q.reduce((p, v) => p + (v | 0), 0);
};
```

#### 参考

##### 方法一：栈

**思路**

由于乘除优先于加减计算，因此不妨考虑先进行所有乘除运算，并将这些乘除运算后的整数值放回原表达式的相应位置，则随后整个表达式的值，就等于一系列整数加减后的值。

基于此，我们可以用一个栈，保存这些（进行乘除运算后的）整数的值。对于加减号后的数字，将其直接压入栈中；对于乘除号后的数字，可以直接与栈顶元素计算，并替换栈顶元素为计算后的结果。

具体来说，遍历字符串 s，并用变量 preSign 记录每个数字之前的运算符，对于第一个数字，其之前的运算符视为加号。每次遍历到数字末尾时，根据 preSign 来决定计算方式：

- 加号：将数字压入栈；
- 减号：将数字的相反数压入栈；
- 乘除号：计算数字与栈顶元素，并将栈顶元素替换为计算结果。
  代码实现中，若读到一个运算符，或者遍历到字符串末尾，即认为是遍历到了数字末尾。处理完该数字后，更新 preSign 为当前遍历的字符。

遍历完字符串 s 后，将栈中元素累加，即为该字符串表达式的值。

**代码**

```c++
// C++
class Solution {
public:
    int calculate(string s) {
        vector<int> stk;
        char preSign = '+';
        int num = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            if (isdigit(s[i])) {
                num = num * 10 + int(s[i] - '0');
            }
            if (!isdigit(s[i]) && s[i] != ' ' || i == n - 1) {
                switch (preSign) {
                    case '+':
                        stk.push_back(num);
                        break;
                    case '-':
                        stk.push_back(-num);
                        break;
                    case '*':
                        stk.back() *= num;
                        break;
                    default:
                        stk.back() /= num;
                }
                preSign = s[i];
                num = 0;
            }
        }
        return accumulate(stk.begin(), stk.end(), 0);
    }
};
```

```java
// Java
class Solution {
    public int calculate(String s) {
        Deque<Integer> stack = new LinkedList<Integer>();
        char preSign = '+';
        int num = 0;
        int n = s.length();
        for (int i = 0; i < n; ++i) {
            if (Character.isDigit(s.charAt(i))) {
                num = num * 10 + s.charAt(i) - '0';
            }
            if (!Character.isDigit(s.charAt(i)) && s.charAt(i) != ' ' || i == n - 1) {
                switch (preSign) {
                    case '+':
                        stack.push(num);
                        break;
                    case '-':
                        stack.push(-num);
                        break;
                    case '*':
                        stack.push(stack.pop() * num);
                        break;
                    default:
                        stack.push(stack.pop() / num);
                }
                preSign = s.charAt(i);
                num = 0;
            }
        }
        int ans = 0;
        while (!stack.isEmpty()) {
            ans += stack.pop();
        }
        return ans;
    }
}
```

```py
# Python3
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        preSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if preSign == '+':
                    stack.append(num)
                elif preSign == '-':
                    stack.append(-num)
                elif preSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preSign = s[i]
                num = 0
        return sum(stack)
```

```c
// C
int calculate(char* s) {
    int n = strlen(s);
    int stk[n], top = 0;
    char preSign = '+';
    int num = 0;
    for (int i = 0; i < n; ++i) {
        if (isdigit(s[i])) {
            num = num * 10 + (int)(s[i] - '0');
        }
        if (!isdigit(s[i]) && s[i] != ' ' || i == n - 1) {
            switch (preSign) {
                case '+':
                    stk[top++] = num;
                    break;
                case '-':
                    stk[top++] = -num;
                    break;
                case '*':
                    stk[top - 1] *= num;
                    break;
                default:
                    stk[top - 1] /= num;
            }
            preSign = s[i];
            num = 0;
        }
    }
    int ret = 0;
    for (int i = 0; i < top; i++) {
        ret += stk[i];
    }
    return ret;
}
```

```js
// JavaScript
var calculate = function (s) {
  s = s.trim();
  const stack = new Array();
  let preSign = "+";
  let num = 0;
  const n = s.length;
  for (let i = 0; i < n; ++i) {
    if (!isNaN(Number(s[i])) && s[i] !== " ") {
      num = num * 10 + s[i].charCodeAt() - "0".charCodeAt();
    }
    if (isNaN(Number(s[i])) || i === n - 1) {
      switch (preSign) {
        case "+":
          stack.push(num);
          break;
        case "-":
          stack.push(-num);
          break;
        case "*":
          stack.push(stack.pop() * num);
          break;
        default:
          stack.push((stack.pop() / num) | 0);
      }
      preSign = s[i];
      num = 0;
    }
  }
  let ans = 0;
  while (stack.length) {
    ans += stack.pop();
  }
  return ans;
};
```

```golang
func calculate(s string) (ans int) {
    stack := []int{}
    preSign := '+'
    num := 0
    for i, ch := range s {
        isDigit := '0' <= ch && ch <= '9'
        if isDigit {
            num = num*10 + int(ch-'0')
        }
        if !isDigit && ch != ' ' || i == len(s)-1 {
            switch preSign {
            case '+':
                stack = append(stack, num)
            case '-':
                stack = append(stack, -num)
            case '*':
                stack[len(stack)-1] *= num
            default:
                stack[len(stack)-1] /= num
            }
            preSign = ch
            num = 0
        }
    }
    for _, v := range stack {
        ans += v
    }
    return
}
```

**复杂度分析**

- 时间复杂度：O(n)，其中 n 为字符串 s 的长度。需要遍历字符串 s 一次，计算表达式的值。

- 空间复杂度：O(n)，其中 n 为字符串 s 的长度。空间复杂度主要取决于栈的空间，栈的元素个数不超过 n。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/basic-calculator-ii/solution/ji-ben-ji-suan-qi-ii-by-leetcode-solutio-cm28/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
