### 147.对链表进行插入排序（中等）

对链表进行插入排序。

![1](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)
插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

**插入排序算法：**

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

示例 1：

```text
输入: 4->2->1->3
输出: 1->2->3->4
```

示例  2：

```text
输入: -1->5->3->4->0
输出: -1->0->3->4->5
```

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/insertion-sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 链表（Linked List）  # 排序（Sort）
```

#### 提交

```js
var insertionSortList = function (head) {
  return sort(head, new ListNode(0));
};
var sort = (cur, start) => {
  while (cur) {
    // 当前节点
    var next = cur.next,
      left = start; // cur.next会被改，暂存。每次从第0节点起
    while (left.next && left.next.val < cur.val) left = left.next; // 找 插入位置左侧节点left，即第一个右侧节点值比当前节点大的节点
    cur.next = left.next; // 当前节点 与 插入位置右侧节点 相连
    left.next = cur; // 当前节点 与 插入位置左侧节点 相连
    cur = next; // 迭代到原来的 当前节点右侧节点
  }
  return start.next; // 返回辅助链表的next，不用考虑排序后链表的第0节点在哪里
};
```

#### 参考

##### 方法一：从前往后找插入点

插入排序的基本思想是，维护一个有序序列，初始时有序序列只有一个元素，每次将一个新的元素插入到有序序列中，将有序序列的长度增加 1，直到全部元素都加入到有序序列中。

如果是数组的插入排序，则数组的前面部分是有序序列，每次找到有序序列后面的第一个元素（待插入元素）的插入位置，将有序序列中的插入位置后面的元素都往后移动一位，然后将待插入元素置于插入位置。

对于链表而言，插入元素时只要更新相邻节点的指针即可，不需要像数组一样将插入位置后面的元素往后移动，因此插入操作的时间复杂度是 O(1)，但是找到插入位置需要遍历链表中的节点，时间复杂度是 O(n)，因此链表插入排序的总时间复杂度仍然是 O(n^2)，其中 n 是链表的长度。

对于单向链表而言，只有指向后一个节点的指针，因此需要从链表的头节点开始往后遍历链表中的节点，寻找插入位置。

对链表进行插入排序的具体过程如下：

1. 首先判断给定的链表是否为空，若为空，则不需要进行排序，直接返回。

2. 创建哑节点 dummyHead，令 dummyHead.next = head。引入哑节点是为了便于在 head 节点之前插入节点。

3. 维护 lastSorted 为链表的已排序部分的最后一个节点，初始时 lastSorted = head。

4. 维护 curr 为待插入的元素，初始时 curr = head.next。

5. 比较 lastSorted 和 curr 的节点值。

   - 若 lastSorted.val <= curr.val，说明 curr 应该位于 lastSorted 之后，将 lastSorted 后移一位，curr 变成新的 lastSorted。
   - 否则，从链表的头节点开始往后遍历链表中的节点，寻找插入 curr 的位置。令 prev 为插入 curr 的位置的前一个节点，进行如下操作，完成对 curr 的插入：

   ```js
   lastSorted.next = curr.next;
   curr.next = prev.next;
   prev.next = curr;
   ```

6. 令 curr = lastSorted.next，此时 curr 为下一个待插入的元素。

7. 重复第 5 步和第 6 步，直到 curr 变成空，排序结束。

8. 返回 dummyHead.next，为排序后的链表的头节点。

```js
// JavaScript
var insertionSortList = function (head) {
  if (head === null) {
    return head;
  }
  const dummyHead = new ListNode(0);
  dummyHead.next = head;
  let lastSorted = head,
    curr = head.next;
  while (curr !== null) {
    if (lastSorted.val <= curr.val) {
      lastSorted = lastSorted.next;
    } else {
      let prev = dummyHead;
      while (prev.next.val <= curr.val) {
        prev = prev.next;
      }
      lastSorted.next = curr.next;
      curr.next = prev.next;
      prev.next = curr;
    }
    curr = lastSorted.next;
  }
  return dummyHead.next;
};
```

```java
// Java
class Solution {
    public ListNode insertionSortList(ListNode head) {
        if (head == null) {
            return head;
        }
        ListNode dummyHead = new ListNode(0);
        dummyHead.next = head;
        ListNode lastSorted = head, curr = head.next;
        while (curr != null) {
            if (lastSorted.val <= curr.val) {
                lastSorted = lastSorted.next;
            } else {
                ListNode prev = dummyHead;
                while (prev.next.val <= curr.val) {
                    prev = prev.next;
                }
                lastSorted.next = curr.next;
                curr.next = prev.next;
                prev.next = curr;
            }
            curr = lastSorted.next;
        }
        return dummyHead.next;
    }
}
```

```c++
// C++
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
        if (head == nullptr) {
            return head;
        }
        ListNode* dummyHead = new ListNode(0);
        dummyHead->next = head;
        ListNode* lastSorted = head;
        ListNode* curr = head->next;
        while (curr != nullptr) {
            if (lastSorted->val <= curr->val) {
                lastSorted = lastSorted->next;
            } else {
                ListNode *prev = dummyHead;
                while (prev->next->val <= curr->val) {
                    prev = prev->next;
                }
                lastSorted->next = curr->next;
                curr->next = prev->next;
                prev->next = curr;
            }
            curr = lastSorted->next;
        }
        return dummyHead->next;
    }
};
```

```py
# Python3
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        lastSorted = head
        curr = head.next

        while curr:
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummyHead
                while prev.next.val <= curr.val:
                    prev = prev.next
                lastSorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = lastSorted.next

        return dummyHead.next
```

```golang
// Golang
func insertionSortList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    dummyHead := &ListNode{Next: head}
    lastSorted, curr := head, head.Next
    for curr != nil {
        if lastSorted.Val <= curr.Val {
            lastSorted = lastSorted.Next
        } else {
            prev := dummyHead
            for prev.Next.Val <= curr.Val {
                prev = prev.Next
            }
            lastSorted.Next = curr.Next
            curr.Next = prev.Next
            prev.Next = curr
        }
        curr = lastSorted.Next
    }
    return dummyHead.Next
}
```

```c
// C
struct ListNode *insertionSortList(struct ListNode *head) {
    if (head == NULL) {
        return head;
    }
    struct ListNode *dummyHead = malloc(sizeof(struct ListNode));
    dummyHead->val = 0;
    dummyHead->next = head;
    struct ListNode *lastSorted = head;
    struct ListNode *curr = head->next;
    while (curr != NULL) {
        if (lastSorted->val <= curr->val) {
            lastSorted = lastSorted->next;
        } else {
            struct ListNode *prev = dummyHead;
            while (prev->next->val <= curr->val) {
                prev = prev->next;
            }
            lastSorted->next = curr->next;
            curr->next = prev->next;
            prev->next = curr;
        }
        curr = lastSorted->next;
    }
    return dummyHead->next;
}
```

**复杂度分析**

- 时间复杂度：O(n^2)，其中 n 是链表的长度。

- 空间复杂度：O(1)。

**注**
作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/insertion-sort-list/solution/dui-lian-biao-jin-xing-cha-ru-pai-xu-by-leetcode-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
