### 5.最长回文子串（中等）

给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

注意：
回文就是指一个正着读和反着读都一样的字符串。

示例 1：

```text
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
```

示例 2：

```text
输入: "cbbd"
输出: "bb"
```

##### 相关题目：[409.最长回文串](409_longest-palindrome.md)

#### 提交

##### 提交 1（算法有误，题目理解有误导致）

```py
# Python3
import collections

class Solution:
    def longestPalindrome(self, s: str) -> str:
        count = collections.Counter(s)
        keys = []
        flag = ''
        for k, v in count.items():
            if v % 2 == 1:
                if flag == '':
                    flag = k
                    keys.insert(len(keys) // 2 - 1, k)
                else:
                    n = v // 2
                    keys.insert(0, k * n)
                    keys.append(k * n)
            else:
                n = v // 2
                keys.insert(0, k * n)
                keys.append(k * n)
        return ''.join(keys)
```

##### 提交 2

```py
# Python3
class Solution:
    def checkPolindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return False
            i+=1
            j-=1
        return True

    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        # 二分长度, 直接二分长度不行，因为3个成立，2个有可能不成立
        # 但是长度为4成立，则2一定成立，长度为5成立，则3一定成立
        # 因此每次判断两个一奇一偶，不满足才能长度减一。
        ans = ''
        l = 0
        r = len(s)
        while l<=r:
            mid = (l+r)//2
            find = False

            for i in range(len(s)-mid+1):
                if self.checkPolindrome(s[i:i+mid]):
                    find = True
                    ans = s[i:i+mid]
                    break

            for i in range(len(s)-mid):
                if self.checkPolindrome(s[i:i+mid+1]):
                    find = True
                    ans = s[i:i+mid+1]
                    break
            if find:
                l = mid + 1
            else:
                r = mid - 1
        return ans
```

#### 参考

```py
class Solution:
    # 中心扩散法Spread From Center
    def spread(self, s, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    # manacher法专门用来解决回文字符串的问题
    def mancher(self, s:str) -> str:
        '''
        这是一个复杂度为 O(n) 的 Manacher 算法。
        假如字符串是奇数个，那么我们可以通过遍历所有字符串，再对所有字符串进行左右匹配，就像中心扩散方法一样。然后得到长度最大的字符串
        但是如果字符串是偶数个，我们无法进行此操作
        这个算法的最终要的额一点就是，我们将一个偶数长/奇数长的字符串，构造成新的字符串。
        这样我们可以对新字符串的每个字符，进行左右匹配。
        '''
        if len(s) < 2:
            return s
        # 将一个可能是偶数长/奇数长的字符串，首位以及每个字符间添加#
        test = '#'+'#'.join(s)+'#'
        # 当前遍历的中心最大扩散步数，其值等于原始字符串的最长回文子串的长度
        max_len = 0
        for i in range(len(test)):
            left = i - 1
            right = i + 1
            step = 0
            print(test[i])
            while left >= 0 and right < len(test) and test[left] == test[right]:
                # print("spread",test[left],test[right])
                left -= 1
                right += 1
                step += 1
                # print(step)

            if step > max_len:
                max_len = step
                start = (i - max_len) // 2
        return s[start: start + max_len]

    # 动态规划法-中心扩散法Spread From Center
    def spread_from_center(self, s:str) -> str:
        '''
        中心扩散法:
        为了改进暴力法，我们首先观察如何避免在验证回文时进行不必要的重复计算。考虑“ababa” 一定是回文，因为它的左首字母和右尾字母是相同的。
        我们给出 P(i,j) 的定义如下：
            如果子串S_i和S_j是回文字符串则P(i,j)为ture
            其他情况，P(i,j)为false
        因此   P(i,j)=(P(i+1,j−1) and S_i==S_j)
        基本示例如下：
            P(i, i) = true
            P(i, i+1) = ( S_i == S_{i+1} )
        这产生了一个直观的动态规划解法，我们首先初始化一字母和二字母的回文，然后找到所有三字母回文，并依此类推…
        复杂度分析
            时间复杂度：O(n^2)
            空间复杂度：O(1)
        '''

        if s==s[::-1]:
            return s
        res = s[:1]
        for i in range(len(s)):
            palindrome_odd= self.spread(s,i, i)
            palindrome_even= self.spread(s,i, i + 1)
            # 当前找到的最长回文子串
            res = max(palindrome_odd,palindrome_even,res,key=len)
        return res

    # 暴力法
    def force(self, s: str) -> str:
        '''
        很明显，暴力法将选出所有子字符串可能的开始和结束位置，并检验它是不是回文。
        时间复杂度：O(n^2),往往利用python的切片可以很好的缩减复杂度
        如果不用切片，还需要遍历一次子字符串，时间复杂度就是O(^3)
        空间复杂度：O(1)
        '''

        if s==s[::-1]:
            return s
        max_len = 1
        res = s[0]
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
                    max_len = j - i + 1
                    res = s[i:j + 1]
        return res
    def longestPalindrome(self, s: str) -> str:
        return{
            1 : lambda s:self.force(s),
            2 : lambda s:self.spread_from_center(s),
            3 : lambda s:self.mancher(s),
        }[3](s)
```

```py
# 马拉车算法
# 先在字符串中间加符号隔开，使得奇偶回文数的形式统一
# 然后用kmp的思想去优化中心扩散
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)== 0:return ""
        s_new  = '#' + '#'.join(s) + '#'
        #print(s_new)

        #已遍历的最大右边界
        mx = 0
        #对应的中心点
        mid = 0

        l = len(s_new)
        # 扩散半径数组，初始值1或者0都可以，只是代表刚开始的时候扩散半径是多少而已
        p = [1]*l

        for i in range(l):
            if i<mx:
                # 这个时候可以用已经计算过的值
                # 不能超过已遍历的右边界
                # i对应的镜像 = 2*mid - i
                # 由mx定义可知半径最长不会超过mx-i
                p[i] = min(mx-i,p[2*mid-i])

            # 主要的优化已经在上面节省了时间，接下来就是正常的扩散
            while( i-p[i]>=0 and i+p[i]<l and s_new[i-p[i]] == s_new[i+p[i]]):
                p[i] += 1

            # 记录一下mx和mid
            if i+p[i] > mx:
                mx = i+p[i]
                mid = i

        maxr = max(p)
        ans = p.index(maxr)
        # 因为跳出循环的时候多加了1，所以实际上的扩散半径应该减1
        maxr -= 1

        return s_new[ans-maxr:ans+maxr+1].replace('#',"")
```

##### 方法一：最长公共子串

**常见错误**

有些人会忍不住提出一个快速的解决方案，不幸的是，这个解决方案有缺陷(但是可以很容易地纠正)：
反转 S，使之变成 S'。找到 S 和 S'之间最长的公共子串，这也必然是最长的回文子串。

这似乎是可行的，让我们看看下面的一些例子。

例如，S = "caba", S' = "abac"：S 以及 S'之间的最长公共子串为 “aba”，恰恰是答案。

让我们尝试一下这个例子：S = “abacdfgdcaba”, S' = “abacdgfdcaba”，S 以及 S'之间的最长公共子串为 “abacd”。显然，这不是回文。

**算法**

我们可以看到，当 S 的其他部分中存在非回文子串的反向副本时，最长公共子串法就会失败。为了纠正这一点，每当我们找到最长的公共子串的候选项时，都需要检查子串的索引是否与反向子串的原始索引相同。如果相同，那么我们尝试更新目前为止找到的最长回文子串；如果不是，我们就跳过这个候选项并继续寻找下一个候选。

这给我们提供了一个复杂度为 O(n^2) 动态规划解法，它将占用 O(n^2) 的空间（可以改进为使用 O(n) 的空间）。请在 这里 阅读更多关于最长公共子串的内容。

##### 方法二：暴力法

很明显，暴力法将选出所有子字符串可能的开始和结束位置，并检验它是不是回文。

**复杂度分析**

- 时间复杂度：O(n^3)，假设 n 是输入字符串的长度，则 ({n}{2}) = n(n-1)}/2 为此类子字符串(不包括字符本身是回文的一般解法)的总数。因为验证每个子字符串需要 O(n) 的时间，所以运行时间复杂度是 O(n^3)。

- 空间复杂度：O(1)。

##### 方法三：动态规划

为了改进暴力法，我们首先观察如何避免在验证回文时进行不必要的重复计算。考虑 “ababa” 这个示例。如果我们已经知道 “bab” 是回文，那么很明显，“ababa” 一定是回文，因为它的左首字母和右尾字母是相同的。

我们给出 P(i, j) 的定义如下：

```text
P(i, j) = {
true, // 如果子串 S_i...S_j 是回文子串
false, // 其他情况
}
```

因此，

```text
P(i, j) = (P(i + 1, j-1) and S_i == S_j)
```

基本示例如下：

```text
P(i, i) = true
P(i, i + 1) = (S_i == S_{i + 1})
```

这产生了一个直观的动态规划解法，我们首先初始化一字母和二字母的回文，然后找到所有三字母回文，并依此类推…

**复杂度分析**

- 时间复杂度：O(n^2)，这里给出我们的运行时间复杂度为 O(n^2) 。

- 空间复杂度：O(n^2)，该方法使用 O(n^2) 的空间来存储表。

##### 方法四：中心扩展算法

事实上，只需使用恒定的空间，我们就可以在 O(n^2) 的时间内解决这个问题。

我们观察到回文中心的两侧互为镜像。因此，回文可以从它的中心展开，并且只有 2n - 1 个这样的中心。

你可能会问，为什么会是 2n - 1 个，而不是 n 个中心？原因在于所含字母数为偶数的回文的中心可以处于两字母之间（例如 “abba” 的中心在两个 ‘b’ 之间）。

```java
// Java
public String longestPalindrome(String s) {
    if (s == null || s.length() < 1) return "";
    int start = 0, end = 0;
    for (int i = 0; i < s.length(); i++) {
        int len1 = expandAroundCenter(s, i, i);
        int len2 = expandAroundCenter(s, i, i + 1);
        int len = Math.max(len1, len2);
        if (len > end - start) {
            start = i - (len - 1) / 2;
            end = i + len / 2;
        }
    }
    return s.substring(start, end + 1);
}

private int expandAroundCenter(String s, int left, int right) {
    int L = left, R = right;
    while (L >= 0 && R < s.length() && s.charAt(L) == s.charAt(R)) {
        L--;
        R++;
    }
    return R - L - 1;
}
```

**复杂度分析**

- 时间复杂度：O(n^2)，由于围绕中心来扩展回文会耗去 O(n) 的时间，所以总的复杂度为 O(n^2)。

- 空间复杂度：O(1)。

##### 方法五：Manacher 算法

还有一个复杂度为 O(n) 的 Manacher 算法。然而，这是一个非同寻常的算法，在 45 分钟的编码时间内提出这个算法将会是一个不折不扣的挑战。理解它，我保证这将是非常有趣的。

**注：**
作者：LeetCode
链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
