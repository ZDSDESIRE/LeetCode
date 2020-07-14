### 剑指 Offer 09.用两个栈实现队列（简单）

用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )

示例 1：

```text
输入：
["CQueue","appendTail","deleteHead","deleteHead"]
[[],[3],[],[]]
输出：[null,null,3,-1]
```

示例 2：

```text
输入：
["CQueue","deleteHead","appendTail","appendTail","deleteHead","deleteHead"]
[[],[],[5],[2],[],[]]
输出：[null,-1,null,null,5,2]
```

提示：

- 1 <= values <= 10000
- 最多会对  appendTail、deleteHead 进行  10000  次调用

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 栈（Stack）
```

#### 提交

```py
# Python3
class CQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def appendTail(self, value: int) -> None:
        self.stack_in.append(value)

    def deleteHead(self) -> int:
        if not self.stack_out:
            if not self.stack_in:
                return -1
            else:
                while self.stack_in:
                    self.stack_out.append(self.stack_in.pop())
                return self.stack_out.pop()
        else:
            return self.stack_out.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
```

#### 参考

##### 方法一：双栈

**思路和算法**

维护两个栈，第一个栈支持插入操作，第二个栈支持删除操作。

根据栈先进后出的特性，我们每次往第一个栈里插入元素后，第一个栈的底部元素是最后插入的元素，第一个栈的顶部元素是下一个待删除的元素。为了维护队列先进先出的特性，我们引入第二个栈，用第二个栈维护待删除的元素，在执行删除操作的时候我们首先看下第二个栈是否为空。如果为空，我们将第一个栈里的元素一个个弹出插入到第二个栈里，这样第二个栈里元素的顺序就是待删除的元素的顺序，要执行删除操作的时候我们直接弹出第二个栈的元素返回即可。

**成员变量**

- 维护两个栈 stack1 和 stack2，其中 stack1 支持插入操作，stack2 支持删除操作

**构造方法**

- 初始化 stack1 和 stack2 为空

**插入元素**

插入元素对应方法 appendTail

- stack1 直接插入元素

**删除元素**

删除元素对应方法 deleteHead

- 如果 stack2 为空，则将 stack1 里的所有元素弹出插入到 stack2 里
- 如果 stack2 仍为空，则返回 -1，否则从 stack2 弹出一个元素并返回

![双栈](https://assets.leetcode-cn.com/solution-static/jianzhi_09/jianzhi_9.gif)

```c++
// C++
class CQueue {
    stack<int> stack1,stack2;
public:
    CQueue() {
        while (!stack1.empty()) {
            stack1.pop();
        }
        while (!stack2.empty()) {
            stack2.pop();
        }
    }

    void appendTail(int value) {
        stack1.push(value);
    }

    int deleteHead() {
        // 如果第二个栈为空
        if (stack2.empty()) {
            while (!stack1.empty()) {
                stack2.push(stack1.top());
                stack1.pop();
            }
        }
        if (stack2.empty()) {
            return -1;
        } else {
            int deleteItem = stack2.top();
            stack2.pop();
            return deleteItem;
        }
    }
};
```

```java
// Java
class CQueue {
    Deque<Integer> stack1;
    Deque<Integer> stack2;

    public CQueue() {
        stack1 = new LinkedList<Integer>();
        stack2 = new LinkedList<Integer>();
    }

    public void appendTail(int value) {
        stack1.push(value);
    }

    public int deleteHead() {
        // 如果第二个栈为空
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
        if (stack2.isEmpty()) {
            return -1;
        } else {
            int deleteItem = stack2.pop();
            return deleteItem;
        }
    }
}
```

```c#
// C#
public class CQueue
{

    private Stack<int> stack1;
    private Stack<int> stack2;

    public CQueue()
    {
        stack1 = new Stack<int>();
        stack2 = new Stack<int>();
    }

    public void AppendTail(int value)
    {
        stack1.Push(value);
    }

    public int DeleteHead()
    {
        if (stack2.Count == 0)
        {
            while (stack1.Count != 0)
            {
                stack2.Push(stack1.Pop());
            }
        }
        if (stack2.Count == 0)
        {
            return -1;
        }
        else
        {
            int deleteItem = stack2.Pop();
            return deleteItem;
        }
    }
}
```

```golang
// Golang
type CQueue struct {
    stack1, stack2 *list.List
}

func Constructor() CQueue {
    return CQueue{
        stack1: list.New(),
        stack2: list.New(),
    }
}

func (this *CQueue) AppendTail(value int)  {
    this.stack1.PushBack(value)
}

func (this *CQueue) DeleteHead() int {
    // 如果第二个栈为空
    if this.stack2.Len() == 0 {
        for this.stack1.Len() > 0 {
            this.stack2.PushBack(this.stack1.Remove(this.stack1.Back()))
        }
    }
    if this.stack2.Len() != 0 {
        e := this.stack2.Back()
        this.stack2.Remove(e)
        return e.Value.(int)
    }
    return -1
}
```

**复杂度分析**

- 时间复杂度：对于插入和删除操作，时间复杂度均为 O(1)。插入不多说，对于删除操作，虽然看起来是 O(n) 的时间复杂度，但是仔细考虑下每个元素只会「至多被插入和弹出 stack2 一次」，因此均摊下来每个元素被删除的时间复杂度仍为 O(1)。

- 空间复杂度：O(n)。需要使用两个栈存储已有的元素。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/mian-shi-ti-09-yong-liang-ge-zhan-shi-xian-dui-l-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
