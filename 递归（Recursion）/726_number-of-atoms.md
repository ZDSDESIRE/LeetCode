### 726. 原子的数量（困难）

给定一个化学式 formula（作为字符串），返回每种原子的数量。

原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。例如，H2O 和 H2O2 是可行的，但 H1O2 这个表达是不可行的。

两个化学式连在一起是新的化学式。例如  H2O2He3Mg4 也是化学式。

一个括号中的化学式和数字（可选择性添加）也是化学式。例如 (H2O2) 和 (H2O2)3 是化学式。

给定一个化学式，输出所有原子的数量。格式为：第一个（按字典序）原子的名子，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

示例 1:

```text
输入:
formula = "H2O"
输出: "H2O"
解释:
原子的数量是 {'H': 2, 'O': 1}。
```

示例 2:

```text
输入:
formula = "Mg(OH)2"
输出: "H2MgO2"
解释:
原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。
```

示例 3:

```text
输入:
formula = "K4(ON(SO3)2)2"
输出: "K4N2O14S4"
解释:
原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。
```

注意:

- 所有原子的第一个字母为大写，剩余字母都是小写。
- formula 的长度在[1, 1000]之间。
- formula 只包含字母、数字和圆括号，并且题目中给定的是合法的化学式。

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-atoms
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 递归（Recursion）  # 栈（Stack）  # 哈希表（Hash Table）  # 字符串（String）
```

#### 提交

**解题思路**：使用递归解析化学式

定义一个词法分析器，能解析原字符串，读入词元 term（可能为原子名，左括号，右括号，数字）
然后使用上面的词法分析器，依次读入 term，该 term:

- 如果是原子名，设置为当前原子 atom，并将原子数+1
- 如果是整数 n，将当前原子数+(n-1)
- 如果是左括号，进入递归处理，将递归程序返回值 subCounter 记录下来，并读入下一个词元，如果词元是数值 m，将 subCounter\*m 更新到当前计数器
- 如果是右括号，将当前计数器返回上一级

**代码**

```py
# Python3
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        self.i = 0
        n = len(formula)

        # 词法分析，读取下一个词元
        def nextTerm():
            if self.i == n:
                return None
            if formula[self.i].isupper():  # 原子名
                j = self.i + 1
                while j < n and formula[j].islower():
                    j += 1
                start = self.i
                self.i = j
                return formula[start:j]
            if formula[self.i].isdigit():  # 数字
                j = self.i + 1
                while j < n and formula[j].isdigit():
                    j += 1
                start = self.i
                self.i = j
                return int(formula[start:j])
            if formula[self.i] == '(':
                self.i += 1
                return '('
            if formula[self.i] == ')':
                self.i += 1
                return ')'

        import collections

        # 原子表达式解析
        def expr():
            counter = collections.Counter()
            term = nextTerm()
            atom = None
            while term:
                if isinstance(term, int):  # 如果是数值，需要将当前原子数增加
                    counter[atom] += term - 1
                    term = nextTerm()
                elif term == '(':
                    subcounter = expr()  # 如果是左括号，进入子表达式处理
                    term = nextTerm()
                    if isinstance(term, int):  # 如果子表达式后面跟着数值，需要将子表达式计数器乘以数值
                        for a, c in subcounter.most_common():
                            subcounter[a] = c * term
                        term = nextTerm()
                    counter.update(subcounter)  # 将子表达式的计数器更新到当前计数器里面
                elif term == ')':  # 如果是右括号，将当前表达式的计数器返回给上级
                    return counter
                else:  # 如果是原子，计数器中增加1个原子
                    atom = term
                    counter[atom] += 1
                    term = nextTerm()
            return counter

        # 对计数器中的原子按照字典序进行排序后输出
        counter = expr()
        ans = []
        for atom, count in sorted(counter.most_common(), key=lambda item: item[0]):
            ans.append(atom)
            if count > 1:
                ans.append(str(count))
        return ''.join(ans)
```

**复杂度分析**

- 时间复杂度：O(n^2)，一次遍历，每次递归函数中需要累计每个原子的数量。
- 空间复杂度：O(n)，需要使用计数器累计所有原子数。

#### 参考

##### 方法一：栈 + 哈希表

对于括号序列相关的题目，通用的解法是使用递归或栈。本题中我们将使用栈解决。

从左到右遍历该化学式，并使用哈希表记录当前层遍历到的原子及其数量，因此初始时需将一个空的哈希表压入栈中。对于当前遍历的字符：

- 如果是左括号，将一个空的哈希表压入栈中，进入下一层。
- 如果不是括号，则读取一个原子名称，若后面还有数字，则读取一个数字，否则将该原子后面的数字视作 1。然后将原子及数字加入栈顶的哈希表中。
- 如果是右括号，则说明遍历完了当前层，若括号右侧还有数字，则读取该数字 num，否则将该数字视作 1。然后将栈顶的哈希表弹出，将弹出的哈希表中的原子数量与 num 相乘，加到上一层的原子数量中。

遍历结束后，栈顶的哈希表即为化学式中的原子及其个数。遍历哈希表，取出所有「原子-个数」对加入数组中，对数组按照原子字典序排序，然后遍历数组，按题目要求拼接成答案。

```js
// JavaScript
var countOfAtoms = function (formula) {
  let i = 0;
  const n = formula.length;

  const stack = [new Map()];
  while (i < n) {
    const ch = formula[i];

    const parseAtom = () => {
      const sb = [];
      sb.push(formula[i++]); // 扫描首字母
      while (i < n && formula[i] >= "a" && formula[i] <= "z") {
        sb.push(formula[i++]); // 扫描首字母后的小写字母
      }
      return sb.join("");
    };

    const parseNum = () => {
      if (i === n || isNaN(Number(formula[i]))) {
        return 1; // 不是数字，视作 1
      }
      let num = 0;
      while (i < n && !isNaN(Number(formula[i]))) {
        num = num * 10 + formula[i++].charCodeAt() - "0".charCodeAt(); // 扫描数字
      }
      return num;
    };

    if (ch === "(") {
      i++;
      stack.unshift(new Map()); // 将一个空的哈希表压入栈中，准备统计括号内的原子数量
    } else if (ch === ")") {
      i++;
      const num = parseNum(); // 括号右侧数字
      const popMap = stack.shift(); // 弹出括号内的原子数量
      const topMap = stack[0];
      for (const [atom, v] of popMap.entries()) {
        topMap.set(atom, (topMap.get(atom) || 0) + v * num); // 将括号内的原子数量乘上 num，加到上一层的原子数量中
      }
    } else {
      const atom = parseAtom();
      const num = parseNum();
      const topMap = stack[0];
      topMap.set(atom, (topMap.get(atom) || 0) + num); // 统计原子数量
    }
  }

  let map = stack.pop();
  map = Array.from(map);
  map.sort();
  const sb = [];
  for (const [atom, count] of map) {
    sb.push(atom);
    if (count > 1) {
      sb.push(count);
    }
  }
  return sb.join("");
};
```

**复杂度分析**

- 时间复杂度：O(n^2)。其中 n 是化学式 formula 的长度。
  最坏情况下栈有 O(n) 层，每次出栈时需要更新 O(n) 个原子的数量，因此遍历化学式的时间复杂度为 O(n^2)。
  遍历结束后排序的时间复杂度为 O(nlogn)。
  因此总的时间复杂度为 O(n^2 + nlogn) = O(n^2)。

- 空间复杂度：O(n)。空间复杂度取决于栈中所有哈希表中的元素个数之和，而这不会超过化学式 formula 的长度，因此空间复杂度为 O(n)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-atoms/solution/yuan-zi-de-shu-liang-by-leetcode-solutio-54lv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
