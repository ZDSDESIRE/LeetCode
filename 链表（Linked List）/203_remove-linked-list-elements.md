### 203. 移除链表元素（简单）

给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

示例 1：
![removelinked-list](https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg)

```text
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
```

示例 2：

```text
输入：head = [], val = 1
输出：[]
```

示例 3：

```text
输入：head = [7,7,7,7], val = 7
输出：[]
```

提示：

- 列表中的节点在范围 [0, 104] 内
- 1 <= Node.val <= 50
- 0 <= k <= 50

**注**
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-linked-list-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

```py
# 链表（Linked List）
```

#### 提交

```js
// JavaScript
/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
//  迭代
var removeElements = function (head, val) {
  if (head === null) return head;
  const dummyNode = new ListNode(0); // 创建虚拟头节点
  dummyNode.next = head;
  let temp = dummyNode;
  while (temp.next != null) {
    if (temp.next.val === val) {
      temp.next = temp.next.next;
    } else {
      temp = temp.next;
    }
  }
  return dummyNode.next;
};

// 递归
var removeElements = function (head, val) {
  if (head === null) return head;
  head.next = removeElements(head.next, val);
  return head.val === val ? head.next : head;
};
```
