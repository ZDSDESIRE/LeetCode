# 树的遍历问题汇总（Traversal）

如下图, 三种遍历方式, 可用同一种递归思想实现：

![traversal](../images/traversal/traversal.png)

1. 先序遍历(PreOrder, 按照先访问根节点的顺序)

```js
// JavaScript
var preorderTraversal = function (root) {
  const res = [];
  function traversal(root) {
    if (root !== null) {
      res.push(root.val); // 访问根节点的值
      traversal(root.left); // 递归遍历左子树
      traversal(root.right); // 递归遍历右子树
    }
  }
  traversal(root);
  return res;
};
```

2. 中序遍历(InOrder, 按照根节点在中间访问的顺序)

```js
// JavaScript
var inorderTraversal = function (root) {
  const res = [];
  function traversal(root) {
    if (root !== null) {
      traversal(root.left);
      res.push(root.val);
      traversal(root.right);
    }
  }
  traversal(root);
  return res;
};
```

例题：
[94.二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) 3. 后续遍历(PosterOrder, 按照根节点在后面访问的顺序)

```js
// JavaScript
var postorderTraversal = function (root) {
  const res = [];
  function traversal(root) {
    if (root !== null) {
      traversal(root.left);
      traversal(root.right);
      res.push(root.val);
    }
  }
  traversal(root);
  return res;
};
```

例题：
[145.二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/)
[590.N 叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/)

1.
