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
