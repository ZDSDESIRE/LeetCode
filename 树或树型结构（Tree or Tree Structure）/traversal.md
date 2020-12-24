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
[94.二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

3. 后续遍历(PosterOrder, 按照根节点在后面访问的顺序)

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

100 相同的树

可以利用这种递归思想并发同时爬两棵树

```js
var isSameTree = function (p, q) {
  function traversal(root1, root2) {
    if (root1 === null && root2 !== null) {
      return false;
    } else if (root1 !== null && root2 === null) {
      return false;
    } else if (root1 === null && root2 === null) {
      return true;
    } else {
      return (
        root1.val === root2.val &&
        traversal(root1.left, root2.left) &&
        traversal(root1.right, root2.right)
      );
    }
  }
  return traversal(p, q);
};
```

226 翻转二叉树

这种算法可以帮助 Homebrew 作者 Max Howell 解开 Google 的算法面试题

```js
var invertTree = function (root) {
  function traversal(root) {
    if (root === null) {
      return null;
    } else {
      [root.left, root.right] = [traversal(root.right), traversal(root.left)];
      return root;
    }
  }
  return traversal(root);
};
```

590 N 叉树的后序遍历

我们还可以用此种算法解决 N 叉树的问题

```js
var postorder = function (root) {
  const res = [];
  function traversal(root) {
    if (root !== null) {
      root.children.forEach((child) => {
        traversal(child);
      });
      res.push(root.val);
    }
  }
  traversal(root);
  return res;
};
```

如果你已对这种写法审美疲劳, 可以换个写法, 使用匿名函数

```js
var postorder = function (root) {
  const res = [];
  (function (root) {
    if (root !== null) {
      root.children.forEach((child) => {
        arguments.callee(child);
      });
      res.push(root.val);
    }
  })(root);
  return res;
};
```

还可以利用栈来迭代

```js
var postorder = function (root) {
  if (root === null) {
    return [];
  }
  const res = [];
  const arr = [root];
  while (arr.length) {
    const cur = arr.pop();
    res.push(cur.val);
    for (let i = cur.children.length - 1; i >= 0; i--) {
      arr.push(cur.children[i]);
    }
  }
  return res.reverse();
};
```

103 二叉树的锯齿形层次遍历

大白话, 蛇皮走位爬树

```js
var zigzagLevelOrder = function (root) {
  if (root === null) {
    return [];
  } else {
    let res = [];
    function traversal(root, depth) {
      if (root !== null) {
        if (res[depth] === undefined) {
          res[depth] = [];
        }
        res[depth].push(root.val);
        traversal(root.left, depth + 1);
        traversal(root.right, depth + 1);
      }
    }
    traversal(root, 0);
    res.forEach((item, index) => {
      if (index & 1) {
        res[index] = item.reverse();
      }
    });
    return res;
  }
};
```

优化

```js
var zigzagLevelOrder = function (root) {
  if (root === null) {
    return [];
  } else {
    let res = [];
    function traversal(root, depth) {
      if (root !== null) {
        if (res[depth] === undefined) {
          res[depth] = [];
        }
        if (depth & 1) {
          res[depth].unshift(root.val);
        } else {
          res[depth].push(root.val);
        }
        traversal(root.left, depth + 1);
        traversal(root.right, depth + 1);
      }
    }
    traversal(root, 0);
    return res;
  }
};
```

230 二叉搜索树中第 K 小的元素

```js
var kthSmallest = function (root, k) {
  let arr = [];
  function traversal(node) {
    if (node !== null) {
      traversal(node.left);
      arr.push(node.val);
      traversal(node.right);
    }
  }
  traversal(root);
  return arr[k - 1];
};
```

优化, 减少遍历次数

```js
var kthSmallest = function (root, k) {
  let arr = [];
  function traversal(node) {
    if (node !== null && arr.length < k) {
      traversal(node.left);
      arr.push(node.val);
      traversal(node.right);
    }
  }
  traversal(root);
  return arr[k - 1];
};
```

进一步优化, 使用 O(1)的额外空间

```js
var kthSmallest = function (root, k) {
  let res;
  let count = 0;
  function traversal(node) {
    if (node !== null) {
      if (count < k) {
        traversal(node.left);
      }
      if (++count === k) {
        res = node.val;
      }
      if (count < k) {
        traversal(node.right);
      }
    }
  }
  traversal(root);
  return res;
};
```

102 二叉树的层序遍历

```js
var levelOrder = function (root) {
  const res = [];
  function traversal(root, depth) {
    if (root !== null) {
      if (!res[depth]) {
        res[depth] = [];
      }
      traversal(root.left, depth + 1);
      res[depth].push(root.val);
      traversal(root.right, depth + 1);
    }
  }
  traversal(root, 0);
  return res;
};
```

199 二叉树的右视图

基本思路: 先序遍历, 记录每一层深度下的节点的值, 并先记录左节点再记录右节点, 则最后记录的值即为该层深度的右视图看到的值

```js
var rightSideView = function (root) {
  const arr = [];
  function traversal(root, depth) {
    if (root) {
      if (arr[depth] === undefined) {
        arr[depth] = [];
      }
      arr[depth].push(root.val);
      traversal(root.left, depth + 1);
      traversal(root.right, depth + 1);
    }
  }
  traversal(root, 0);
  const res = [];
  for (let i = 0; i < arr.length; ++i) {
    res.push(arr[i][arr[i].length - 1]);
  }
  return res;
};
```

104 二叉树的最大深度

```js
var maxDepth = function (root) {
  let res = 0;
  function traversal(root, depth) {
    if (root !== null) {
      if (depth > res) {
        res = depth;
      }
      if (root.left) {
        traversal(root.left, depth + 1);
      }
      if (root.right) {
        traversal(root.right, depth + 1);
      }
    }
  }
  traversal(root, 1);
  return res;
};
```

107 二叉树的层次遍历 II

```js
var levelOrderBottom = function (root) {
  if (root === null) {
    return [];
  }
  let res = [];
  function traversal(root, depth) {
    if (root !== null) {
      if (!res[depth]) {
        res[depth] = [];
      }
      traversal(root.left, depth + 1);
      res[depth].push(root.val);
      traversal(root.right, depth + 1);
    }
  }
  traversal(root, 0);
  return res.reverse();
};
```

671 二叉树中第二小的节点

```js
var findSecondMinimumValue = function (root) {
  let arr = [];
  (function traversal(root) {
    if (root !== null) {
      traversal(root.left);
      arr.push(root.val);
      traversal(root.right);
    }
  })(root);
  let _arr = [...new Set(arr)].sort();
  return _arr[1] ? _arr[1] : -1;
};
```

1038 从二叉搜索树到更大和树

```js
var bstToGst = function(root) {
  let sum = 0
  function traversal (root) {
    if (root !== null) {
      traversal(root.right)
      root.val += sum
      sum = root.val
      traversal(root.left)
    }
  }
  traversal(root)
  return root
}`
```

538 把二叉搜索树转换为累加树

```js
var convertBST = function (root) {
  let sum = 0;
  function traversal(root) {
    if (root !== null) {
      traversal(root.right);
      sum += root.val;
      root.val = sum;
      traversal(root.left);
    }
  }
  traversal(root);
  return root;
};
```

700 二叉搜索树中的搜索

```js
var searchBST = function (root, val) {
  function traversal(root) {
    if (root !== null) {
      if (root.val === val) {
        return root;
      } else if (root.val < val) {
        return traversal(root.right);
      } else {
        return traversal(root.left);
      }
    } else {
      return root;
    }
  }
  return traversal(root);
};
```

559 N 叉树的最大深度

```js
var maxDepth = function (root) {
  if (root === null) {
    return 0;
  } else {
    let depth = 1;
    function traversal(root, curDepth) {
      if (root !== null) {
        if (curDepth > depth) {
          depth = curDepth;
        }
        root.children.forEach((child) => traversal(child, curDepth + 1));
      }
    }
    traversal(root, 1);
    return depth;
  }
};
```

589 N 叉树的前序遍历

```js
var preorder = function (root) {
  const res = [];
  function traversal(root) {
    if (root !== null) {
      res.push(root.val);
      root.children.forEach((child) => traversal(child));
    }
  }
  traversal(root);
  return res;
};
```

897 递增顺序查找树

```js
var increasingBST = function (root) {
  const arr = [];
  function traversal(root) {
    if (root !== null) {
      traversal(root.left);
      arr.push(root.val);
      traversal(root.right);
    }
  }
  traversal(root);
  const res = new TreeNode(arr[0]);
  let currentNode = res;
  for (let i = 0; i < arr.length - 1; i++) {
    currentNode.left = null;
    currentNode.right = new TreeNode(arr[i + 1]);
    currentNode = currentNode.right;
  }
  return res;
};
```

作者：magisilk
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/solution/yi-tao-quan-fa-shua-diao-nge-bian-li-shu-de-wen-9/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
